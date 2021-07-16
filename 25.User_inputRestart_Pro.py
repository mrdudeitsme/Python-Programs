a = True 
while a == True:
    num1 = int(input("Enter 1st Number :"))
    num2 = int(input("Enter 2nd Number :"))
    result = num1 + num2
    print("Addition of two number is : " + str(result))
    Answer = input("Do you wants to repeat your program yes / no :").lower()
    if Answer == "yes":
        continue
    else:
        exit()