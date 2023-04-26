from .models import User, Customer, Supplier

def userIsCustomer(user):
    try:
        Customer.objects.get(userid=User.objects.get(email=user))
        return True
    except:
        return False

def userIsSupplier(user):
    try:
        Supplier.objects.get(userid=User.objects.get(email=user))
        return True
    except:
        return False