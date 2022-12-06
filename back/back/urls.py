from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rooms.views import ImageRoom, CreateRoom, GetDataRooms, GetDataRoom, SettingsRoom, DeleteRoom, Players, Rooms, \
    ForPlay, AddRoom, OkList, Exit, Play, Resualt, res, History, wish
from users.views import CreateUser, AuthorizationUser, Info, UserSettings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/create', CreateUser.as_view()),
    path('api/v1/user/settings', UserSettings.as_view()),
    path('api/v1/user/authorization', AuthorizationUser.as_view()),
    path('api/v1/user/info', Info.as_view()),
    path('api/v1/room/images', ImageRoom.as_view()),
    path('api/v1/room/create', CreateRoom.as_view()),
    path('api/v1/room/my', GetDataRooms.as_view()),
    path('api/v1/room/show', GetDataRoom.as_view()),
    path('api/v1/room/settings', SettingsRoom.as_view()),
    path('api/v1/room/delete', DeleteRoom.as_view()),
    path('api/v1/room/players', Players.as_view()),
    path('api/v1/room/', Rooms.as_view()),
    path('api/v1/room/play', ForPlay.as_view()),
    path('api/v1/room/add', AddRoom.as_view()),
    path('api/v1/room/listOK', OkList.as_view()),
    path('api/v1/room/exit', Exit.as_view()),
    path('api/v1/room/start', Play.as_view()),
    path('api/v1/room/resualt', Resualt.as_view()),
    path('api/v1/room/res', res.as_view()),
    path('api/v1/history', History.as_view()),
    path('api/v1/room/wish', wish.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
