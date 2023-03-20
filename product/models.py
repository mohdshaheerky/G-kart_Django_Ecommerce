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

variation_category_choices=(
    ('color','color'),
    ('size','size'),
)

class variationManager(models.Manager):
    def colors(self):
        return super(variationManager, self).filter(variation_category='color',is_active=True)
    def sizes(self):
        return super(variationManager, self).filter(variation_category='size',is_active=True)

class variation(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category =models.CharField(max_length=100,choices=variation_category_choices)
    variation_value =models.CharField(max_length=100)
    is_active =models.BooleanField(default=True)
    created_date =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.variation_value
    objects = variationManager()


