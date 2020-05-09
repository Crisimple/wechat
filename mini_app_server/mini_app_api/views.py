from django.shortcuts import render

# https://www.django-rest-framework.org/
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response({
            "status": True
        })
