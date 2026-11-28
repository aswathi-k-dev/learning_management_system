from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.generics import RetrieveAPIView,DestroyAPIView


from accounts.models import User,TrainerProfile,StudentProfile
from accounts.permission import IsStudentUser

from accounts.serializers import UserSerializer,TrainerProfileSerializer,StudentProfileSerializer

# Create your views here.

class TrainerCreateView(APIView):
     
     def post(self,request):
            form_data = request.data
    
            serializer_instance = UserSerializer(data = form_data)

            if serializer_instance.is_valid():
                 cleaned_data = serializer_instance.validated_data
                 instance = User.objects.create_superuser(role="trainer",**cleaned_data)
                 serializer_instance = UserSerializer(instance)

                 return Response(data = serializer_instance.data)
            else:
                 return Response(data = serializer_instance.errors)


class StudentCreateView(APIView):

      def post(self,request):

            form_data = request.data 

            serializer_instance =  UserSerializer(data = form_data)

            if serializer_instance.is_valid():
                  
                  cleaned_data = serializer_instance.validated_data

                  instance = User.objects.create_user(role="student",**cleaned_data)

                  serializer_instance = UserSerializer(instance)

                  return Response(data = serializer_instance.data)
            
            else:

                  return Response(data = serializer_instance.errors)



class TrainerProfileUpdateView(APIView):

   authentication_classes = [authentication.TokenAuthentication]

   permission_classes = [permissions.IsAuthenticated]

   def put(self,request):

        form_data = request.data 

        trainer_profile_object = TrainerProfile.objects.get(trainer = request.user)

        serializer_instance = TrainerProfileSerializer(data = form_data,instance = trainer_profile_object)

        if serializer_instance.is_valid():

             serializer_instance.save()

             return Response(data = serializer_instance.data)
        
        else:
             return Response(data = serializer_instance.errors)


class TrainerProfileDetailView(RetrieveAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    queryset = TrainerProfile.objects.all()

    serializer_class = TrainerProfileSerializer

















      
