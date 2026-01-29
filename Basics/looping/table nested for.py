#write a program to print tables from 1 to 100 using nested for loop
for i in range(1,11):
    for j in range(1,11):
        print(  f"{j} x {i}  =  {i*j}",   end   =  "         ")
    print()