# def fibo(num):
#     a=0
#     b=1
#     if num == 1:
#         print(a)
#     elif num == 2:
#         print(b)
#     else:
#         # print(a,b , end = " ")
#         for i in range(num-2):
#             c=a+b
#             a=b
#             b=c
#             print(b,end = " ")
# fibo(10)
# --------------------------------------------------------------------------------------


# fibonacci series with user input 

def fibo(num):
    a=0
    b=1
    if num == 1:
        print(a)
    elif num == 2:
        print(b)
    else:
        for i in range(num):
            c = a+b
            a = b
            b = c
            print(b,end=" ")

num = int(input("Enter a number for fibonacci series"))
print(fibo(num))