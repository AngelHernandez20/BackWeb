from .models import Alumno
from .serializers import AlumnoSerializer

from rest_framework import viewsets, views, filters, generics
from django.shortcuts import render

 



# -------------------------------------------------
# from rest_framework.decorators import api_view
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# @api_view(['GET'])
# def login(request):
#     User = User.objects.get(username='admin')

#     token = Token.objects.create(user=user)

#     print(token.key)
# -------------------------------------------------



# Create your views here.

class AlumnoViewSet(viewsets.ModelViewSet):
    
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoEditDelete(generics.RetrieveUpdateDestroyAPIView):    
    
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

