name=input("enter your name:")
birthyear=int(input ("enter your  birth year:"))
print(type(birthyear))
currentyear=int(input("enter the current year:"))
print(type(currentyear))
age=currentyear-birthyear
print(" your age is " + str(age))
print(name + "your age is "+ str(age))
print(f"{name} your age is {age}")
#Formatted Strings way
print("{} your age is{}".format(name,age))