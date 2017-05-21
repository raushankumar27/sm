from django.db import models

# Create your models here.
class products(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=200)
    price=models.IntegerField()

class order(models.Model):
    orderno=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(products)
    #and some more

class Addons(models.Model):
    Product_name=models.CharField(max_length=200)
    Main_product=models.ForeignKey(products)
