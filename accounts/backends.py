from accounts.models import User
from django.contrib.auth.backends import BaseBackend

class EmailBackend(BaseBackend):

    def authenticate(self, request, username = ..., password = ..., **kwargs):

        try:

            user_object  = User.objects.get(email = username)

            if user_object.check_password(password):

                return user_object

            else:

                return None

        except:

            return None