# Interview Questions

# Python Questions

- [OOP - Python](#oop---python)
- [Copy an object in Python](#copy-an-object-in-python)
  - [Shallow Copy](#shallow-copy)
  - [Deep Copy](#deep-copy)
- [Mutable vs Immutable](#mutable-vs-immutable)
- [Decorators in python](#what-are-decorators-in-python)
- [How python is different from C or C++?](#how-python-is-different-from-c-or-c)
- [Why interpreter languages are slow?](#why-interpreter-languages-are-slow)
- [What is List comprehension?](#what-is-list-comprehension)
- [Tuple VS a list](#tuple-vs-a-list)

## OOP - Python
[Back to TOC](#Interview-Questions)    
In Python, everything is an object, including numbers, strings, functions, and classes. This means that each entity in Python has attributes and methods associated with it, which define its properties and behaviors.


## Copy an object in Python
[Back to TOC](#Interview-Questions)    
### Shallow Copy
A shallow copy creates a new object, but instead of copying the objects that the original object references, it only copies the references to those objects. Therefore, changes to mutable objects within the copied object would reflect in the original object as well.
```python
shallow_copied_list = copy.copy(original_list)
copied_list = original_list[:]
copied_dict = original_dict.copy()
```
### Deep Copy
A deep copy creates a new object and recursively copies all the objects it references. Changes to any level of nested objects within the copied object will not affect the original object.
```python
deep_copied_list = copy.deepcopy(original_list)
```


## Mutable vs Immutable
[Back to TOC](#Interview-Questions)    
**Mutable types** are those that allow for the modification of their content without changing their identity (memory address):     
- Lists    
- Dictionaries    
- Sets
           
**Immutable types** do not allow their content to be changed after they are created. If you try to change an immutable object, a new object is created instead. 
- Integers
- Floats
- Strings
- Tuples


## What are decorators in python
## How python is different from C or C++

## Why interpreter languages are slow

## What is List comprehension
## Tuple VS a list
##

## 

## 

