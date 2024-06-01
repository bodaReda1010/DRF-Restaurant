from django.db import models
from accounts.models import Account
import uuid



class BookTable(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.ForeignKey(Account , on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    no_of_people = models.IntegerField()
    date_and_time = models.CharField(max_length=100)


    class Meta:
        verbose_name = ("BookTable")
        verbose_name_plural = ("BookTables")

    def __str__(self):
        return str(self.name)