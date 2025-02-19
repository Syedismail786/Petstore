from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class contactenquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()

class Product(models.Model):
    CAT = (
        ('1', 'Dog'), ('2', 'Cat'), ('3', 'Parrot'),
        ('4', 'Horse'), ('5', 'rabbit'), ('6', 'Airedale Terrier'),
    )

    name = models.CharField(max_length=50, verbose_name='Product Name')
    price = models.FloatField()
    age = models.IntegerField()
    cat = models.CharField(max_length=50, verbose_name='Category', choices=CAT)
    pdetail = models.CharField(max_length=300, verbose_name='Product Details')
    is_active = models.BooleanField(default=True)
    pimage = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name


class Cart(models.Model):
    objects = None
    uid = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, db_column='uid')
    pid = models.ForeignKey(to='Product', on_delete=models.CASCADE, db_column='pid')
    qty = models.IntegerField(default=1)


class Order(models.Model):
    orderid = models.IntegerField()
    uid = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, db_column='uid')
    pid = models.ForeignKey(to='Product', on_delete=models.CASCADE, db_column='pid')
    qty = models.IntegerField(default=1)
    amt = models.FloatField()


class Orderhistory(models.Model):
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)