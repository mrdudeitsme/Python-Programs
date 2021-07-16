roll_no = int(input("Enter Your roll number :"))
name = input("Enter Your Name :")
gender = input("Enter your gender :")
student_class = int(input("Enter your class :"))
physics = int(input("Enter your physics marks :"))
chemistry = int(input("Enter your chemistry marks :"))
Maths = int(input("Enter your Maths marks :"))
Biology = int(input("Enter your Biology marks :"))
obtain_marks = physics + chemistry + Maths + Biology
percentage = obtain_marks / 400 * 100

print("-----------------Student Marksheet-----------------")
print("Student Roll Number is :"+ str(roll_no))
print("Student Name is :"+ name)
print("Student Gender is :"+ gender)
print("Student class : "+ str(student_class))
# print("Student physics marks :" +str(physics))
# print("Student chemistry marks :" +str(chemistry))
# print("Student Maths marks :" +str(Maths))
# print("Student Biology marks :" +str(Biology))
print("Student total marks is : 400")
print("Student obtain marks is :"+ str(obtain_marks))
print("Student percentage :" +str(percentage))

if percentage >= 80:
    print("A grade")
    print("remark : Excellent")
elif percentage >= 60:
    print("B grade")
    print("remark : Good+")
elif percentage >= 50:
    print("C grade")
    print("remark : Good")
elif percentage >= 40:
    print("D grade")
    print("remark : Poor")
elif percentage >=35:
    print("E grade")
    print("Need to more study")
else:
    print("fail")



