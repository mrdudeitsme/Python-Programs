name,char =input("Enter your name and character for count :").split(",")
print(f"Your name is :{len(name)}")
print(f"the character count is :{name.lower().count(char.lower())}")