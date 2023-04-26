from django.db import models
from user.models import Customer
from product.models import Product

# Create your models here.

class Rating(models.Model):
    id = models.AutoField(verbose_name='Rating Id', db_column='id', primary_key=True)
    userid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='userid')
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productid')
    stars = models.IntegerField()
    feedback = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'rating'
        unique_together = (('userid', 'productid'),)