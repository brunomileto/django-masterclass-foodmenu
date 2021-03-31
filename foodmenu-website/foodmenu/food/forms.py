from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        # Setting the model and fields
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']