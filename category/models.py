from django.db import models
from django.utils.text import slugify
import uuid



# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField( max_length=250)
    slug = models.SlugField(unique=True,blank=True,null=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.name