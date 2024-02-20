from django.db import models
from django.contrib.auth.models import User


# Create your models here.mc
class ToDo(models.Model):
    title = models.CharField(max_length=100)                # Длина названия
    description = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)      # Created Time
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)   # Помогает связать ID пользователя

    def __str__(self) -> str:
        return self.title