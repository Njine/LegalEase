from django.db import models
from case_app.models import Case

class Invoice(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    payment_status = models.CharField(max_length=50, choices=[('paid', 'Paid'), ('pending', 'Pending')])

    def __str__(self):
        return f"Invoice for {self.case} - Amount: {self.amount}"
