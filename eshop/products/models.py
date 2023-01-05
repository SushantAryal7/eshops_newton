from django.db import models
from base.models import BaseModel
# pip install django-autoslug
from autoslug import AutoSlugField

# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='category_name',unique=True, null=True, default=None)
    category_image = models.ImageField(upload_to="categories")

    def __str__(self) -> str:
        return self.slug


class ColorVariant(BaseModel):
    color_name  = models.CharField(max_length=100)
    price       = models.IntegerField(default=0)

    def __str__(self):
        return self.color_name


class SizeVariant(BaseModel):
    size_name  = models.CharField(max_length=100)
    price       = models.IntegerField(default=0)

    def __str__(self):
        return self.size_name



class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='product_name',unique=True, null=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    price = models.IntegerField()
    product_description = models.TextField()
    color_variant = models.ManyToManyField(ColorVariant, blank=True)
    size_variant  = models.ManyToManyField(SizeVariant, blank=True)

    def __str__(self) -> str:
        return self.slug


    def get_product_price_size(self , size):        
        return self.price + SizeVariant.objects.get(size_name = size).price


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")
