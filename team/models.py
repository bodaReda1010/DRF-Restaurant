from django.db import models
import uuid


class Chef(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    class Meta:
        verbose_name = ("Chef")
        verbose_name_plural = ("Chefs")

    def __str__(self):
        return self.name