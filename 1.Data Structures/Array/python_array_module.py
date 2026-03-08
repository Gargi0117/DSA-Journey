# import array as a -> #importing array module and giving it an alias a
# we can also import array module by writing

from array import * # -> this will import all the functions and classes of array module

val=array('i',[1,2,3,4,5,6,7,8,9,10])
# print(val[0])

# for i in range(len(val)):
#     print(val[i],end=" ")

# print()

# for x in val: #enhanced for loop
#     print(x,end=",")

# #some functions of array module
# print(val.typecode) #typecode is used to find the type of array
# print(val.itemsize) #itemsize is used to find the size of each element in the array
# print(len(val)) #len() function is used to find the length of the array
# print(val.buffer_info()) #buffer_info() function is used to find the memory address and size of the array

# val.reverse() #reverse() function is used to reverse the array
# print(val) #now our array is reversed

# val.insert(0,11) #insert() function is used to insert an element at a specific position in the array
# val.append(12) #append() function is used to add an element at the end of the array
# print(val) #now our array is [11,1,2,3,4,5,6,7,8,9,10]

copy=array(val.typecode,(x for x in val))
print(copy)