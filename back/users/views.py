import random
import string
from shlex import join
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import DBUsers


class CreateUser(APIView):

    def post(self, request, format=None):
        name = self.request.data.get("name")
        surname = self.request.data.get("surname")
        login = self.request.data.get("login")
        password = self.request.data.get("password")
        email = self.request.data.get("email")
        token = generation_token()
        if len(login) < 8:
            return Response({"err": "Логин слишком короткий"})
        else:
            if DBUsers.objects.filter(login=login).exists():
                return Response({"err": "Логин есть"})
        if len(password) < 8:
            return Response({"err": "Пароль слишком короткий"})
        if DBUsers.objects.filter(email=email).exists():
            return Response({"err": "Такая почта уже есть"})

        create_user = DBUsers(
            token=token,
            name=name,
            surname=surname,
            email=email,
            login=login,
            password=password,
        )
        create_user.save()
        info_user = {
            'token': token,
        }
        return Response(token)


def generation_token():
    letters = string.ascii_lowercase
    token = (join(random.choice(letters) for i in range(32))).replace(' ', '')
    if DBUsers.objects.filter(token=token):
        return generation_token
    return token


class AuthorizationUser(APIView):

    def post(self, request, format=None):
        login = self.request.data.get("login")
        password = self.request.data.get("password")
        db = DBUsers.objects.all()
        print(login, password)
        for user in db:
            print(user.login, user.password)
            if login in user.login and password in user.password:
                return Response((user.token))
        db.exists()
        return Response({"err": 'Проверьте данные'})

    def get(self, request, format=None):
        token = self.request.query_params.get('token')
        db = DBUsers.objects.filter(token=token)[0]
        info_user = {
            'fullName': db.name + ' ' + db.surname,
            'email': db.email,
        }
        return Response(info_user)
