# dEFINITION: set is unordered collection of unique elements
# unordered  order of hashing is considered
#Mutable
#does not allow duplicates

mySet = {1,2,3,4,4}
print(mySet)

# Adding elements
mySet.add(5)
print(mySet)

# remove elements
mySet.remove(2) # remove function will give error
print(mySet)
mySet.discard(2)  #discard function not give any error
print(mySet)
mySet.pop()
print(mySet)
mySet.pop()
print(mySet)

setA={1,2,3}
setB={3,4,5}

union = setA | setB # {1,2,3,4,5}
print(union)
intersection = setA & setB # {3}
print(intersection)
difference = setA - setB # { 1,2}
print(difference)
difference = setB - setA
print(difference)