from django.db import models
from orders.models import OrderProduct

# Create your models here.

class Refunds(models.Model):
    id = models.AutoField(verbose_name='Refund Id', db_column='id', primary_key=True)
    # orderid = models.ForeignKey(OrderProduct, models.DO_NOTHING, db_column='orderid', primary_key=True)  # The composite primary key (orderid, productid) found, that is not supported. The first column is selected.
    # productid = models.ForeignKey(OrderProduct, models.DO_NOTHING, db_column='productid', to_field='productid', related_name='refunds_productid_set')
    orderid = models.IntegerField(verbose_name='OrderProduct Order', db_column='orderid')
    productid = models.IntegerField(verbose_name='OrderProduct Product', db_column='productid')
    reason = models.CharField(max_length=256, blank=True, null=True)
    refund_date_time = models.DateTimeField()
    orderproduct = models.ForeignKey(OrderProduct, on_delete=models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'refunds'
        unique_together = (('orderid', 'productid'),)