# LIST

# append - ONE ITEM AT THE END OF THE LIST

l = [1,2,3]
l.append(4)
print (l)
l.append ('delhi')
print (l)

# extend - WILL TRY TO BREAK THE THING WE HAVE PROVIDED AND USED TO ADD MULIPLE ITEMS AT THE END OF THE LIST.
l = [1,2,3]
l.extend([4,5,6])
print (l)
l.extend ('delhi')
print (l)

# insert - IF WE WANNA ADD AN ELEMENT AT A SPECIFIC INDEX .
l= [1,2,3]
l.insert(1,100)
print (l)

 
 
#delete - takes index to delete a specific portion of list
l=[[1,2],[3,4]]
del l [0][1]
print(l)

#remove - dont have to pass index deletes element dynamically by passing the specific element
l=[1,2,22,424,3]
l.remove(22)
print (l)

#pop - deletes the last item of an element 

l=[4,3,1]
l.pop()
print(l)
l.pop(1)# can also delete by index
print(l)

#clear - deletes all the elements from the list

l= [3,4,'delhi',5]
l.clear()
print(l)

#OPERATIONS ON LIST

# + operator - merges two list
l1= [1,2,3]
l2=[2,3,5]
print(l1+l2) 

# * repeats the list n times

print (l1*3)

#membership operator
l=[1,21,3]
print(21 in l)

#LOOP

L1= [1,2,44,75,7]

for i in L1:
    print(i)

# SOME FUNCTIONS
L1= [1,2,44,75,7,1,2]
print(min(L1))
print(max(L1))
print(len(L1))
print(sorted(L1))
print(sum(L1))
print(L1.count(2))

#SORT VS SORTED
L=[1,34,42,2,53,5,8]


#SORTED IS A TEMPORARY OPERATION ORIGINAL LIST DOES NT CHANGE

print(sorted(L))
print (L)

L.sort()
print(L)


#COPY

L=[1,2,3,31.3]
L2= L.copy()
print (L)
print(id(L))
print (L2)
print (id(L2))

#BOTH ARE DIFFERENT LIST SINCE THE ADDRESS OF BOTH ARE DIFFERENT BUT THE VALUES OF BOTHM OF THE LISTS ARE SAME

#LIST COMPREHENSION

L=[i for i in range (1,11)]
print(L)

l= [1,2,3,4]

l2=[i**2 for i in l ]
print(l2)

l=[]

l=[i for i in range(1,51) if i%5==0]
print (l)
