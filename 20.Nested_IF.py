# Email Nested IF 
e_mail = input("Enter Your Email ID : ")
if e_mail == "sahil.dudwadkar46@gmail.com" :
    password = input("Enter Your Password :")
    if password == "sahil123" :
        print("Successfull login")
    else:
        print("Invalid Password")
else:
    print("Invalid Email ID")

#
# num = int(input("Enter a number :") )
# if num > 5:
#     if num == 10:
#         print("Number is 10..")
#     else:
#         print("Number is not 10..")
# else:
#     if num == 3:
#         print("NUmber is 3..")
#     else:
#         print("Number is not 3..")