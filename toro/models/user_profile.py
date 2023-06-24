from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from toro.models.vendor import Vendor

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    vendors = models.ManyToManyField(Vendor, related_name='user_profile', db_table='user_profile_client')

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        db_table = 'user_profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
