import json
import random
import string
from shlex import join
import re

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
        if name == '':
            return Response({"err":"Введите имя"})
        if surname == '':
            return Response({"err":"Введите фамилию"})
        if email == '':
            return Response({"err": "Введите почту"})
        if DBUsers.objects.filter(email=email).exists():
            return Response({"err": "Такая почта уже есть"})
        if len(login) < 5:
            return Response({"err": "Логин слишком короткий, минимум 5 символов"})
        else:
            if DBUsers.objects.filter(login=login).exists():
                return Response({"err": "Логин есть"})
        if len(password) < 8:
            return Response({"err": "Пароль слишком короткий"})


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
        if login == '':
            return Response({"err":"Введите логин"})
        if password == '':
            return Response({"err":"Введите пароль"})
        db = DBUsers.objects.all()
        print(login, password)
        for user in db:
            print(user.login, user.password)
            if login == user.login and password == user.password:
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


pass_check = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
email_check = (r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def Validation_email(email):
    if re.fullmatch(email_check, email):
        return True
    else:
        return False

class Info(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        user = DBUsers.objects.get(token=token)
        return Response(json.dumps({"fullname":(user.name + ' ' + user.surname)}))

class UserSettings(APIView):
    def get(self, request, format=None):
        token = self.request.query_params.get('token')
        user = DBUsers.objects.get(token=token)
        info={
            "name":user.name,
            "surname":user.surname,
            "email":user.email
        }
        return Response(json.dumps(info))
    def post(self, request, format=None):
        token = self.request.data.get("token")
        name = self.request.data.get("name")
        surname = self.request.data.get("surname")
        email = self.request.data.get("email")
        user = DBUsers.objects.get(token=token)
        if name == '':
            return Response({"err": "Введите имя"})
        if surname == '':
            return Response({"err": "Введите фамилию"})
        if email == '':
            return Response({"err": "Введите почту"})
        if DBUsers.objects.filter(email=email).exists():
            return Response({"err": "Такая почта уже есть"})
        user.name = name
        user.surname = surname
        user.email = email
        user.save()
        return Response(json.dumps({"mas":"Успешно!"}))