# Print string last character with function
# def last_char(name):
#     return name[-2]

# print(last_char("sahil"))
# ------------------------------------------------------------------------

# Even or odd

# def odd_even(num):
#     if num%2==0:
#         return "even"
#     return "odd"

# num = int(input("Enter a number :"))
# print(odd_even(num))

# ----------------------------------------------------------------------------------

# Even or odd & return Boolean Value 
# def ifs_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False

# num = int(input("Enter a number for entered number is even or not :"))
# print(ifs_even(num))

# -----------------------------------------------------------------------------------
# Grater Num function 
# def Greater_num(a,b):
#     if a>b:
#         return a
#     return b

# num1 = int(input("Enter num1 :"))
# num2 = int(input("Enter num2 :"))
# print(Greater_num(num1,num2))

# given string is palindrom or not 
def is_palindrom(name):
    reverse_name = name[::-1]
    if name == reverse_name:
        return "Name is palindrome"
    return "Name is not palindrome"

name = input("Enter a name for check name is palindrome or not :")
print(is_palindrom(name))