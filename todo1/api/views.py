from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        username = self.request.user
        # pass currect user
        serializer.save(username=username) 


class UserLoginApi(APIView):
    def post(self, request):
        #get username , password from request
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'refresh':str(refresh),
                'access': str(refresh.access_token), 
                })
           
        else:
            return Response({'message': 'Username or Password wrong'}, status=status.HTTP_400_BAD_REQUEST)

#class UserRegister(APIView):
#    
#    def post(self,request):
#