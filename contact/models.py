from django.db import models
from accounts.models import Account
# Create your models here.


class Contact(models.Model):
    account = models.ForeignKey(Account , on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return str(self.account)