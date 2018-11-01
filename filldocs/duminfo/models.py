from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class DumUser(models.Model):
    f1 = models.CharField(max_length=100,null=True)
    f2 = models.CharField(max_length=20,null=True)
    f3 = models.CharField(max_length=3,null=True)
    f4 = models.DateField(null=True)
    f5 = models.CharField(max_length=3, null=True)
    f6 = models.DateField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = DumUser.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = DumUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.dumuser.save()
