from django.db import models
from user.models import User

# Create your models here.

class Tickets(models.Model):
    ticketid = models.AutoField(primary_key=True)
    t_type = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    complete = models.IntegerField(blank=True, null=True)
    issued_by = models.ForeignKey(User, models.DO_NOTHING, db_column='issued_by', blank=True, null=True)
    issued_for = models.ForeignKey(User, models.DO_NOTHING, db_column='issued_for', related_name='tickets_issued_for_set', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tickets'