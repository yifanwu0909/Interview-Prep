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
In Python, everything is an object, including numbers, strings, functions, and classes. This means that each entity in Python has attributes and methods associated with it, which define its properties and behaviors.   
[Back to TOC](#Interview-Questions)    

## Copy an object in Python
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
[Back to TOC](#Interview-Questions)    


## Mutable vs Immutable  
**Mutable types** are those that allow for the modification of their content without changing their identity (memory address):     
- Lists    
- Dictionaries    
- Sets
           
**Immutable types** do not allow their content to be changed after they are created. If you try to change an immutable object, a new object is created instead. 
- Integers
- Floats
- Strings
- Tuples

[Back to TOC](#Interview-Questions)  


## What are decorators in python
decorators wrap a function, modifying its behavior.   
To define a decorator, you typically define a function returning a wrapper function. The wrapper function uses *args and **kwargs to pass on arguments to the decorated function. If you want your decorator to also take arguments, you need to nest the wrapper function inside another function. In this case, you usually end up with three return statements. Decorators provide a simple syntax for calling higher-order functions. By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it. You'll use a decorator when you need to change the behavior of a function without modifying the function itself. A few good examples are when you want to add logging, test performance, perform caching, verify permissions, and so on. You can also use one when you need to run the same code on multiple functions.
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)

>>> say_whee()
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```
[Back to TOC](#Interview-Questions)  


 
## How python is different from C or C++
C is a compiled language. C++ is a compiled language. Python is an interpreted language. 
| Feature | C | C++ | Python |
|---------|---|-----|--------|
| **Development** | Developed by Dennis Ritchie between 1969 and 1973 at AT&T Bell Labs. | Developed by Bjarne Stroustrup in 1979. | Created by Guido van Rossum, and released in 1991. |
| **Code Complexity** | More difficult to write code due to complex syntax. | Code is less complex than C but more than Python. | Easier to write code. |
| **Lines of Code** | Longer lines of code. | Longer lines of code. | 3-5 times shorter than equivalent C/C++ programs. |
| **Variable Declaration** | Variables are declared. | Variables are declared. | No declaration. |
| **Language Type** | Compiled language. | Compiled language. | Interpreted language. |
| **Keywords** | Contains 32 keywords. | Contains 52 keywords. | Contains 33 keywords. |
| **Programming Paradigm** | Supports procedural programming. | Known as hybrid language, supports procedural and object-oriented programming. | Supports multiple paradigms: procedural, object-oriented, and functional programming. |
| **Inheritance** | Does not support inheritance. | Supports both single and multiple inheritance. | Supports all 5 types of inheritance: single, multiple, multilevel, hierarchical, and hybrid. |
| **Memory Management** | Provides `malloc()` and `calloc()` for allocation, `free()` for deallocation. | Provides `new` for allocation, `delete` for deallocation. | Memory allocation and deallocation is automatic. |
| **Exception Handling** | Does not support direct exception handling. | Supports exception handling. | Supports exception handling. |

[Back to TOC](#Interview-Questions)  


## Why interpreter languages are slow
Interpreting code is slower than running the compiled code because the interpreter must analyze each statement in the program each time it is executed and then perform the desired action, whereas the compiled code just performs the action within a fixed context determined by the compilation. This run-time analysis is known as "interpretive overhead". Having to reprocess a line every time in a loop is what makes interpreted languages so slow. This overhead means that interpreted code runs between 5 - 10 times slower than compiled code.  Access to variables is also slower in an interpreter because the mapping of identifiers to storage locations must be done repeatedly at run-time rather than at compile time. 

Think of it this way. If you can talk in your native language to someone, that would generally work faster than having an interpreter having to translate your language into some other language for the listener to understand. 

The bottom line is that all computers really "understand" is binary instructions, which is what "fast" languages like C are compiled into.

[Back to TOC](#Interview-Questions)  

## What is List comprehension
## Tuple VS a list
| Aspects \ Objects                                          | List                                               | Tuple                                              |
|------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------|
| Mutability                                                 | Lists are mutable                                  | Tuples are immutable                               |
| Iteration Implication                                      | The implication of iterations is Time-consuming    | The implication of iterations is comparatively Faster |
| Operations                                                 | The list is better for performing operations, such as insertion and deletion. | Tuple data type is appropriate for accessing the elements |
| Memory Consumption                                         | Lists consume more memory                          | Tuple consumes less memory as compared to the list |
| Built-in Methods                                           | Lists have several built-in methods                | Tuple does not have many built-in methods.         |
| Likelihood of Unexpected Changes and Errors                | The unexpected changes and errors are more likely to occur | In tuple, it is hard to take place.                 |

**Detail:**

Non interpreted means that it’s already in machine code. To run each instruction all you have to do is load it. So the pattern looks like

- load next instruction.
- execute instruction.
- advance to next instruction.
This is all done in hardware. This is what processors do.

The interpreter model lifts some responsibility to software. The interpreted model looks like this (bear in mind the the interpreter itself is usually compiled and running under the above model)

- read next line
  - this itself is many instructions (perhaps hundreds) from the interpreter
- interpret meaning of line
  - scan line for errors and parse line for meaning (perhaps hundreds or thousands of instructions in the interpreter)
- execute line
  - effectively performing an instruction at the machine level, however as this is at a higher level this is likely several instructions
If you think about the interpreter model every line has to be interpreted for meaning before execution. Even If we assume this step to be as cheap as possible (1 instruction) the interpreter model has to be 2x slower than machine code. But the interpretation step can involve 100’s of additional instructions. Thus an interpreted program is going to be orders of magnitude slower.

[Back to TOC](#Interview-Questions)  


## What is List comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.  

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
         newlist.append(x)

#VS:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
```

## 

## 

