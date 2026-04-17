# *args   used to pass arguements of variable length
def mult(*args):
    prod = 1

    for i in args:
        prod = prod*i
    return prod
print(mult(2,3,4,4))

# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

def display(**kwargs):

  for (key,value) in kwargs.items():
    print(key,'->',value)
display(india= 'DELHI', pakistan='ISLAMABAD')

#nested function
def f():
    def x(a, b):
        return a+b
    return x
    
val = f()(3,4)
print(val)

#function as an arguement
def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))



# Lambda Function
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.



# Diff between lambda vs Normal Function
# No name
# lambda has no return value(infact,returns a function)
# lambda is written in 1 line


# Then why use lambda functions?
# They are used with HOF

a = lambda s:'a' in s
print(a('hello'))


# odd or even
a = lambda x:'even' if x%2 == 0 else 'odd'
a(6)






# Example
#HIGHER ORDER FN
def square(x):
  return x**2

def cube(x):
  return x**3

# HOF
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

transform(lambda x:x**3,L)



#MAP - LAMBDA FN AND LIST REQUIRED IN ARGUEMENT

# square the items of a list
print(list(map(lambda x:x**2,[1,2,3,4,5])))


# fetch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

a=list(map(lambda users:users['gender'],users))
print(a)


#FILTER  

# numbers greater than 5
L = [3,4,5,6,7]

a=list(filter(lambda x:x>5,L))
print(a)


#REDUCE 

# sum of all item
import functools

a=functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
print(a)