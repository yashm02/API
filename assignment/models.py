from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Artist(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField('Work')

class Work(models.Model):
    LINK_CHOICES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other')
    ]
    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=LINK_CHOICES)


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)