from django.db import models

# Create your models here.

class Events(models.Model):
    title = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return self.title