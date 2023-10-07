
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# 建立資料庫
class EnglishWord(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField()

    def __str__(self):
        return self.word
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)