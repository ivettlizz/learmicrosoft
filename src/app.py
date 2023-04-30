# print("Welcome to the greeter prorgam")
# name = input("Enter your name:")
# print("Greeting "+ name)
# print("Calculator program")
# first_number=input("Enter first number:")
# second_number=input("Enter second number:")
# print(int(first_number)+int(second_number))

# parsecs_input=input("Enter thr number of parsecs")
# lightyears = int(parsecs_input) * 3.26
# print(str(parsecs_input) + " parsecs is " + str(lightyears) + " lightyears")
from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)

