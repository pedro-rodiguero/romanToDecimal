roman_dict ={'I': 1, 'V': 5,
             'X': 10, 'L': 50,
             'C': 100, 'D': 500,
             'M': 1000}

def convert_to_decimal(roman):
    global roman_dict
    roman_back = list(reversed(list(roman)))  
    value = 0
    right_val = roman_dict[roman_back[0]]  
    for numeral in roman_back:
        left_val = roman_dict[numeral]
        if left_val < right_val:
           value -= left_val
        else:
            value += left_val
        right_val = left_val
    return str(value) 

