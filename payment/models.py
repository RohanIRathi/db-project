from django.db import models
from orders.models import Orders
from cards.models import Cards

# Create your models here.

class Payment(models.Model):
    id = models.AutoField(verbose_name='Payment Id', db_column='id', primary_key=True)
    orderid = models.ForeignKey(Orders, models.DO_NOTHING, db_column='orderid')
    card = models.ForeignKey(Cards, on_delete=models.RESTRICT)

    class Meta:
        managed = True
        db_table = 'payment'
        unique_together = (('orderid', 'card'),)