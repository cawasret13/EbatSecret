import ast
import time
from datetime import datetime
import json
import random
import string
from shlex import join

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.models import photos, rooms
from users.models import DBUsers

url_server = '45.9.24.240:8000'


class ImageRoom(APIView):

    def get(self, request, format=None):
        data = []
        images = photos.objects.all()
        for image in images:
            data.append({"image": f'http://{url_server}/media/' + image.photo.name, "id": image.id_photo})
        return Response(json.dumps(data))


def generation_token():
    letters = string.ascii_lowercase
    token = (join(random.choice(letters) for i in range(16))).replace(' ', '')
    if rooms.objects.filter(id_room=token):
        return generation_token
    return token


class CreateRoom(APIView):

    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_icon = self.request.data.get("id_icon")
        name = self.request.data.get("name")
        max = self.request.data.get("max")
        max_price = self.request.data.get("max_price")
        date = self.request.data.get("date")
        autoRes = self.request.data.get("autoRes")
        private = self.request.data.get("private")

        if name == '' or name == ' ' or name == None or name == 'null':
            return Response({"err": "Введите имя"})
        if max == '' or max == None or max == 'null':
            return Response({"err": "Поле игроков не может быть пустым"})
        if int(max) < 2 and int(max) != None:
            return Response({"err": "Игроков минимум 2"})
        if max_price == '':
            max_price = 0

        if '1' in autoRes:
            autoRes = True
        else:
            autoRes = False
        if '1' in private:
            private = True
        else:
            private = False
        room = rooms(
            id_room=generation_token(),
            id_created=token,
            id_icon=id_icon,
            name=name,
            description='',
            numHum=int(max),
            max_price=int(max_price),
            date=date,
            autoRes=bool(autoRes),
            private=private,
            users=[{"token": token, "wish": '...', 'ready': True, 'from':False, 'fromNam':True}],
            OK_list='[]',
            listSant='[]',
            play=False,
            endPlay=False,
        )
        room.save()
        return Response({"mas": "Успешно"})


class GetDataRooms(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        res = []
        data = rooms.objects.filter(id_created=token)
        for room in data:
            nowPlayer = len(ast.literal_eval(room.users))
            img = photos.objects.get(id_photo=int(room.id_icon))
            url = f'http://{url_server}/media/' + img.photo.name
            flag = False
            for us in (ast.literal_eval(room.listSant)):
                if (us['from'] == token):
                    if (us['guess'] == True):
                        flag = True

            info = {
                "id_room": room.id_room,
                "name": room.name,
                "maxHum": room.numHum,
                "private": room.private,
                "icon": url,
                "nowPlayer": nowPlayer,
                "play": room.play,
                "push": len(ast.literal_eval(room.OK_list))
            }
            if flag == False:
                res.append(info)
        res = res[::-1]
        return Response(json.dumps(res))


class GetDataRoom(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id")
        res = []
        data = rooms.objects.filter(id_room=id_room)
        nowPlayer = ast.literal_eval(data[0].users)
        user_ = DBUsers.objects.get(token=token)
        why = False
        wish = '...'
        for user in nowPlayer:
            if token == user['token']:
                wish = user['wish']
                ready = user['ready']
                why = True
        if why == False:
            ready = False
        for room in data:
            img = photos.objects.get(id_photo=int(room.id_icon))
            url = f'http://{url_server}/media/' + img.photo.name
            if token == room.id_created:
                status = True
            else:
                status = False
            lenok = len(ast.literal_eval(room.OK_list))
            info = {
                "id_room": room.id_room,
                "id_icon": room.id_icon,
                "name": room.name,
                "maxHum": room.numHum,
                "private": room.private,
                "icon": url,
                "maxPrice": room.max_price,
                "desc": room.description,
                "autoPlay": room.autoRes,
                "nowPlayer": len(nowPlayer),
                "created": status,
                "why": why,
                "play": room.play,
                "oklen": lenok,
                "wish": wish,
                "you": (user_.name + ' ' + user_.surname),
                "ready": ready
            }
            res.append(info)
        return Response(json.dumps(res))


class SettingsRoom(APIView):

    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id")
        data = json.loads(self.request.data.get("data"))
        room = rooms.objects.get(id_room=id_room)
        if data['name'] == '' or data['name'] == ' ':
            return Response({"err": "Введите имя"})
        if int(data['maxHum']) < 2:
            return Response({"err": "Игроков минимум 2"})
        if (room.id_created == token):
            room.name = data['name']
            room.numHum = data['maxHum']
            room.private = data['private']
            room.max_price = data['maxPrice']
            room.description = data['desc']
            room.autoRes = data['autoPlay']
            room.id_icon = data['id_icon']
            room.save()
            img = photos.objects.get(id_photo=int(room.id_icon))
            url = f'http://{url_server}/media/' + img.photo.name
            info = {
                "id_room": room.id_room,
                "id_icon": room.id_icon,
                "name": room.name,
                "maxHum": room.numHum,
                "private": room.private,
                "icon": url,
                "maxPrice": room.max_price,
                "desc": room.description,
                "autoPlay": room.autoRes,
            }
            return Response(json.dumps(info))
        return Response("0")


class DeleteRoom(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id")
        room = rooms.objects.get(id_room=id_room)
        if (room.id_created == token):
            room.delete()
            return Response("Good")
        return Response("Bad")


class Players(APIView):

    def post(self, request, format=None):
        id_room = self.request.data.get("id")
        room = rooms.objects.get(id_room=id_room)
        players = ast.literal_eval(room.users)
        players_info = []
        for player in players:
            db = DBUsers.objects.get(token=player['token'])
            info = {
                "fullname": (db.name + ' ' + db.surname),
                "ready": player['ready']
            }
            players_info.append(info)
        return Response(json.dumps(players_info))


class Rooms(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        res = []
        data = rooms.objects.all()
        for room in data:
            nowPlayer = ast.literal_eval(room.users)
            why = False
            for tokens in nowPlayer:
                if (token == tokens['token']):
                    why = True
            flag = False
            if room.listSant != None:
                for us in (ast.literal_eval(room.listSant)):
                    if (us['from'] == token):
                        if (us['guess'] == True):
                            flag = True
            if (room.id_created != token):
                img = photos.objects.get(id_photo=int(room.id_icon))
                url = f'http://{url_server}/media/' + img.photo.name
                info = {
                    "id_room": room.id_room,
                    "name": room.name,
                    "maxHum": room.numHum,
                    "private": room.private,
                    "icon": url,
                    "nowPlayer": len(nowPlayer),
                }
                if why == False and room.play == False and flag == False:
                    res.append(info)
        res = res[::-1]
        return Response(json.dumps(res))


class ForPlay(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        db = rooms.objects.all()
        res = []
        for room in db:
            if (room.id_created != token):
                flag = False
                if room.listSant != None:
                    for us in (ast.literal_eval(room.listSant)):
                        if (us['from'] == token):
                            if (us['guess'] == True):
                                flag = True
                users = ast.literal_eval(room.users)
                for user in users:
                    info = []
                    if token in user['token']:
                        img = photos.objects.get(id_photo=int(room.id_icon))
                        url = f'http://{url_server}/media/' + img.photo.name
                        info = {
                            "id_room": room.id_room,
                            "name": room.name,
                            "maxHum": room.numHum,
                            "private": room.private,
                            "icon": url,
                            "nowPlayer": len(users),
                            "play": room.play,
                        }
                        if flag == False:
                            res.append(info)
        res = res[::-1]
        return Response(json.dumps(res))


class AddRoom(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        db = rooms.objects.get(id_room=id_room)
        if db.private == True:
            a = ast.literal_eval(db.OK_list)
            for player in a:
                if player['token'] == token:
                    return Response({"err": "Вы уже подали завку"})
            a.append({'token': token})
            db.OK_list = a
            db.save()
            return Response({"mas": "Ждемс..."})
        else:
            a = ast.literal_eval(db.users)
            for player in a:
                if player['token'] == token:
                    return Response({"err": "Вы уже подали завку"})
            if len(ast.literal_eval(db.users)) == int(db.numHum):
                return Response({"err": "Мест нет"})
            else:
                a.append({'token': token, 'wish': "...", 'ready': False, 'from':False, 'fromNam':True})
                db.users = a
                db.save()
            return Response({"mas": "Ждемс..."})
        return Response("")


class OkList(APIView):

    def get(self, request, forma=None):
        id_room = id_session = self.request.query_params.get('id_room')
        list = []
        db = rooms.objects.get(id_room=id_room)
        room = ast.literal_eval(db.OK_list)
        for player in room:
            user = DBUsers.objects.get(token=player['token'])
            res = {
                'fullname': (user.name + ' ' + user.surname)
            }
            list.append(res)
        return Response(json.dumps(list))

    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        status = self.request.data.get("status")
        id = self.request.data.get("id")
        room = rooms.objects.get(id_room=id_room)
        token_user = ''
        print(len(ast.literal_eval(room.users)), int(room.numHum), status)
        if (len(ast.literal_eval(room.users))) < int(room.numHum):
            if room.id_created == token:
                if status == 'true':
                    if room.id_room == id_room:
                        lsOK = ast.literal_eval(room.OK_list)
                        ids = 0
                        for ok in lsOK:
                            if (int(id) == int(ids)):
                                db_room = ast.literal_eval(room.users)
                                db_room.append({'token': ok['token'], "wish": '...', 'ready': False, 'from':False, 'fromNam':True})
                                room.users = db_room
                                okLs = ast.literal_eval(room.OK_list)
                                okLs.remove({'token': ok['token']})
                                room.OK_list = okLs
                            ids = +1
                        room.save()
                        return Response('Добавлен', status=200)
                else:
                    if room.id_room == id_room:
                        lsOK = ast.literal_eval(room.OK_list)
                        ids = 0
                        for ok in lsOK:
                            if (int(id) == int(ids)):
                                okLs = ast.literal_eval(room.OK_list)
                                okLs.remove({'token': ok['token']})
                                room.OK_list = okLs
                            ids = +1
                        room.save()
                        return Response('Удален из списка')
        return Response("Мест нет")


class Exit(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        room = rooms.objects.get(id_room=id_room)
        if room.id_created != token:
            lsOK = ast.literal_eval(room.users)
            ids = 0
            for ok in lsOK:
                if ok['token'] == token:
                    okLs = ast.literal_eval(room.users)
                    okLs.remove({'token': ok['token'], 'wish': ok['wish'], 'ready': ok['ready'], 'from':ok['from'], 'fromNam':ok['fromNam']})
                    room.users = okLs
                ids = +1
            room.save()
            return Response('Вы вышли')
        return Response("0")


class Play(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        room = rooms.objects.get(id_room=id_room)
        if (len(ast.literal_eval(room.users))) == int(room.numHum):
            flag = True
            for player in ast.literal_eval(room.users):
                if player['ready'] == False:
                    flag = False
            if room.id_created == token and flag:
                print("Игра началась")
                room.play = True
                room.date = datetime.date(datetime.now())
                room.listSant = PlayGenerate(ast.literal_eval(room.users))
                room.save()
            else:
                return Response("Не все игроки готовы")
        return Response("Игра началась")


def PlayGenerate(data):
    list = []
    listUsers = data
    black_list_from = []
    black_list_to = []
    flag = False
    while flag == False:
        id = random.randint(0, len(data) - 1)
        id_to = random.randint(0, len(data) - 1)
        if ((data[id]['token'] not in data[id_to]['token'])):
            # if (data[id_to]["token"] not in black_list_to and data[id]['token'] not in black_list_from):
            #     list.append({"from": data[id]['token'], "to": data[id_to]['token'], "guess": False})
            #     black_list_to.append(data[id_to]['token'])
            #     black_list_from.append(data[id]['token'])
            if (data[id]['token'] not in black_list_from) and (data[id_to]['token'] not in black_list_to):
                list.append({"from": data[id]['token'], "to": data[id_to]['token'], "guess": False})
                black_list_to.append(data[id_to]['token'])
                black_list_from.append(data[id]['token'])
        if len(black_list_from) == len(data) and len(black_list_to) == len(data):
            flag = True
    print(list)
    return list


class Resualt(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        room = rooms.objects.get(id_room=id_room)
        info = []
        for user in ast.literal_eval(room.listSant):
            if (user['from'] == token):
                user_name = ''
                for us_to in ast.literal_eval(room.listSant):
                    if us_to['to'] == token:
                        user__ = DBUsers.objects.get(token=us_to['from'])
                        user_name = user__.name + ' ' + user__.surname
                for user_ in ast.literal_eval(room.users):
                    if user_['token'] == user['to']:
                        wish = user_['wish']
                    if user_['token'] == token:
                        from_=user_['from']
                        fromNam_=user_['fromNam']
                db_from = DBUsers.objects.get(token=token)
                db = DBUsers.objects.get(token=user['to'])
                info.append({'user': (db.name + ' ' + db.surname), "guess": user['guess'],
                             "from": (db_from.name + ' ' + db_from.surname), "price": room.max_price, "wish": wish,
                             "from_": from_, "fromNam": fromNam_, "from_name":user_name})
        return Response(json.dumps(info))


class res(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        room = rooms.objects.get(id_room=id_room)
        info = []
        a = []
        for user in ast.literal_eval(room.listSant):
            if user['to'] == token:
                user__ = DBUsers.objects.get(token=user['from'])
                user_name = user__.name + ' ' + user__.surname
            if (user['from'] == token):
                user_name = ''
                for user_ in ast.literal_eval(room.users):
                    if user_['token'] == user['to']:
                        wish = user_['wish']
                    if user_['token'] == token:
                        from_=user_['from']
                        fromNam_=user_['fromNam']
                db = DBUsers.objects.get(token=user['to'])
                db_from = DBUsers.objects.get(token=token)
                user['guess'] = True
                info.append({'user': (db.name + ' ' + db.surname), "guess": user['guess'],
                             "from": (db_from.name + ' ' + db_from.surname), "price": room.max_price, "wish": wish, "from_":from_, "fromNam":fromNam_, "from_name":user_name})
            a.append(user)
        room.listSant = a
        room.save()
        return Response(json.dumps(info))


class History(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        list = []
        rooms_ = rooms.objects.all()
        for room in rooms_:
            if room.play == True:
                for user in ast.literal_eval(room.listSant):
                    if user['from'] == token and user['guess'] == True:
                        img = photos.objects.get(id_photo=int(room.id_icon))
                        url = f'http://{url_server}/media/' + img.photo.name
                        info = {
                            "id_room": room.id_room,
                            "name": room.name,
                            "icon": url,
                            "date": str(room.date),
                        }
                        list.append(info)
        list = list[::-1]
        return Response(json.dumps(list))


class wish(APIView):
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        wish = self.request.data.get("wish")
        print(wish)
        room = rooms.objects.get(id_room=id_room)
        users = []
        for user in ast.literal_eval(room.users):
            if user['token'] == token:
                print("jjj")
                user['wish'] = wish
            users.append(user)
        room.users = users
        room.save()
        return Response({"mas": "Успех"})


class SetStatus(APIView):
    def get(self, request, format=None):
        id_room = self.request.query_params.get('id_room')
        token = self.request.query_params.get('token')
        room = rooms.objects.get(id_room=id_room)
        users = []
        for user in ast.literal_eval(room.users):
            if user['token'] == token:
                if user['ready'] == True:
                    user['ready'] = False
                else:
                    user['ready'] = True
            users.append(user)
        room.users = users
        room.save()
        return Response({'mas': "Вы успешно поменяли статус"})
    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        id = self.request.data.get("id")
        room = rooms.objects.get(id_room=id_room)
        if token == room.id_created:
            users = []
            ids = 0
            for user in ast.literal_eval(room.users):
                if(ids != int(id)):
                    users.append(user)
                    print("OST")
                print(ids, id)
                ids+=1
            room.users = users
            room.save()
            return Response({'mas':'Успешно убрали пользователя'})
        else:
            return Response({'err': 'У вас нет прав'})

class getMySanta(APIView):
    def get(self, request, format=None):
        id_room = self.request.query_params.get('id_room')
        token = self.request.query_params.get('token')
        room = rooms.objects.get(id_room=id_room)
        users = []
        for user in ast.literal_eval(room.users):
            if user['token']!=token:
                flag = False
                for to in ast.literal_eval(room.listSant):
                    if to['from'] == user['token'] and to['to'] == token:
                        flag = True
                db = DBUsers.objects.get(token=user['token'])
                users.append({"fullname":(db.name +' '+ db.surname), "santa":flag})
        return Response(json.dumps(users))

    def post(self, request, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        room = rooms.objects.get(id_room=id_room)
        status = self.request.data.get("status")
        users=[]
        for user in ast.literal_eval(room.users):
            if user['token'] == token:
                if int(status) == 1:
                    user['from'] = True
                    user['fromNam'] = False
                elif int(status) == 0 :
                    user['from'] = False
                    user['fromNam'] = False
            users.append(user)
        room.users = users
        room.save()

        return Response(json.dumps(clone_(token, id_room)))
    def put(self, requset, format=None):
        token = self.request.data.get("token")
        id_room = self.request.data.get("id_room")
        room = rooms.objects.get(id_room=id_room)
        users = []
        for user in ast.literal_eval(room.users):
            user['from'] = True
            user['fromNam'] = False
            users.append(user)
        room.autoRes = True
        room.users = users
        room.save()
        return Response({"mas":"Все видят сант", "data":json.dumps(clone_(token, id_room))})

def clone_(token, id_room):
    room = rooms.objects.get(id_room=id_room)
    info = []

    for user in ast.literal_eval(room.listSant):
        if (user['from'] == token):
            user_name = ''
            for us_to in ast.literal_eval(room.listSant):
                if us_to['to'] == token:
                    user__ = DBUsers.objects.get(token=us_to['from'])
                    user_name = user__.name + ' ' + user__.surname
            for user_ in ast.literal_eval(room.users):
                if user_['token'] == user['to']:
                    wish = user_['wish']
                if user_['token'] == token:
                    from_ = user_['from']
                    fromNam_ = user_['fromNam']
            db_from = DBUsers.objects.get(token=token)
            db = DBUsers.objects.get(token=user['to'])
            info.append({'user': (db.name + ' ' + db.surname), "guess": user['guess'],
                         "from": (db_from.name + ' ' + db_from.surname), "price": room.max_price, "wish": wish,
                         "from_": from_, "fromNam": fromNam_, "from_name":user_name})
    return info
