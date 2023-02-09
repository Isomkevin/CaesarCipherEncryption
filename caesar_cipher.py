"""
For More Information about Caesars Cipher visit 
https://en.wikipedia.org/wiki/Caesar_cipher
""" 

cipherText: str = 'Hello, World'
shift: int = 7
FIRST_CHAR_CODE: int = ord('A')
LAST_CHAR_CODE: int = ord('Z')
CHAR_RANGE: int = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def encrypt(text: str = cipherText, shiftNumber: int = shift) -> str:
  # Result Placeholder
  result = ''
  
  # loop thru each letter in the plain text
  for char in text.upper():
    if char.isalpha():
      # Convert Character to the ASCII code.
      char_code = ord(char)
      new_char_code = char_code + shiftNumber
      
      if new_char_code > LAST_CHAR_CODE:
        new_char_code -= CHAR_RANGE

      if new_char_code < FIRST_CHAR_CODE:
        new_char_code += CHAR_RANGE
      
      new_char = chr(new_char_code)
    
      result += new_char
      
      
    else:
      result += char
  print(f'\nEncrypted Text: \n{result}', end='\n\n')
  print(f'The Cipher Shift Number is {shiftNumber}')
  return result


user_message = input("Message to Encrypt\Decrypt:\n")
user_shift_key = int(input("\nCipher Shift Key: "))

encrypt(user_message, user_shift_key)