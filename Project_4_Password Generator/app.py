import random
import string

length = int(input("Enter The Length Of Password : "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all = lower + upper + digits + symbols

temp = random.sample(all,length)
password = "".join(temp)
print(password)