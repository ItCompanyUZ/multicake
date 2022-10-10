from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['date', 'cake', 'number', 'how_many_kg', 'filling', 'writing', 'type_of_delivery']

