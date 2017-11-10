Array:
======
convert the type to float and reverse the array
import numpy
print numpy.array(input().split(),float)[::-1]
--------------------------------------------------------------

reversed_array = numpy.fliplr(numpy.array([input_data],float))[0]

--------------------------------------------------------------
print numpy.flipud(numpy.array(raw_input().split(),float))

return(numpy.array(arr[::-1], float))

############################################################################

Shape and Reshape
=================


import numpy

my__1D_array = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape     #(5,) -> 5 rows and 0 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print my_2D_array.shape     #(3, 2) -> 3 rows and 2 columns 
-------------------------------------------------------------
import numpy

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print change_array      

#Output
[[1 2]
[3 4]
[5 6]]

--------------------------------------------------------------
import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]

--------------------------------------------------------------
import numpy

arr=numpy.array(input().split(),int)
print(numpy.reshape(arr,(3,3)))

import numpy as np
print(np.array(input().split(),int).reshape(3,3))

numpy.reshape(numpy.array(raw_input().split(),int),(3,3))

############################################################################
Transpose 
=========
import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print numpy.transpose(my_array)

#Output
[[1 4]
 [2 5]
 [3 6]]

Flatten 
======== 
 import numpy

my_array = numpy.array([[1,2,3],
                        [4,5,6]])
print my_array.flatten()

#Output
[1 2 3 4 5 6]

numpy.ndarray.flatten(arr)
OR
numpy.matrix.flatten(arr)

--------------------------------------------------------------
import numpy as np
N,M=map(int,input().split())

lst=[]
for i in range(N):
    lst.append(list(map(int,input().split())))

my_array=np.array(lst)    
print(np.transpose(my_array))
print(my_array.flatten())
--------------------------------------------------------------
import numpy

N, M = map(int,raw_input().split())

my_array = numpy.array( [map(int,input().split()) for i in range(N)] )
print numpy.transpose(my_array)
print my_array.flatten()

--------------------------------------------------------------    
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())

-------------------------------------------------------------- 
Concatenate 
===========
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))    

#Output
[1 2 3 4 5 6 7 8 9]

-------------------------------------------------------------- 

import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]] 

-------------------------------------------------------------- 

import numpy

N,M,P=map(int,input().split())

arr1=numpy.array([input().split() for _ in range(N)],int)
arr2=numpy.array([input().split() for _ in range(M)],int)

print(numpy.concatenate((arr1,arr2),axis=0))

############################################################################
Zeros and Ones
==============
zeros
-----
The zeros tool returns a new array with a given shape and type filled with 's.

import numpy

print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]


ones
-----
The ones tool returns a new array with a given shape and type filled with 's.

import numpy

print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]

--------------------------------------------------------------
import numpy


lst=list(map(int,input().split()))

print(numpy.zeros((lst), dtype = numpy.int) )
print(numpy.ones((lst), dtype = numpy.int))

############################################################################

Eye and Identity
================ 
identity

The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as  and the rest as . The default type of elements is float.

import numpy
print numpy.identity(3) #3 is for  dimension 3 X 3

#Output
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
eye

The eye tool returns a 2-D array with 's as the diagonal and 's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter . A positive  is for the upper diagonal, a negative  is for the lower, and a   (default) is for the main diagonal.

import numpy
print numpy.eye(8, 7, k = 1)    # 8 X 7 Dimensional array with first upper diagonal 1.

#Output
[[ 0.  1.  0.  0.  0.  0.  0.]
 [ 0.  0.  1.  0.  0.  0.  0.]
 [ 0.  0.  0.  1.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.]
 [ 0.  0.  0.  0.  0.  1.  0.]
 [ 0.  0.  0.  0.  0.  0.  1.]
 [ 0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.]]

print numpy.eye(8, 7, k = -2)   # 8 X 7 Dimensional array with second lower diagonal 1.

-----------------------------------------------------------------------------------------------------------

import numpy

N,M=map(int,input().split())

print(numpy.eye(N,M, k = 0))

############################################################################

import numpy

a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print a + b                     #[  6.   8.  10.  12.]
print numpy.add(a, b)           #[  6.   8.  10.  12.]

print a - b                     #[-4. -4. -4. -4.]
print numpy.subtract(a, b)      #[-4. -4. -4. -4.]

print a * b                     #[  5.  12.  21.  32.]
print numpy.multiply(a, b)      #[  5.  12.  21.  32.]

print a / b                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print numpy.divide(a, b)        #[ 0.2         0.33333333  0.42857143  0.5       ]

print a % b                     #[ 1.  2.  3.  4.]
print numpy.mod(a, b)           #[ 1.  2.  3.  4.]

print a**b                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print numpy.power(a, b)         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]

-----------------------------------------------------------------------------------------------------------

import numpy as np

n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(*[a+b, a-b, a*b, a//b, a%b, a**b],sep='\n')

############################################################################

Floor, Ceil and Rint
====================

floor 
The tool floor returns the floor of the input element-wise. 
The floor of  is the largest integer  where .

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.floor(my_array)         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
ceil 
The tool ceil returns the ceiling of the input element-wise. 
The ceiling of  is the smallest integer  where .

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.ceil(my_array)          #[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
rint 
The rint tool rounds to the nearest integer of input element-wise.

import numpy

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

-----------------------------------------------------------------------------------------------------------

import numpy


my_array = numpy.array(input().split(),float)

print(*[numpy.floor(my_array) ,numpy.ceil(my_array),numpy.rint(my_array)],sep='\n')

############################################################################
Sum and Prod 
============

sum

The sum tool returns the sum of array elements over a given axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.sum(my_array, axis = 0)         #Output : [4 6]
print numpy.sum(my_array, axis = 1)         #Output : [3 7]
print numpy.sum(my_array, axis = None)      #Output : 10
print numpy.sum(my_array)                   #Output : 10
By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

prod

The prod tool returns the product of array elements over a given axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.prod(my_array, axis = 0)            #Output : [3 8]
print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
print numpy.prod(my_array, axis = None)         #Output : 24
print numpy.prod(my_array)                      #Output : 24
By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input array.

-----------------------------------------------------------------------------------------------------------
import numpy as np

N,M=map(int,input().split())

my_array = np.array([input().split() for _ in range(N)], dtype=int) 

print(np.prod(np.sum(my_array, axis = 0)))

############################################################################
Min and Max
===========
min

The tool min returns the minimum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0
By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

max

The tool max returns the maximum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7
By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.

-------------------------------------------------------------------------------------------------------------
import numpy as np

N,M=map(int,input().split())

my_array = np.array([input().split() for _ in range(N)], dtype=int) 

print(np.max(np.min(my_array,axis=1)))

############################################################################
Mean, Var, and Std
==================

mean
----
The mean tool computes the arithmetic mean along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5
By default, the axis is None. Therefore, it computes the mean of the flattened array.

var
---
The var tool computes the arithmetic variance along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25
By default, the axis is None. Therefore, it computes the variance of the flattened array.

std
---
The std tool computes the arithmetic standard deviation along the specified axis.

import numpy

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875
By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.

-------------------------------------------------------------------------------------------------------
import numpy as np

N,M=map(int,input().split())

my_array = np.array([input().split() for _ in range(N)], dtype=int) 

print(*[np.mean(my_array,axis=1),np.var(my_array,axis=0),np.std(my_array)],sep='\n')

############################################################################
Dot and Cross
==============
dot
---
The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11

cross
-----
The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
-------------------------------------------------------------------------------------------------------

import numpy as np

N=int(input())

A,B=(np.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))

print(np.dot(A,B))


Sample Input

2
1 2
3 4
1 2
3 4
Sample Output

[[ 7 10]
 [15 22]]

############################################################################

Inner and Outer 
=================

The inner tool returns the inner product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4
outer

The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
							
############################################################################							