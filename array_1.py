"""Array Data Structure

An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).

Other than some generic containers like list, Python in its definition can also handle containers with specified data types. Array can be handled in python by module named “array“. They can be useful when we have to manipulate only a specific data type values.

Operations on Array :

1. array(data type, value list) :- This function is used to create an array with data type and value list specified in its arguments.


TYPE CODE	C TYPE	PYTHON TYPE	MINIMUM SIZE IN BYTES
‘b’	    signed char	int			            1
‘B’	    unsigned char	int			        1
‘u’	    Py_UNICODE	unicode character	    2
‘h’	    signed short	int			        2
‘H’	    unsigned short	int			        2
‘i’	    signed int	int			            2
‘I’	    unsigned int	int		        	2
‘l’	    signed long	int			            4
‘L’	    unsigned long	int		        	4
‘q’	    signed long long	int		        8
‘Q’	    unsigned long long	int		        8
‘f’	    float		float			        4
‘d’	    double		float			        8


2. append() :- This function is used to add the value mentioned in its arguments at the end of the array.

3. insert(i,x) :- This function is used to add the value at the position specified in its argument."""

import array

arr = array.array('i', [1, 2, 3])

arr.append(4)  # appends at last position

arr.insert(3, 0)  # (position of insertion, element to insert)
for i in range(0, len(arr)):
    print(arr[i])

print('pop', arr.pop(
    1))  # function removes the element at the position mentioned in its argument, and returns it  by default removes last element

arr.append(0)
print(arr.remove(0))  # function is used to remove the first occurrence of the value mentioned in its arguments.
print(arr)

print(arr.reverse())  # reversed array

print('*' * 50)
for i in range(0, len(arr)):
    print(arr[i])

print(arr.typecode)  # prints array datatype
print(arr.itemsize)  # itemsize of array
print(arr.buffer_info())  # using buffer_info() to print buffer info. of array
arr.append(0)
arr.append(0)
arr.append(0)
arr.append(0)
arr2 = array.array('i', [1, 2, 3])
print(arr.count(0))  # function counts the number of occurrences of argument mentioned in array

# using extend() to add array 2 elements to array 1
arr.extend(arr2)

print(arr)

# initializing list
li = [1, 2, 3]

# using fromlist() to append list at end of array
arr.fromlist(li)
print(arr)

# using tolist() to convert array into list
li2 = arr.tolist()

print(li2)
