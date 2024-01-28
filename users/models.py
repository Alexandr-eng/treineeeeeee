from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):

    TYPES = (
        ('MU', 'Музыка'),
        ('PO', 'Политика'),
        ('ED', 'Учеба'),
        ('DA', 'Танцы'),
        ('AR', 'Рисование'),
        ('PC', 'Компьютеры'),
        ('EA', 'Еда'),
        ('CA', 'Машины'),
    )
    type = models.CharField(max_length=2, choices=TYPES, default='C')

    def __str__(self):
        return self.username
