# Challenge 3: Roman Number Learning points: Roman Number, Number Conversion,Testing & Debugging
# Ada sebuah roman number berikut MMXXV
# Buatlah sebuah function untuk mengembalikan roman number diatas
# Setelah itu buatlah testing dan debugging dalam proses decodenya.
# Cover semua positive dan negative test case.

def roman_to_integer(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_dict[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

def number_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

s = "MMXXV"
result = roman_to_integer(s)
if result != -1:
    print(f"Roman Number: {s} -> Integer: {result}")
else:
    print("Invalid Roman Number")