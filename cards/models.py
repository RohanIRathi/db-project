from django.db import models
from user.models import Customer

# Create your models here.

class Cards(models.Model):
    id = models.AutoField(verbose_name='Card Id', db_column='id', primary_key=True)
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='userid')
    card_no = models.BigIntegerField()
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cards'
        unique_together = (('userid', 'card_no'),)