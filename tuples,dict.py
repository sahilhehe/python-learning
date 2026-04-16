#TUPLES


# Tuples

# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

# Characterstics

# - Ordered
# - Unchangeble
# - Allows duplicate

# empty
t1 = ()
print(t1)
# create a tuple with a single item
t2 = ('hello',)
print(t2)
print(type(t2))
# homo
t3 = (1,2,3,4)
print(t3)
# hetro
t4 = (1,2.5,True,[1,2,3])
print(t4)
# tuple
t5 = (1,2,3,(4,5))
print(t5)
# using type conversion
t6 = tuple('hello')
print(t6)

#INDEXING 
print(t3)
print(t3[0])
print(t3[-1])


# EVERYTHING SAME AS LISTS

# zipping tuples
a = (1,2,3,4)
b = (5,6,7,8)

# list(zip(a,b)) 
print([i+j for i,j in zip(a,b)])



# SETS
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).

# However, a set itself is mutable. We can add or remove items from it.

# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# Characterstics:

# Unordered
# Mutable
# No Duplicates
# Can't contain mutable data types


# empty
s = set()
print(s)
print(type(s))
# 1D and 2D
s1 = {1,2,3}
print(s1)
#s2 = {1,2,3,{4,5}}
#print(s2)
# homo and hetro
s3 = {1,'hello',4.5,(1,2,3)}
print(s3)
# using type conversion

s4 = set([1,2,3])
print(s4)
# duplicates not allowed
s5 = {1,1,2,2,3,3}
print(s5)
# set can't have mutable items
#s6 = {1,2,[3,4]}#NOT POSSIBLE

#ACCESSING IS NOT POSSIBE IN 


S = {1,2,3,4}
# add
S.add(5)
print(S)
# update
S.update([5,6,7])
print(S)


#del
#discard
#remove 
#pop
#clear



s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1|s2)#union
print(s1&s2)#intersection
print(s1 ^ s2)#symmetric differance

# len() sum() min() max() - usual functions


# union/update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# s1 | s2
s1.union(s2)

s1.update(s2)
print(s1)
print(s2)


# intersection/intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.intersection(s2)

s1.intersection_update(s2)
print(s1)
print(s2)




# Dictionary
# Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# Characterstics:

# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items

# empty dictionary
d = {}
d
# 1D dictionary
d1 = { 'name' : 'nitish' ,'gender' : 'male' }
d1
# with mixed keys
d2 = {(1,2,3):1,'hello':'world'}
d2
# 2D dictionary -> JSON
s = {
    'name':'nitish',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
print(s)
# using sequence and dict function
d4 = dict([('name','nitish'),('age',32),(3,3)])
print(d4)
# duplicate keys
d5 = {'name':'sahil','name':'rahul'}
print(d5)

d6 = {'name':'nitish',(1,2,3):2}
print(d6)

# Accessing items


my_dict = {'name': 'Jack', 'age': 26}
# []
print(my_dict['age'])
# get
print(my_dict.get('age'))

#ADD KEY VALUE PAIR
d4['gender'] = 'male'
print(d4)
d4['weight'] = 72
print(d4)


#deletion

d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
# pop
#d.pop(3)
#print(d)
# popitem
#d.popitem()
# d.popitem()
# print(d)
# del
#del d['name']
#print(d)
# clear
# d.clear()
# print(d)



d = {'name':'nitish','gender':'male','age':33}

for i in d:
  print(i,d[i])



#LIST COMPREHENSION


# print 1st 10 numbers and their squares
{i:i**2 for i in range(1,11)}

distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print(distances.items())

# using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print({key:value*0.62 for (key,value) in distances.items()})

# using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

print({i:j for (i,j) in zip(days,temp_C)})

# using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}

print({key:value for (key,value) in products.items() if value>0})

# Nested Comprehension
# print tables of number from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})

