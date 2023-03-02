from django.db import models
from home.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name     =models.CharField(max_length=200,unique=True)
    slug             =models.SlugField(max_length=200,unique=True)
    pro_description  =models.TextField()
    pro_image        =models.ImageField(upload_to='photos/product')
    category         =models.ForeignKey(Category,on_delete=models.CASCADE)
    price            =models.IntegerField()
    stock            =models.IntegerField()
    is_available     =models.BooleanField(default=True)
    created_date     =models.DateTimeField(auto_now_add=True)
    modified_date    =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])



