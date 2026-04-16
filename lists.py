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