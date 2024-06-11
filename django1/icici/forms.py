from django import forms
from icici.models import Accounts
class inputform(forms.ModelForm):
    class Meta:
        model=Accounts
        fields=['firstname','lastname','aadhaar','phone']