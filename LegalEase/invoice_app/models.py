from django.db import models
from case_app.models import Case
from client_app.models import Client  # Import Client model
from django.utils import timezone

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('SENT', 'Sent'),
        ('PAID', 'Paid'),
        ('OVERDUE', 'Overdue'),
    ]

    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=2)  # Use default client with ID 2
    invoice_number = models.CharField(max_length=20, unique=True, default='INV-0002')  # Manually set default value
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_period_start = models.DateField(default=timezone.now)
    billing_period_end = models.DateField(default=timezone.now)
    due_date = models.DateField()
    payment_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='DRAFT')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    adjustment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Invoice #{self.invoice_number} - Amount: {self.amount}"
