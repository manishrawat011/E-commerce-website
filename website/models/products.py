from django.db import models 
from .categorys import Category

class Product(models.Model):
    name= models.CharField(max_length=30)
    price= models.IntegerField(default=0)
    categorys= models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description= models.CharField(max_length=200,  default='', null=True, blank=True)
    image= models.ImageField(upload_to='upload/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(categorys= category_id)
        else:
            return Product.get_all_products();

        