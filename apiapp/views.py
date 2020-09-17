from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from apiapp.models import User


class Demo(APIView):

    def get(self, request, *args, **kwargs):
        user = User.objects.filter()
        print(user)
        return Response('ok')