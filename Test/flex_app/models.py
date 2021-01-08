from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_name=models.CharField(max_length=30)


class User(models.Model):
    username = models.CharField(max_length=20)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = password = models.CharField(('password'), max_length=128, help_text=("Use '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>."))
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254,unique=True)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



