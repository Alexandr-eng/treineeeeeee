from django.db import models
from users.models import User
# Create your models here.

class Events(models.Model):
    title = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title