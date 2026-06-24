### Some Theory

##### Types of data used for I/O:
# - Text - '12345' as a sequence of unicode chars
# - Binary - 12345 as a sequence of bytes of its binary equivalent

# ##### Hence there are 2 file types to deal with
# - Text files - All program files are text files
# - Binary Files - Images,music,video,exe files

#file is not present 
f = open('filehandling/sample.txt','w')
f.write("HELLO")
f.close()

#if we wanna append to existing text

f = open ('filehandling/sample.txt','a')
f.write("\nHELLO 2")
f.close()

l= ["hello\n","how are you\n", "how was your day"]
f = open('filehandling/sample.txt','w')
f.writelines(l) #adds multiple lines at once

#read operation

f = open('filehandling/sample.txt','r')
s= f.read()
print(s)
f.close()

#readline
f = open('filehandling/sample.txt','r')
s= f.readline()
a= f.readline()
print(s,end='')
print(a,end='')
f.close()

#reading multiple lines using readline()
f= open('filehandling/sample.txt','r')
while True:
    data = f.readline()
    if(data)=='':
        break
    else:
        print(data,end='')

#with keyword is an alternative of f.close()

with open('filehandling/sample2.txt','w') as f:
    f.write("FIZU BHAI AAGE BOL SKTA HAI KYA")


#seek and tell function

#seek - where u want to go
#tell - tells u where u currently at

with open('filehandling/sample2.txt','w') as f:
    f.write('HELLO')
    f.seek(0)
    f.write('x')

# Serialization and Deserialization
# Serialization - process of converting python data types to JSON format
# Deserialization - process of converting JSON to python data types


# serialization using json module
# list
import json

L = [1,2,3,4]

with open('filehandling/demo.json','w') as f:
  json.dump(L,f)


# dict
import json
d = {
    'name':'nitish',
     'age':33,
     'gender':'male'
}

with open('filehandling/demo.json','w') as f:
  json.dump(d,f,indent=4)

# deserialization
import json

with open('filehandling/demo.json','r') as f:
  d = json.load(f)
  print(d['name'])
  print(type(d))

#json.dump() ->with write fn
#json.load() ->with read fn


class Person:

  def __init__(self,fname,lname,age,gender):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.gender = gender

# format to printed in
# -> Nitish Singh age -> 33 gender -> male
person= Person("nitish","gupta", 23,"Male")
# As a string
import json

def show_object(person):
  if isinstance(person,Person):
    return "{} {} age -> {} gender -> {}".format(person.fname,person.lname,person.age,person.gender)

with open('filehandling/demo.json','w') as f:
  json.dump(person,f,default=show_object)


# Pickling
# Pickling is the process whereby a Python object hierarchy is converted into a byte stream, and unpickling is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

# Pickle Vs Json
# Pickle lets the user to store data in binary format. JSON lets the user store data in a human-readable text format.
# pickle.dump()
# pickle.load()