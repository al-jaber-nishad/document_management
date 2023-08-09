from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group, Permission
from django.conf import settings



class CustomUser(User):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('regular', 'Regular'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return f"{self.username}"