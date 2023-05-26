def romanize(number):
    """Convert integers between 1 and 3999 to Roman Numerals

    Args:
        number (int): The number to be converted

    Returns:
        str: Roman numeral converted from the input number
    """
    thousands = ["M", "MM", "MMM"]
    hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    units = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    roman_numeral = ""  # Create an empty string
    string_number = str(number)  # Convert the number to string
    if len(string_number) == 4 and string_number[-4] != "0":
        roman_numeral += thousands[int(string_number[-4]) - 1]
    if len(string_number) >= 3 and string_number[-3] != "0":
        roman_numeral += hundreds[int(string_number[-3]) - 1]
    if len(string_number) >= 2 and string_number[-2] != "0":
        roman_numeral += tens[int(string_number[-2]) - 1]
    if len(string_number) >= 1 and string_number[-1] != "0":
        roman_numeral += units[int(string_number[-1]) - 1]
    return roman_numeral


# Get input from the user
print(romanize(input("Enter the number between 1 and 3999 :")))
