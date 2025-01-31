#password generator
import random
print("Enter the length of the password")
length = int(input())
password = ''
str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
for i in range(length):
    password += random.choice(str)
print(password)

