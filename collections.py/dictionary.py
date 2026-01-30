# Definition:  is mutable, unordered collection of keyvalue pairs

# Properties

# Unordered (Python 3.7+ maintains the order of insertion)
# Mutable
# keys should be unique

# Basic operations

dic1 = {'name ':'Monish' ,'age' : 11, 'city': 'Bangalore'}
dic2 =  {'name ':'shubha' ,'age' : 15, 'city': 'Bangalore'}
dic3 = {'names':['Monish', 'shubha'],'ages' : [11,15], 'cities': ['Bangalore', 'Bangalore']}
print(dic1)
print(dic1{'name'})


# 1) key
myDict={'name': 'shubha','age':15,'city':'Bangalore'}
key=myDict.keys()
print(key)
print(type(key))
for i in key:
    print(i) # iterate overs keys and printing them seperately
print(list(key))

# 2) values
value=myDict.values()
print(value)
print(type(value))
for i in value:
    print(i)
print(list(value))

# 3)items
item=myDict.items()
print(item)
print(type(item))
for i in item:
    print(i)
print(list(item))

#get()
print(myDict.get('name'))
print(myDict.get('city'))
print(myDict.get('age'))

# update
myDict.update({'city': 'Pune'})
print(myDict)
