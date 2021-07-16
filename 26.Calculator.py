# Funcation Declaration 

def Addition(num1, num2):
    if num1 != "" and num2 != "":
        result = int(num1) + int(num2)
        print("Addition result is : " +str(result))
def Subtraction(num1, num2):
    if num1 != "" and num2 != "":
        result = int(num1) - int(num2)
        print("Subtraction result is : " +str(result))
def Multiplication(num1, num2):
    if num1 != "" and num2 != "":
        result = int(num1) * int(num2)
        print("Multiplication result is : " +str(result))
def Division(num1, num2):
    if num1 != "" and num2 != "":
        result = int(num1) / int(num2)
        print("Division result is : " +str(result))

a = True
while a == True:

# User Input 

    f_num = input("Enter First Number :")
    s_num = input("Enter Second Number :")
    operator = input("Enter a operator - +,-,*,/ :")
    
    if operator == "+":
        Addition(f_num,s_num)
    elif operator == "-":
        Subtraction(f_num,s_num)
    elif operator == "*":
        Multiplication(f_num,s_num)
    elif operator == "/":
        Division(f_num,s_num)
    else:
        print("Invalid operator....")
    Answer = input("Do you wants to repeat your program : ").lower()
    if Answer == "yes":
        continue
    else:
        exit()
