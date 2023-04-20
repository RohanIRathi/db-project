from django.db import models
from orders.models import Orders
from cards.models import Cards

# Create your models here.

class Payment(models.Model):
    id = models.AutoField(verbose_name='Payment Id', db_column='id', primary_key=True)
    orderid = models.ForeignKey(Orders, models.DO_NOTHING, db_column='orderid')
    # userid = models.ForeignKey(Cards, models.DO_NOTHING, db_column='userid')
    # card_no = models.ForeignKey(Cards, models.DO_NOTHING, db_column='card_no', to_field='card_no', related_name='payment_card_no_set')
    userid = models.IntegerField(verbose_name="User Id")
    card_no = models.BigIntegerField(verbose_name="Card no")
    card = models.ForeignKey(Cards, on_delete=models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'payment'
        unique_together = (('orderid', 'userid', 'card_no'),)