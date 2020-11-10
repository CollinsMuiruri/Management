from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_number = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_billing_address = models.CharField(max_length=200)
    customer_shipping_address = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name
    
    def save_customer(self):
        return self.save()

    def delete_customer(self):
        return self.delete()