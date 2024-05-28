from django import forms


class AddProductToCart(forms.Form):
    quantity_choices = [(i,str(i)) for i in range(1,30)] #FOR choices we need tuole [(1,"1"),...
    quantity = forms.TypedChoiceField(choices= quantity_choices , coerce=int) #coerce change to int