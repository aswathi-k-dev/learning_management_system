from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from accounts.views import TrainerCreateView
from accounts.views import StudentCreateView
from accounts.views import TrainerProfileUpdateView
from accounts.views import TrainerProfileDetailView


urlpatterns = {

    # register trainer and student

    path("trainer/register/",TrainerCreateView.as_view()),
    path("student/register/",StudentCreateView.as_view()),

    # token generation 
    path("token/",ObtainAuthToken.as_view()),

    # profile completion 

    path("profile/complete/",TrainerProfileUpdateView.as_view()),
    




}