from django.db import models

# Create your models here.
class producthunt(models.Model):
    idtest=models.IntegerField()
    testcol=models.CharField(max_length=3)
    testcol1=models.CharField(max_length=3)
class productdetails(models.Model):
    product_id=models.IntegerField()
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to='pics')
    desc=models.CharField(max_length=100)
    price=models.IntegerField()