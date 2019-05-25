from djang.db.models.signals import post_save
from djang.contrib.auth.models imprt User
from django.dispatch import receiver
from .models import profile

@receiver(post_save , sender=User)
def create_profile(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save , sender=User)
def save_profile(sender , instance , **kwargs):
    instance.profile.save()