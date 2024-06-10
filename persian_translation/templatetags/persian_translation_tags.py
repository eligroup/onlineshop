from django import template
from babel.numbers import format_decimal

register = template.Library()

def convert_to_arabic_numerals(number):
    arabic_numerals = '٠١٢٣٤٥٦٧٨٩'
    return ''.join(arabic_numerals[int(digit)] if digit.isdigit() else digit for digit in str(number))

@register.filter
def arabic_numerals(value):
    try:
        return convert_to_arabic_numerals(value)
    except (ValueError, TypeError):
        return value









# @register.filter
# def arabic_numerals(value):
#     try:
#         return format_decimal(value, locale='fa')
#     except (ValueError, TypeError):
#         return value


@register.filter
def translate_numbers_en_to_fa(value):
    en_num = "0123456789"
    fa_num = "٠١٢٣٤٥٦٧٨٩"
    persian_number = str(value).maketrans(en_num , fa_num)
    return str(value).translate(persian_number)


#


# txt = "Hello Sam!"
# mytable = str.maketrans("S", "P")
# print(txt.translate(mytable))

# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = str.maketrans(x, y, z)
# print(txt.translate(mytable))

#--------------
# @register.filter(name='persian_int')
# def persian_int(english_int):
#     devanagari_nums = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
#     number = str(english_int)
#     return ''.join(devanagari_nums[int(digit)] for digit in number)