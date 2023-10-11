from django.db import models

# Create your models here.
# invoice_app/models.py
from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return self.invoice_no

class InvoiceDetail(models.Model):
    invoice_no = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description
