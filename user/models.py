from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail

from .managers import CustomUserManager

# Create your models here.

class User(AbstractBaseUser):
    userid = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=30)
    password = models.CharField(max_length=128, blank=True, null=True)
    phone = models.BigIntegerField(unique=True)
    acct_no = models.BigIntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=45, blank=True, null=True)
    swift_code = models.CharField(max_length=11, blank=True, null=True)
    routing_no = models.CharField(max_length=11, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    last_login = None

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'user'
    
    def __str__(self):
        return self.email
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
    
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Address(models.Model):
    id = models.AutoField(verbose_name='Address PK', db_column="id", primary_key=True)
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userid')  # The composite primary key (userid, street, city, state, zip) found, that is not supported. The first column is selected.
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    _zip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'address'
        unique_together = (('userid', 'street', 'city', 'state', '_zip'),)

class Supplier(models.Model):
    userid = models.OneToOneField(User, models.DO_NOTHING, db_column='userid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'supplier'

class Customer(models.Model):
    userid = models.OneToOneField(User, models.DO_NOTHING, db_column='userid', primary_key=True)
    fname = models.CharField(max_length=15, blank=True, null=True)
    lname = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'