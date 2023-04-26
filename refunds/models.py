from django.db import models
from orders.models import OrderProduct

# Create your models here.

class Refunds(models.Model):
    id = models.AutoField(verbose_name='Refund Id', db_column='id', primary_key=True)
    reason = models.CharField(max_length=256, blank=True, null=True)
    refund_date_time = models.DateTimeField()
    orderproduct = models.OneToOneField(OrderProduct, on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'refunds'
        unique_together = ()