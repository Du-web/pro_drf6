from django.contrib.auth.models import Group, Permission
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.authentication import SessionAuthentication

from apiapp.authenticator import MyAuth
from apiapp.models import User
from apiapp.permission import MyPermission
from apiapp.throttle import MyThrottle


class Demo(APIView):

    def get(self, request, *args, **kwargs):
        # user = User.objects.all().first()
        # print(user.email)
        # print(user.groups.first().name)
        # print(user.user_permissions.first().name)

        # group = Group.objects.first()
        # print(group.user_set.first().username)
        # print(group.permissions.first().name)

        # permission = Permission.objects.first()
        # print(permission.user_set.first().username)
        # per = Permission.objects.filter(pk=1).first()
        # print(per.group_set.first().name)
        return Response('ok')


class BookAPIView(APIView):

    # authentication_classes = [MyAuth]
    # permission_classes = [MyPermission]
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response("读操作")

    def post(self, request, *args, **kwargs):
        return Response("写操作")