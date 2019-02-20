from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=10)
    pw1 = models.CharField(max_length=20)
    pw2 = models.CharField(max_length=20)

    # def __str__(self):
    #     return self.name

