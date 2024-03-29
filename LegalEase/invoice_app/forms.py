from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    CURRENCY_CHOICES = [
        ('KES', 'Ksh'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        # Add more currency choices as needed
    ]

    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'placeholder': 'Enter amount'}))
    currency = forms.ChoiceField(label='Currency', choices=CURRENCY_CHOICES)

    class Meta:
        model = Invoice
        fields = ['amount', 'due_date', 'client', 'description', 'currency']

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount
