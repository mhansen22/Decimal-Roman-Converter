def roman_to_dec(number):
    numeral_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    
    roman_numerals = {"I", "V", "X", "L", "C", "D", "M"}
    # checks if all characters are roman numerals (from set)
    if all (char in roman_numerals for char in number):
      prev_val = 0
      digit = 0

      # reversing the number makes it easier to handle the values that are subtracted
      for char in reversed(number):
        # value is set to the character's (char) digit value from map (numeral_map)
        value = numeral_map[char]

        # enter if value is less than the previous value
        if value < prev_val:
          # catches case 4. (from instructions) or when preceding value cannot be V or L or D
          if ((value * 10) < prev_val) or ((char == "V") or (char == "L") or (char == "D")):
            return "Invalid Roman numeral, incorrect precedence."
          digit -= value
        else:
          digit += value
        prev_val = value
      return digit
    else:
      return "Enter a valid roman numeral!"
    

def dec_to_roman(decimal):
      # list of tuples of decimals to roman numerals
      # includes cases like CM, CD, etc for efficiency, thus only need one for and while loop below
      numeral_list = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),(100, "C"), (90, "XC"), (50, "L"), (40, "XL"),(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

      # check if input is a positive integer
      if isinstance(decimal, int) and decimal > 0:
        roman_numeral = ""

        for digit, numeral in numeral_list:
          while decimal >= digit:
            decimal -= digit
            roman_numeral += numeral
        return roman_numeral

      else:
        return "Enter a valid decimal number!"
      


# Makes code interactive with user choice
if __name__ == "__main__":
    choice = input("Choose a conversion: 1 for Roman to Decimal, 2 for Decimal to Roman: ")
    if choice == '1':
        roman_num = input("Enter Roman numeral: ")
        print(roman_to_dec(roman_num))
    elif choice == '2':
        decimal_num = input("Enter Decimal number: ")
        print(dec_to_roman(decimal_num))
    else:
        print("Invalid choice!!")
