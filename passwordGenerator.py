import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%^&!*/\?"

Use_for = lower_case + upper_case + numbers + symbols
length_for_pass = 15

password ="".join(random.sample(Use_for, length_for_pass))

print(password)