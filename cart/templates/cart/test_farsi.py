
import babel
from babel.numbers import format_decimal

# Check if the locale data is available
if 'fa' in babel.localedata.locale_identifiers():
    print("Arabic locale data is available")
else:
    print("Arabic locale data is NOT available")

# Try formatting a number
print(format_decimal(1, locale='ar'))  # Should print ١

def convert_to_arabic_numerals(number):
    arabic_numerals = '٠١٢٣٤٥٦٧٨٩'
    return ''.join(arabic_numerals[int(digit)] if digit.isdigit() else digit for digit in str(number))

print(convert_to_arabic_numerals(124))  # Should print ١
# number=12345
# arabic_numerals = '٠١٢٣٤٥٦٧٨٩'
#
# for digit in str(number): #1,2,3,4,5
#     if digit.isdigit():
#         print(','.join(arabic_numerals[int(4)]))#4
# print(','.join(arabic_numerals[int(0)]))

# quantity_choices = [(i,str(i)) for i in range(1,30)] #FOR choices we need tuole [(1,"1"),...
#     quantity = forms.TypedChoiceField(choices= quantity_choices , coerce=int) #coerce change to int
#
#     inplace = forms.BooleanField(required=False , widget=forms.HiddenInput) # as we need true or false ,we set booleanfield .
#     # if it is false user is in product page and quantity should be added to cart. if it is true user is im cart page and quantity shpuld be updated.
#     # as we dont want this field displaye for the uaser we hide it. widget is field for html

print([(i, str(i) ) for i in range(1,5)])
