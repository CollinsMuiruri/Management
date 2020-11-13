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

    # @classmethod()
    # def get_customers(cls, customer_name):
    #     customer = cls.object.filter(customer__)

class Product(models.Model):
    product_name = models.CharField(max_length=10)

    def __str__(self):
        return self.product_name

    def save_product(self):
        return self.save

    def delete_product(self):
        return self.delete

class Order(models.Model):
    order_number = models.CharField(max_length=5)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.order_number

    def save_order(self):
        return self.save

    def delete_order(self):
        return self.delete

