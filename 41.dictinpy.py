# Declaration of dictionary in python  - String data type

# dict1 = {"A":"Sahil","B":"Shripad","C":"Dudwadkar"}
# print(dict1["A"])

# Declaration of dictionary in python  - Integer data type
# dict1 = {1:"Sahil",2:"Shripad",3:"Dudwadkar"}
# print(dict1[1])

# update dictionary key value
# dict2 = {"Name":"Sahil","Age":"23","Roll no":"IT7008"}
# print(dict2)
# dict2 ["Name"] = "Sidd"
# print(dict2)

# Adding key & its value in dictionary 
# dict2 = {"Name":"Sahil","Age":"23","Roll no":"IT7008"}
# dict2 ["Surname"] = "Dudwadkar"
# print(dict2)


# Nested Dictionary 
# nested_dict = {"Name":{"First_name":"Sahil","Middle_name":"Shripad","Last_name":"Dudwadkar"}}
# print(nested_dict["Name"]["First_name"])

# Dictionary conatain list & vice versa 
# dict2 = {10:["Sahil","Sidd","Mangesh"],12:["Sahil","Sidd","Mangesh"]}
# print(dict2)
# print(dict2[10][0])

# Dictionary inside list 
list1 = ["Name",{"Fname":"sahil","Lname":"Dudwadkar"},"Roll_No",{"Roll":7008},"S_Age",{"Age":23}]
print(list1[0])
print(list1[1]["Fname"])
print(list1[1]["Lname"])
print(list1[3]["Roll"])
print(list1[5]["Age"])