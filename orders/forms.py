from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Order,OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name","last_name","phone_number","address","order_notes"]
        widgets = {
            'address' : forms.Textarea (attrs={'rows': 3}),
            'order_notes' : forms.Textarea (attrs={
                'rows':5,
                'placeholder' : _('if you have any notes please enter here')})
                  }
        error_messages = {
        'first_name': {
            'max_length': _("This writer's name is too long."),
        },

    }