from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import permissions,authentication
from rest_framework.response import Response

from courses.models import Course
from courses.serializers import CourseSerializer
from courses.permissions import TrainerOnly

# Create your views here.

class CourseListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [TrainerOnly]

    serializer_class = CourseSerializer
    # queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(trainer =self.request.user)

class CourseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [TrainerOnly]

    serializer_class = CourseSerializer
    queryset = Course.objects.all()




    


    

