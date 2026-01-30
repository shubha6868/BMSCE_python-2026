# Definition - A list of  a ordered , mutable collection of items
 # properties
 #ordered
 #Mutable
 # Allows Duplicates

myList  =  [1,2,3,4,5]       # syntax using [ ]
anotherList   =  list(range(2,101,2))
#operations on List
# 1) Access elements from myList
print (f"on 3rd index we have {myList[3]}")
print (f"on 0th index we have {myList[0]}")
print(myList[2:4])  #[3,4]
print(f"another list is {anotherList}")
print(anotherList[10:25])


#2) Modifying the elements
# Because lists are mutable we can modify lists
myList[3] = 400
# 2nd way
for i in myList:
    print(i, end="")
print()

#4) Adding an elements to a list
# append()  it will add element at the last of list
myList.append(6)
myList.append(7)
print(myList)
for i in range(8,11):
    myList.append(i)
    print(myList)

# insert() it will insert the element at a particular position
myList.insert(6 ,  5000)
print(myList)
myList.insert(3, "BMSCE")
print(myList)

# removing the element from list
myList.remove(5000)
print(myList)
myList.pop() # remove the last index
print(myList)
del myList[3]
print(myList)

# 6) other functions
print(f"Length of myList is{len(myList)}")
myList.sort()
myList.sort(reverse=True)
print(myList)


