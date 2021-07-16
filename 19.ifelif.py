# Stu_Percentage = float(input("Enter Your Percentage :"))
# if Stu_Percentage >= 80:
#     print("A1 Grade")
# elif Stu_Percentage >=70:
#     print("A Grade")
# elif Stu_Percentage >=60:
#     print("B Grade")
# elif Stu_Percentage >=50:
#     print("C Grade")
# elif Stu_Percentage >=40:
#     print("D Grade")
# elif Stu_Percentage >=30:
#     print("E Grade")
# else:
#     print("Fail")

Age = int(input("Enter your age :"))
if 0<Age<=3:
    print("Ticket price for 1 to 3 year people for free ")
elif 4<Age<=10:
    print("Ticket price for 4 to 10 year people for 150 rs..")
elif 11<Age<=60:
    print("Ticket price for 11 to 60 year people for 250 rs..")
elif 60<Age<=100:
    print("Ticket price for above 60 year people for 200 rs..")
else:
    print("Wrong Age")