from django.db import models

class ModelHarvest(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    password = models.CharField(max_length=128)
    confirm = models.CharField(max_length=128)


class Add_Products(models.Model):
    product_name = models.CharField(max_length=20)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/',null=True)
    farmer_name = models.CharField(max_length=20)


class Add_Farmers(models.Model):
    farmer_name = models.CharField(max_length=20)
    farmer_address = models.TextField()
    farmer_contact = models.IntegerField()
    farmer_product = models.CharField(max_length=20)
    harvest_date = models.DateTimeField(auto_created=True)
    product_price = models.IntegerField()




