#Random Password Generator#

import random
from time import perf_counter

print("Welcome to random Password generator")
randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&'()*+,-./:;<=>?@[]^_`{|}~0123456789"
numofpw = int(input("Please Enter the number of passwords to be generated :"))
pwlength =int(input("Please Enter the length of the password nedded : "))

print("\nHere are your random passwords : ")

for i in range(numofpw):
    pwd=""
    for j in range(pwlength):
        pwd=pwd + random.choice(randomchars)
    print(pwd)

print("Welcome Come again...")



