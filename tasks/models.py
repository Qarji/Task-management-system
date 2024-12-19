from django.db import models
from users.models import User

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
