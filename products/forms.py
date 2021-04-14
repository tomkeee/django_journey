from django import forms
from .models import Product
class RawProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["title","description","price"]
    # title = forms.CharField(label="Your Title")
    # description = forms.CharField(required=False)
    # price=forms.DecimalField()
