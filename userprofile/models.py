from django.db import models
from users.models import User
from events.models import Events


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scheduled_event = models.ManyToManyField(Events)