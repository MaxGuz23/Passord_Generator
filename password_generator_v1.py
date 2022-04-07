# Importing random library
import random
# Defining which characters we'll use for the password, not ñ included
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@^!€#$%&"
# Begining an infinite loop, to stop input exit()
while True:
    # Getting the user desired password length
    password_len = int(input("Insert password length: "))
    # Getting the user desired count of passwords
    password_count = int(input("Number of passwords to create: "))
    
    for i in range(password_count): # From 0 to the amount of desired passwords
        # Initialize an empty string
        password = "" 
        for j in range(password_len):# From 0 to desired password length
            # Pick random characters from chars
            password_char = random.choice(chars)
            # Concatenate each pick into the password
            password += password_char
        # Printing the random generated password    
        print(f'This is your pasword: {password}')    




