from django import forms
from .models import Customer, Investment, Stock, Mutualfund


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = (
            'customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
            'recent_date',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)

class MutualfundForm(forms.ModelForm):
    class Meta:
        model = Mutualfund
        fields = (
            'customer', 'bondtype', 'description', 'acquired_value', 'acquired_date', 'recent_value',
            'recent_date',)

class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Subject=forms.CharField(required=False)
    Message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )