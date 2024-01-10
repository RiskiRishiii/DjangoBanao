from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'doctor'),
      (2, 'patient'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    address = models.TextField()
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pin_code = models.CharField(max_length=10)
