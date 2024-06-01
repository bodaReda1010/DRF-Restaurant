from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator , MaxValueValidator
from category.models import Category
from django.core.exceptions import ValidationError
import uuid




class Meal(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    name = models.CharField( max_length=250)
    slug = models.SlugField(unique=True,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Meal")
        verbose_name_plural = ("Meals") 

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Meal,self).save(*args, **kwargs)

    def num_of_rating(self):
        rating = Review.objects.filter(product = self)
        return len(rating)
    
    def avg(self):
        rating = Review.objects.filter(product = self)
        stars = 0
        for x in rating:
            start += x.rating
        if len(rating) > 0:
            return stars / len(rating)
        return 0


    def __str__(self):
        return self.name
    


class Review(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Meal , on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment = models.TextField()

    def clean(self):
        if self.rating < 1:
            raise ValidationError('Rating Min Value Must Be Greater Than 1')
        if self.rating > 5:
            raise ValidationError('Rating Max Value Must Be Smaller Than 5')
        return super(Review , self).clean()

    class Meta:
        unique_together = (('user' , 'product'),)
        index_together = (('user' , 'product'),)

    class Meta:
        verbose_name = ("Review")
        verbose_name_plural = ("Reviews")

    def __str__(self):
        return f'Review Of {self.product}'