from django.db import models
from user.models import Supplier, Customer
from product.models import Product

# Create your models here.

class Orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    t_qty = models.IntegerField(blank=True, null=True)
    t_amt = models.FloatField(blank=True, null=True)
    order_date_time = models.DateTimeField()
    supplied_by = models.ForeignKey(Supplier, models.DO_NOTHING, db_column='supplied_by', blank=True, null=True)
    placed_by = models.ForeignKey(Customer, models.DO_NOTHING, db_column='placed_by', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orders'

class OrderProduct(models.Model):
    id = models.AutoField(verbose_name='Order_Product_Id', db_column="id", primary_key=True)
    orderid = models.ForeignKey(Orders, models.DO_NOTHING, db_column='orderid')
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productid')
    discount = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'order_product'
        unique_together = (('orderid', 'productid'),)