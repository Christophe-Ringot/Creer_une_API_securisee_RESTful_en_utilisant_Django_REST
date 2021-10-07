from django.conf import settings
from django.db import models

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=128)
    date = models.DateField()
    description = models.CharField(max_length=128)
    completed = models.BooleanField(default=None)

    TYPE_CHOICES = [
        ('Back', 'Back'), ('Front', 'Front'), ('iOS', 'iOS'),
        ('Android', 'Android')
    ]
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE,
                                       blank=True, null=True)



