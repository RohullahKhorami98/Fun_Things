import string
import random

class getPassword:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
    def get_upperCase(self):
        return string.ascii_uppercase
    def get_lowerCase(self):
        return string.ascii_lowercase
    def get_numbers(self):
        return string.digits
    def get_symbols(self):
        return string.punctuation



def generatePassword(min_length, max_length):
    password = getPassword(min_length, max_length)
    upperCase = password.get_upperCase()
    lowerCase = password.get_lowerCase()
    numbers = password.get_numbers()
    symbols = password.get_symbols()
    genpassword = upperCase + lowerCase + numbers + symbols
    return genpassword

if __name__ == '__main__':
    max_length = int(input("Enter the maximum length of the password: "))
    min_length = int(input("Enter the minimum length of the password: "))
    try:
        if min_length > max_length:
            raise ValueError
        else:
            password = random.randint(min_length, max_length)
            charachterList = generatePassword(min_length, max_length)
            temp = random.sample(charachterList, password)
            print("".join(str(x) for x in temp))     
    except ValueError:
        print("The minimum length must be less than or equal to the maximum length.")
   


