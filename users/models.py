# from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

# At this point, Used to extend "UserManager" only
class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    


