## from collections import OrderedDict

_roman_digits = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
    }

def generate(number):
    if number < 1:
        raise Exception('Number cannot be less than one')
    if number in _roman_digits.keys():
        return _roman_digits[number]
    else:
        for key in list(_roman_digits.keys())[::-1]:
            if int(number / key) > 0:
                retval = int(number / key) * _roman_digits[key]
                if number % key != 0:
                    retval = retval + generate(number % key)
                return retval
