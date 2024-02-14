import random
import string

def generate_password(length):
  """Generates a random password of the specified length."""

  lowercase_letters = string.ascii_lowercase
  uppercase_letters = string.ascii_uppercase
  digits = string.digits
  symbols = "".join(["!", "@", "#", "$", "%", "^", "&", "*", "=", "+", ";", ":", "/", "<", ">", "?"])  # Change symbols to string

  all_characters = lowercase_letters + uppercase_letters + digits + symbols

  password = "".join(random.choice(set) for set in [lowercase_letters, uppercase_letters, digits, symbols])

  while len(password) < length:
    password += random.choice(all_characters)

  password_list = list(password) 
  random.shuffle(password_list) 
  password = "".join(password_list)  

  return password

password_length = int(input("Enter the number of characters u want in the password: "))

password = generate_password(password_length)

print("Your generated password is:", password)
