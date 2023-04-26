from django.db import models

# Create your models here.

class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    category = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category'
    
    def __str__(self):
        return self.category

class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=256, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
    price = models.FloatField()
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product'
    
    def __str__(self):
        return self.product_name