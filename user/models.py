from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Types(models.TextChoices):
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"
        ADMINISTRATION = "ADMINISTRATION", "Administration"
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length = 20)
    user_type = models.CharField(max_length=20, choices=Types.choices, default=Types.STUDENT)
    email = models.EmailField(unique=True, max_length=50, blank =True, null =True)
    username = models.CharField(max_length=40, unique = True)
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = "USER"

    def __str__(self):
        return self.username
    


