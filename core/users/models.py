from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user = instance)

class User(AbstractUser):
    is_freelancer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    

class Freelancer(models.Model):
    user = models.OneToOneField(User, related_name='freelancer', on_delete=models.CASCADE)
    phone= models.CharField(max_length=100, null=True, blank=True)
    skills = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    portfolio = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Client(models.Model):
    user = models.OneToOneField(User, related_name='employer', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name

