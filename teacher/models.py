from django.contrib.auth.models import AbstractUser
from django.db import models

class Teacher(AbstractUser):
    # Add fields specific to the Teacher model
    is_teacher = models.BooleanField(default=True)

    def __str__(self):
        return self.username
