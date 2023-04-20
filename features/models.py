from django.db import models
from user.models import Customer
from product.models import Product

# Create your models here.

class Cart(models.Model):
    id = models.AutoField(verbose_name='Cart Id', db_column='id', primary_key=True)
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='userid')
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productid')

    class Meta:
        managed = False
        db_table = 'cart'
        unique_together = (('userid', 'productid'),)

class Bookmark(models.Model):
    id = models.AutoField(verbose_name='Cart Id', db_column='id', primary_key=True)
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='userid')
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productid')

    class Meta:
        managed = False
        db_table = 'bookmark'
        unique_together = (('userid', 'productid'),)