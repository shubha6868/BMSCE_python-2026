# Definition: A Tuple is ordered, immutable collection of items
# Properties
#Ordered
#Immutable

myTuple = (1,2.5, "BMSCE", "A", 4)
anotherTuple =tuple(range(10))

# access the elements from tuple
print(myTuple)
print(myTuple[0])
print(myTuple[2])
print(myTuple[1:3])
print(myTuple[-1])
print(myTuple[-2])

# Operations on Tuple
# concatenation of 2 tuples using + operator

tuple1 = (1,2,3)
tuple2 =(4,5,6)

resultTuple=tuple1 + tuple2
print(resultTuple)

# Repitations of tuples
originalTuple = (1,2,3)
repeatedTuple = originalTuple*3
print(repeatedTuple)

#membership of an element inside tuple
sameTuple = (1,2,3,4,5,6)
print(20 in sameTuple)
print(3 not in sameTuple)
print(20 not in sameTuple)

# length of a Tuple
#Length = len((4,5,73,1.7,3,6,0))
#print(Length)

# Index
#index = myTuple.index("BMSCE")
#print(index)

#count() counting the number of occurences of an element in a tuple
#count = myTuple.count(2.5)
#print(count)

# Note - There are only 2 inbuilt functions in tuple - index and count
# why? because tuples are immutable, they cannot be modified
# so we have limited options in tuple

# once the tuple is created you cannot change anything in it
# this is tuple
