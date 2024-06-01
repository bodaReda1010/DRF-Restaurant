from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from rest_framework.authtoken.models import Token
from django.conf import settings




class Account(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None , null=True, blank=True)
    phone = models.CharField(max_length=50)


    class Meta:
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    def __str__(self):
        return str(self.user)
    
    @receiver(post_save , sender=User)
    def create_user_account(sender , instance , created , **kwargs):
        if created:
            Account.objects.create(user=instance)


@receiver(post_save , sender =settings.AUTH_USER_MODEL)
def token_create(sender , instance , created , **kwargs):
    if created:
        Token.objects.create(user = instance)