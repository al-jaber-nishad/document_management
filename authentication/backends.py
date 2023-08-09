from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomUserBackend(ModelBackend):
    def authenticate(username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(username=username)
            print("user name", user.username)
        except CustomUser.DoesNotExist:
            print("Doesnot exists")
            return None
        
        print(user.check_password(password))
        print("User", user)

        if user.check_password(password):
            return user
        return None
