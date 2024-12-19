from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name
