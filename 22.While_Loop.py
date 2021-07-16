# counter = 0
# while counter <=10:
#     print(counter)
#     counter = counter + 1
# else :
#     print("Loop Terminated")

# Table Print 
from typing import Counter


Table_Number = int(input("Enter a number :"))
Counter = 1
while Counter <=10:
    print(str(Table_Number) + " X " + str(Counter) + " = " + str(Table_Number * Counter))
    Counter += 1
