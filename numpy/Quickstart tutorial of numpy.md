# **Quickstart tutorial** 
## **Prerequisties**
Before reading this tutorial you should know a bit of Python.If you would like to refresh your 
memory,take a look at the Python tutorial.

If you wish work the examples in this tutoral, you must also have some software installed on your
computer.Please see http://scipy.org/install.html for instructions.

## **The Basics**
NumpyPy's main object is the homogeneous multidimensional array. It is a table of elements(usually numbers),all
of the same type,indexed by a tuple of positive integers.In Numpy dimensions are called axes.The number of axes 
is rank.

For example, the coordinates of a point in 3D space [1, 2, 1] is an array of rank 1,because it has one axis.That
axis has a length of 3. In example pictured below,the array has rank 2(it is 2-dimensional).The first dimension(axis)
has a length of 2, the second dimension has a length of 3.
```Python
[[1., 0., 0.],
 [0., 1., 2.]]
 ```
 Numpy's array class is called ndarray.It is also known by the alias array.Note that numpy.array is not the same as the 
 Standard Python Library class array.array,which only handles one-dimensional arrays and offers less functionality.The 
 more important attributes of an ndarray object are:

**ndarray.ndim**

 the number of axes(dimensions) of the array.In the Python world,the number of dimensions is referred to as rank.

**ndarray.shape**

the dimensions of the array.This is a tuple of integers indicating the size of the array in each dimension.For a matrix
with n rows and m columns, shape will be (n, m).The length of the shape tuple is therefore the rank, or number of dimensions,ndim.

**ndarray.size**

the total number of elements of the array.This is equal to the product of the elements of shape.

**ndarray.dtype**

an object describing the type of the elements in the array.One can create or specify dtype's using standard Python types.Addtionaly Numpy provides
types of its own.numpy.int32,numpy.int16,and numpy.float64 are some examples.

**ndarray.itemsize**

the size in bytes of each element of the array.For example, an array of elements of type float64 has itemsize 8(=64/8),while one of type complex32 has
itemsize4(=32/8).It is equivalent to ndarray.dtype.itemsize.

**ndarray.data**

the buffer containing the actual elements of the array.Normally, we won't need to use this attribute because we will access the elements in an array using 
indexing facilities.

### **An example**
```Python
import numpy as np
a = np.arange(15).reshape(3, 5)
print a
```
###  **Indexing,Slicing and Iterating**
**One-dimensional** arrays can be indexed,sliced and iterated over,much like lists and other Python sequences.
```Python
>>> a = np.arange(10) ** 3
>>> a
array([0, 1, 8, 27, 64, 125, 216, 343, 512, 729])
>>>a[2]
8
>>>a[2:5]
array([8, 27, 64])
>>>a[:6:2] = -1000
>>>a
array([-1000, 1, -1000, 27, -1000, 125, 216, 343, 512, 729])
>>>a[: : -1]
array([729, 512, 343, 216, 125, -1000, 27, -1000, 1, -1000])
>>>for i in a:
...    print i**(1/3.)
...
>>>
nan
1.0
nan
3.0
nan
5.0
6.0
7.0
8.0
9.0
```
**multidimensional** arrays can have one index per axis.These indices are given in a tuple separated by commas:
```Python
>>> def f(x,y):                                                     
...     return 10*x + y                                             
...                                                                 
>>> b = np.fromfunction(f,(5,4),dtype=int)                          
>>> b                                                               
array([[ 0,  1,  2,  3],                                            
       [10, 11, 12, 13],                                            
       [20, 21, 22, 23],                                            
       [30, 31, 32, 33],                                            
       [40, 41, 42, 43]]) 
>>> b[2, 3]                                                         
23                                                                  
>>> b[0:5, 1]                                                       
array([ 1, 11, 21, 31, 41])                                         
>>> b[ : , 1]                                                       
array([ 1, 11, 21, 31, 41])                                         
>>> b[1:3, :]                                                       
array([[10, 11, 12, 13],                                            
       [20, 21, 22, 23]])
```
When fewer indices are provided than the number of axes, the missing indices are considered complete slices:
```Python 
>>> b[-1]                                                           
array([40, 41, 42, 43]) 
```
The expression within brackets in b[i] is treated as an i followed by as many instance of : as needed to represent the remianing axes.Numpy also allows 
you to write this using dots as b[i,...].

The dots(...) represent as many colons as needed to produce a complete indexing tuple.For example,if x is a rank 5 array(ie, it has 5 axes),then
- x[1,2,...] is equivalent to x[1,2,:,:,:]
- x[...,3] to x[:,:,:,:, 3] and
- x[4,...,5,:] to x[4,:,:,5,:].
```Python 
>>> c = np.array([[[ 0, 1, 2],       # a 3D array (two stacked 2D arrays)
                   [ 10, 12, 13],
                  [[100, 101, 102],
                   [110, 112, 113]]])
>>>c.shape
(2, 2, 3)
>>> c[1,...]
array([[100, 101, 102],
       [110, 112, 113]])
>>> c[...,2]
array([[ 2, 13],
       [102, 113]])
```
**Iterating** over multidimensional arrays is done with repect to the first axis:
```Python
>>> for row in b:
...    print row
...
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```
However,if one wants to perform an operation on each element in the array, one can use the flat attribute which
is an iterator over all the elements of the array:
```Python
>>> for element in b.flat:
...    print element
...
0
1
2
3
10
11
12
13
20
21
22                                                                  
23                                                                  
30                                                                  
31                                                                  
32                                                                  
33                                                                  
40                                                                  
41                                                                  
42                                                                  
43        
```
## **Shape Manipulation** 
### Changing the shape of an array
An array has a shape given by the number of elements along each axis:
```Python
>>> a = np.floor(10*np.random.random((3,4)))                          
>>> a                                                                 
array([[ 7.,  3.,  5.,  1.],                                          
       [ 1.,  4.,  5.,  4.],                                          
       [ 3.,  4.,  6.,  4.]])                                         
>>> a.shape                                                           
(3, 4)   
```
The shape of an array can be changed with various commands:
```Python 
>>> a.ravel() # flatten the array                                     
array([ 7.,  3.,  5.,  1.,  1.,  4.,  5.,  4.,  3.,  4.,  6.,  4.])   
>>> a.shape                                                           
(3, 4)                                                                
>>> a.shape = (6, 2)                                                  
>>> a.T                                                               
array([[ 7.,  5.,  1.,  5.,  3.,  6.],                                
       [ 3.,  1.,  4.,  4.,  4.,  4.]]) 
```
The order of the elements in the array resulting from ravel() is normally “C-style”, that is, the rightmost index “changes the fastest”, so the element 
after a[0,0] is a[0,1]. If the array is reshaped to some other shape, again the array is treated as “C-style”. Numpy normally creates arrays stored in 
this order, so ravel() will usually not need to copy its argument, but if the array was made by taking slices of another array or created with unusual 
options, it may need to be copied. The functions ravel() and reshape() can also be instructed, using an optional argument, to use FORTRAN-style arrays, 
in which the leftmost index changes the fastest.

The reshape function returns its argument with a modified shape, whereas the ndarray.resize method modifies the array itself:
```Python
array([[ 7.,  3.],                                                    
       [ 5.,  1.],                                                    
       [ 1.,  4.],                                                    
       [ 5.,  4.],                                                    
       [ 3.,  4.],                                                    
       [ 6.,  4.]])                                                   
>>> a.resize((2, 6))                                                  
>>> a                                                                 
array([[ 7.,  3.,  5.,  1.,  1.,  4.],                                
       [ 5.,  4.,  3.,  4.,  6.,  4.]])   
```
If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
```Python
>>> a.reshape(3, -1)                                                  
array([[ 7.,  3.,  5.,  1.],                                          
       [ 1.,  4.,  5.,  4.],                                          
       [ 3.,  4.,  6.,  4.]]) 
```
### Stacing together different arrays
Several arrays can be stacked together along different axes:
```Python
>>> a = np.floor(10**np.random.random((2, 2)))                        
>>> a                                                                 
array([[ 1.,  1.],                                                    
       [ 3.,  1.]])                                                   
>>> b = np.floor(10*np.random.random((2, 2)))                         
>>> b    
array([[ 9.,  9.],                                                    
       [ 1.,  0.]])                                                   
>>> np.vstack( (a, b))                                                
array([[ 1.,  1.],                                                    
       [ 3.,  1.],                                                    
       [ 9.,  9.],                                                    
       [ 1.,  0.]])                                                   
>>> np.hstack( (a, b) )                                               
array([[ 1.,  1.,  9.,  9.],                                          
       [ 3.,  1.,  1.,  0.]])
```
The function column_stack stacks 1D arrays as columns into a 2D array.It is equivalent to vstack only for 1D arrays:
```Python
>>> a = np.array([4., 2.])                                                                  
>>> b = np.array([2., 8.])                                                                  
>>> a[:,newaxis]                                                                            
array([[ 4.],                                                                               
       [ 2.]])                                                                              
>>> np.column_stack((a[:, newaxis], b[:, newaxis]))                                         
array([[ 4.,  2.],                                                                          
       [ 2.,  8.]]) 
>>> np.vstack((a[:, newaxis], b[:,newaxis])) #The behavior of vstack is different           
array([[ 4.],                                                                               
       [ 2.],                                                                               
       [ 2.],                                                                               
       [ 8.]]) 
```
For arrays of with more than two dimensions, hstack stacks along their second axes, vstack stacks along their first 
axes, and concatenate allows for an optional arguments giving the number of the axis along which the concatenation 
should happen.

### **Note**
In complex cases, r_ and c_ are useful for creating arrays by stacking numbers along one axis. They allow the use of 
range literals (”:”) :
```Python
>>> np.r_[1:4, 0, 4]                                                                  
array([1, 2, 3, 0, 4])
```
When used with arrays as arguments,r_ and c_ are similar to vstack and hstack in their default behavior,but allow for
an optional argument giving the number of the axis along which to concatenate.

### **Splitting one array into serveral smaller ones**
Using hsplit,you can split an array along its horizontal axis,either by specifying the number of equally shaped array to 
return, or by specifying the columns after which the division should occur:
```Python 
>>> a = np.floor(10*np.random.random((2, 12)))                                        
>>> a                                                                                 
array([[ 6.,  0.,  6.,  8.,  8.,  4.,  6.,  3.,  1.,  4.,  9.,  4.],                  
       [ 7.,  6.,  8.,  2.,  2.,  9.,  5.,  2.,  0.,  3.,  5.,  7.]])                 
>>> np.hsplit(a, 3) # Split a into 3                                                  
[array([[ 6.,  0.,  6.,  8.],                                                         
       [ 7.,  6.,  8.,  2.]]), array([[ 8.,  4.,  6.,  3.],                           
       [ 2.,  9.,  5.,  2.]]), array([[ 1.,  4.,  9.,  4.],                           
       [ 0.,  3.,  5.,  7.]])] 
>>> np.hsplit(a, (3, 4)) # Split a after the third and the fourth column              
[array([[ 6.,  0.,  6.],                                                              
       [ 7.,  6.,  8.]]), array([[ 8.],                                               
       [ 2.]]), array([[ 8.,  4.,  6.,  3.,  1.,  4.,  9.,  4.],                      
       [ 2.,  9.,  5.,  2.,  0.,  3.,  5.,  7.]])] 

```
vsplit splits along the vertical axis, and array_split allows one to specify along which axis to split.

## Copies and Views
When operating and manipulating arrays,their data is copied into a new array and sometimes not.This is often 
a source of confusion for beginners.There are three cases:
### No copy at all
Simple assignments make no copy of array objects or of their data.
```Python
>>> a = np.arange(12)   # no new object is created                                                                    
>>> b = a                                                                                   
>>> b is a         # a and b are two names for the same ndarray object                                                                         
True                                                                                        
>>> b,shape = 3,4    # changes the shape of a                                                                       
>>> a.shape                                                                                 
(12,)    
```
Python passes mutable objects as references, so function calls make no copy.
```Python
>>> def f(x):                                                                               
...     print id(x)                                                                         
...                                                                                         
>>> id(a)        # id is a unique identifier of  an object                                                                           
140322807799040                                                                             
>>> f(a)                                                                                    
140322807799040 
```
## View or Shallow Copy
Different array objects can share the same data.The view method creates a new array object that looks at the same data.
```Python
>>> c = a.view()                                                                            
>>> c is a                                                                                  
False                                                                                       
>>> c.base is a                                                                             
True                                                                                        
>>> c.flags.owndata                                                                         
False                                                                                       
>>>        
>>> c.shape = 2, 6                                                                          
>>> a.shape                                                                                 
(12,)                                                                                       
>>> c[0,4] = 1234                                                                           
>>> a                                                                                       
array([   0,    1,    2,    3, 1234,    5,    6,    7,    8,    9,   10,                    
         11])  
```
Slicing an array returns a view of it:
```Python
>>> s = a[ : , 1:3]  # spaces added for clarity;could also be written "s = a[:, 1:3]"
>>> s[:] = 10        # s[:] is a view of s. Note the difference between s=10 and s[:]=10
>>> a
array([[   0, 10, 10, 3],
       [1234, 10, 10, 7],
       [   8, 10, 10, 11]])
```
### Deep Copy
The copy method makes a complete copy of the array and its data.
```Python
>>> d = a.copy        # a new array object with new data is created
>>> d is a
False
>>> d.base is a      # d doesn't share anything with a
False
>>> d[0,0] = 9999
>>> a
array([[   0, 10, 10,  3],
       [1234, 10, 10,  7],
       [   8, 10, 10, 11]])
```













