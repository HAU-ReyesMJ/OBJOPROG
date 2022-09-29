from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "title",
            "description",
            "price",
            "name",
            "location",
            "markAsSold",
        ]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            # 'description':forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Full Name"}
            ),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "markAsSold": forms.CheckboxInput(attrs={"class": "form-check"}),
        }
