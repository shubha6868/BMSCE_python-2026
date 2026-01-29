# write a program to create a calculator using functions with menu options
#1. addition # 2. subtraction #3. Multiplication #4. Division ,5 Exit  6 Invalid choice
from random import choice

def addition(a,b):
    sum=a+b
    return sum

def subtraction(a,b):
    sum=a-b
    return sum

def multiplication(a,b):
    sum=a*b
    return sum

def division(a,b):
 sum=a/b
return sum

operation = int(input("enter operation\n1)addition\n2)subtraction\n3)multiplication\n4)division\n5) Exit")):


if 0 < operation < 5:
    a = int(input("enter num 1:"))
    b = int(input("enter num 2:"))
else:
    break

   match operation:
        case 1:
            print(f"{a}+{b}={a+b}")
        case 2:
          print(f"{a}-{b}={a -b}")
        case 3:
        print(f"{a}*{b}={a *b}")
        case 4:
        print(f"{a}/{b}={a /b}")
        case 5:
        print("ok bye")
         break









