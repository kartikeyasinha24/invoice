from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class invoice(models.Model):
	Date = models.DateTimeField(auto_now_add=True, blank=True)
	inv_number=models.IntegerField(blank=False)
	name=models.CharField(max_length=50)
    

class invoicedetail(models.Model):
	inv=models.ForeignKey(invoice, on_delete=models.CASCADE,related_name='invoice_details',null=True,blank=True)
	description=models.TextField()
	quantity=models.IntegerField()
	unitprice=models.DecimalField(decimal_places=1,max_digits=10,default=10)
	





