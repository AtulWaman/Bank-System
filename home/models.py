from django.db import models

class Customer(models.Model):
  cx_id=models.IntegerField(primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  mobile_number = models.CharField(max_length=255)
  def __str__(self):
        return self.firstname


class Account(models.Model):
  account_id = models.IntegerField(primary_key= True)
#   amount = models.IntegerField()
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  cx_id = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Transfer_money(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    sender_firstname = models.CharField(max_length=255)
    sender_lastname = models.CharField(max_length=255)
    cx_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)