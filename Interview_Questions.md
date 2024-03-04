# Interview Questions

## Python Questions
- [OOP-Python](#OOP-Python)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Advanced Usage](#advanced-usage)
- [Contributing](#contributing)
- [License](#license)

OOP - Python

In Python, everything is an object, including numbers, strings, functions, and classes. This means that each entity in Python has attributes and methods associated with it, which define its properties and behaviors. 

Copy an object in Python

Shallow Copy
A shallow copy creates a new object, but instead of copying the objects that the original object references, it only copies the references to those objects. Therefore, changes to mutable objects within the copied object would reflect in the original object as well.
shallow_copied_list = copy.copy(original_list)
copied_list = original_list[:]
copied_dict = original_dict.copy()
Deep Copy
A deep copy creates a new object and recursively copies all the objects it references. Changes to any level of nested objects within the copied object will not affect the original object.
deep_copied_list = copy.deepcopy(original_list)



## OOP-Python
Content for the introduction section.

## Installation
Content for the installation section.

## Usage
### Basic Usage
Content for the basic usage subsection.

### Advanced Usage
Content for the advanced usage subsection.

## Contributing
Content for the contributing section.

## License
Content for the license section.



OOP - Python

In Python, everything is an object, including numbers, strings, functions, and classes. This means that each entity in Python has attributes and methods associated with it, which define its properties and behaviors. 

Copy an object in Python

Shallow Copy
A shallow copy creates a new object, but instead of copying the objects that the original object references, it only copies the references to those objects. Therefore, changes to mutable objects within the copied object would reflect in the original object as well.
shallow_copied_list = copy.copy(original_list)
copied_list = original_list[:]
copied_dict = original_dict.copy()
Deep Copy
A deep copy creates a new object and recursively copies all the objects it references. Changes to any level of nested objects within the copied object will not affect the original object.
deep_copied_list = copy.deepcopy(original_list)


Mutable vs Immutable
Mutable types are those that allow for the modification of their content without changing their identity (memory address): Lists, Dictionaries, Sets
Immutable types do not allow their content to be changed after they are created. If you try to change an immutable object, a new object is created instead. 
Integers, Floats, Strings, Tuples

What are decorators in python?

	decorators wrap a function, modifying its behavior.
	to define a decorator, you typically define a function returning a wrapper function. The wrapper function uses *args and **kwargs to pass on arguments to the decorated function. If you want your decorator to also take arguments, you need to nest the wrapper function inside another function. In this case, you usually end up with three return statements.
	
	Decorators provide a simple syntax for calling higher-order functions. By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
	
	You'll use a decorator when you need to change the behavior of a function without modifying the function itself. A few good examples are when you want to add logging, test performance, perform caching, verify permissions, and so on. You can also use one when you need to run the same code on multiple functions.
```
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


How python is different from C or C++?

	C is a compiled language. C++ is a compiled language. Python is an interpreted language. 
	link
C
C++
Python
C was developed by Dennis Ritchie between the year 1969 and 1973 at AT&T Bell Labs.
C++ was developed by Bjarne Stroustrup in 1979.
Python was created by Guido van Rossum, and released in 1991.
More difficult to write code in contrast to both Python and C++ due to complex syntax.
C++ code is less complex than C but more complex in contrast to python.
Easier to write code.
Longer lines of code as compared to python.
Longer lines of code as compared to python.
3-5 times shorter than equivalent C/C++ programs.
Variables are declared in C.
Variables are declared in C++
Python has no declaration.
C is a compiled language.
C++ is a compiled language.
Python is an interpreted language.
C contains 32 keywords.
C++ contains 52 keywords.
Python contains 33 keywords.
For the development of code, C supports procedural programming.
C++ is known as hybrid language because C++ supports both procedural and object oriented programming paradigms.
Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
C does not support inheritance.
C++ support both single and multiple inheritance
Python supports all 5 types of inheritance i.e. single inheritance, multiple inheritance, multilevel inheritance, hierarchical inheritance, and hybrid inheritance
C provides malloc() and calloc() functions for dynamic memory allocation, and free() for memory de-allocation.
C++ provides new operator for memory allocation and delete operator for memory de-allocation.
Python’s memory allocation and deallocation method is automatic.
Direct support for exception handling is not supported by C.
Exception handling is supported by C++.
Exception handling is supported by Python.


Why interpreter languages are slow?

	Interpreting code is slower than running the compiled code because the interpreter must analyze each statement in the program each time it is executed and then perform the desired action, whereas the compiled code just performs the action within a fixed context determined by the compilation. This run-time analysis is known as "interpretive overhead". Having to reprocess a line every time in a loop is what makes interpreted languages so slow. This overhead means that interpreted code runs between 5 - 10 times slower than compiled code.  Access to variables is also slower in an interpreter because the mapping of identifiers to storage locations must be done repeatedly at run-time rather than at compile time. 
	
	Think of it this way. If you can talk in your native language to someone, that would generally work faster than having an interpreter having to translate your language into some other language for the listener to understand. 
	
	The bottom line is that all computers really "understand" is binary instructions, which is what "fast" languages like C are compiled into.
	

        Detail:

	
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


What is List comprehension?

	List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.  

	fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
	newlist = []
	for x in fruits:
		if "a" in x:
	         newlist.append(x)
	
	VS:
	
	fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
	newlist = [x for x in fruits if "a" in x]


Tuple VS a list

	The primary difference between tuples and lists is that tuples are immutable as opposed to lists which are mutable. Therefore, it is possible to change a list but not a tuple. The contents of a tuple cannot change once they have been created in Python due to the immutability of tuples. 
LIST
TUPLE
Lists are mutable
Tuples are immutable
The implication of iterations is Time-consuming
The implication of iterations is comparatively Faster
The list is better for performing operations, such as insertion and deletion.
Tuple data type is appropriate for accessing the elements
Lists consume more memory
Tuple consumes less memory as compared to the list
Lists have several built-in methods
Tuple does not have many built-in methods.
The unexpected changes and errors are more likely to occur
In tuple, it is hard to take place.
