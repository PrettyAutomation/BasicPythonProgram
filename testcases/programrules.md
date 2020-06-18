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