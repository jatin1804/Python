# mini project of generating password randomly

import random
import string
pass_length =8

charValues =string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(pass_length):
    password += random.choice(charValues)
print(password)