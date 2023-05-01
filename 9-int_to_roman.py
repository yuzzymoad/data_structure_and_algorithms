def int_to_roman(n):
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                      100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                      9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman = ''
    for value, numeral in roman_numerals.items():
        while n >= value:
            roman += numeral
            n -= value
    return roman


if __name__ == "__main__":
    num = 55
    roman_num = int_to_roman(num)
    print(f"The Roman numeral for {num} is {roman_num}")
