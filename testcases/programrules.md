##### About Python 
1) python is interpreted language which executes line by line.
2) python has good library function which makes it easy for modification of data
3) python memory manager handles the memory management it allocates The memory in form of a private heap space
4) All Python objects are stored in this heap and being private, 
   it is inaccessible to the programmer. 
5) Though, python does provide some core API functions to work upon the private heap space.
6) Python has an in-built garbage collection to recycle the unused memory for the private heap space.

##### Python is call by value or Call by reference
1) python pass objects (reference): if you do an operation that works on same object, it will be pointing to same object. 

2) if you do a new assignment, it will create a new object

3) python pass value : No change in the original copy

#### Differences between Generator function and Normal function
1) Generator function contains one or more yield statements.

2) When called, it returns an object (iterator) but does not start execution immediately.

3) Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().

4) Once the function yields, the function is paused and the control is transferred to the caller.

5) Local variables and their states are remembered between successive calls.

6) Finally, when the function terminates, StopIteration is raised automatically on further calls.

#### Python TypeError: 'int' object is not sub-scriptable
1) This error occurs when your program has a variable that is treated as an array 
by your function, but actually, that variable is an integer.

### Advance operators
1) ** Exponent
2) // floor division (discard the remainder)
3) x is y, here is results is 1 if id(x) equals id(y).
4) x is not y, here is not results in 1 if id(x) is not equal to id(y).
