from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    dishName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dishes/')
    price = models.DecimalField(max_digits=8,decimal_places=2)
    available = models.BooleanField(default=True)

def __str__(self):
    return self.dishName

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=100)
    order_dishes = models.ManyToManyField(Dish)
    status = models.CharField(max_length=70, default='received')
    
    # Add the delivery_address field
    delivery_address = models.CharField(max_length=255, default='')  # Adjust this field type as needed
    contact_number = models.CharField(max_length=20,default='')  # Add the contact_number field
    staff_member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"Order #{self.id}"