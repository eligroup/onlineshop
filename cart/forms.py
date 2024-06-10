from django import forms
from persian_translation.templatetags.persian_translation_tags import arabic_numerals


class AddProductToCart(forms.Form):
    #quantity_choices = [(i,arabic_numerals(i)) for i in range(1,11)] maybe for changing eng num to farsi num it works
    quantity_choices = [(i,str(i)) for i in range(1,30)] #FOR choices we need tuole [(1,"1"),...
    quantity = forms.TypedChoiceField(choices= quantity_choices , coerce=int) #coerce change to int

    inplace = forms.BooleanField(required=False , widget=forms.HiddenInput) # as we need true or false ,we set booleanfield .
    # if it is false user is in product page and quantity should be added to cart. if it is true user is im cart page and quantity shpuld be updated.
    # as we dont want this field displaye for the uaser we hide it. widget is field for html

