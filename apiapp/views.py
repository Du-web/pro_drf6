from django.contrib.auth.models import Group, Permission
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from apiapp.models import User


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