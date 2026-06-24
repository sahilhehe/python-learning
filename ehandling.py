# There are 2 stages where error may happen in a program

# - During compilation -> Syntax Error
# - During execution -> Exceptions

### Syntax Error

# - Something in the program is not written according to the program grammar.
# - Error is raised by the interpreter/compiler
# - You can solve it by rectifying the program

# Other examples of syntax error
# Leaving symbols like colon,brackets
# Misspelling a keyword
# Incorrect indentation
# empty if/else/loops/class/functions


### Exceptions

# If things go wrong during the execution of the program(runtime). It generally happens when something unforeseen has happened.

# - Exceptions are raised by python runtime
# - You have to takle is on the fly

# #### **Examples**

# - Memory overflow
# - Divide by 0 -> logical error
# - Database error

# try catch demo
# let's create a file
# with open('sample.txt','w') as f:
#   f.write('hello world')

# try:
#   with open('sample1.txt','r') as f:
#     print(f.read())
# except:
#   print('sorry file not found')