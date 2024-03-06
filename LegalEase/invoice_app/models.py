from django.db import models
from decimal import Decimal

# Create your models here.

class BillingMethod(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    billing_method = models.ForeignKey(BillingMethod, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_status = models.CharField(max_length=20)

    def __str__(self):
        return f"Invoice #{self.invoice_number}"

class CourtAppearanceBilling(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    court_case = models.ForeignKey('Case', on_delete=models.CASCADE)
    description = models.TextField()
    court_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.court_case}: Court Appearance Billing"