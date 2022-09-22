from django import forms
from .models import Contacts

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = [
            'lastName',
            'firstName',
        ]

        # widgets = {
        #     'title':forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'description':forms.TextInput(attrs={'class': 'form-control'}),
        #     'description':forms.Textarea(attrs={'class': 'form-control'}),
        #     'price':forms.NumberInput(attrs={'class': 'form-control'}),
        #     'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
        #     'location':forms.TextInput(attrs={'class': 'form-control'}),
        #     'markAsSold':forms.CheckboxInput(attrs={'class': 'form-check'}),
        # }
        