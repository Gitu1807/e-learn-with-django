from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class course(models.Model):
    CAT=((1,'Frontend'),(2,'Backend'),(3,'Database'),(4,'Devops'),(5,'DSA'))
    name=models.CharField(max_length=100 ,verbose_name='Course Name')
    price=models.FloatField()
    time=models.CharField(max_length=50)
    std=models.CharField(max_length=50)
    cat=models.IntegerField(max_length=50, verbose_name='Category' ,choices=CAT)
    cdetail=models.CharField(max_length=300, verbose_name='Course Detail')
    cimage=models.ImageField(upload_to='image')
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
# # Create your models here.
# class Notes(models.Model):
#     name=models.CharField(max_length=100 ,verbose_name='Notes Name')
#     cdata=models.CharField(max_length=500, verbose_name='Notes Data')
#     cimage=models.ImageField(upload_to='image')
#     is_active=models.BooleanField(default=True)

#     def __str__(self):
#         return self.name
    

class Cart(models.Model):
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE, db_column='uid')
    pid=models.ForeignKey('Course',on_delete=models.CASCADE, db_column='pid')
    qty=models.IntegerField(default=1)

class Order(models.Model):
    orderid=models.IntegerField()
    uid=models.ForeignKey('auth.User',on_delete=models.CASCADE, db_column='uid')
    pid=models.ForeignKey('Course',on_delete=models.CASCADE, db_column='pid')
    qty=models.IntegerField(default=1)
    amount=models.FloatField()
