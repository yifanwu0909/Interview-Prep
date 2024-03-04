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
- [What does the generator function do in Python?](#what-does-the-generator-function-do-in-Python)
- [Explain the map function.](#explain-the-map-function)
- [Explain what init.py does](#explain-what-initpy-does).
- [Reduce function](#reduce-function)
- [Filter function](#filter-function)
- [Could you explain whether all memory gets freed when Python exits?](#Could-you-explain-whether-all-memory-gets-freed-when-python-exits)

## OOP - Python
In Python, everything is an object, including numbers, strings, functions, and classes. This means that each entity in Python has attributes and methods associated with it, which define its properties and behaviors.   
[Back to TOC](#Python-Questions)    

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
[Back to TOC](#Python-Questions)  


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

[Back to TOC](#Python-Questions)  


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
[Back to TOC](#Python-Questions)   


 
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

[Back to TOC](#Python-Questions)  


## Why interpreter languages are slow
Interpreting code is slower than running the compiled code because the interpreter must analyze each statement in the program each time it is executed and then perform the desired action, whereas the compiled code just performs the action within a fixed context determined by the compilation. This run-time analysis is known as "interpretive overhead". Having to reprocess a line every time in a loop is what makes interpreted languages so slow. This overhead means that interpreted code runs between 5 - 10 times slower than compiled code.  Access to variables is also slower in an interpreter because the mapping of identifiers to storage locations must be done repeatedly at run-time rather than at compile time. 

Think of it this way. If you can talk in your native language to someone, that would generally work faster than having an interpreter having to translate your language into some other language for the listener to understand. 

The bottom line is that all computers really "understand" is binary instructions, which is what "fast" languages like C are compiled into.

[Back to TOC](#Python-Questions)   


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
[Back to TOC](#Python-Questions)  


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

[Back to TOC](#Python-Questions)  


## What does the generator function do in Python?
A special type of function that returns an iterator object. Instead of returning a single value, a generator yields a sequence of results, producing one item at a time and only when required. This is achieved using the `yield` statement instead of `return`. 

Here's what makes generator functions powerful:

1. **Lazy Evaluation**: Generator functions compute values on the fly and do not store the entire sequence in memory. This makes them highly efficient for working with large datasets or infinite sequences, as they only produce items when needed.

2. **Memory Efficiency**: Since the values are generated on demand and not stored, generator functions are memory efficient, especially when dealing with large data streams.

3. **Simplicity**: Generators can simplify code that would otherwise require complex iterators or recursive functions.

Here is a simple example of a generator function:

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)
```

In this example, `count_up_to` is a generator function that yields numbers from 1 up to a specified `max`. When used in a for loop, it generates numbers one by one; after yielding a number, it pauses its state until the next number is requested.

Key points to remember about generator functions:
- They use `yield` instead of `return`.
- Execution is paused and resumed on each `yield`, maintaining state between yields.
- They are more memory efficient for large datasets or streams.

[Back to TOC](#Python-Questions)  



## Explain the map function.
The `map()` function iterates over the items of the given iterable(s) and applies the function to each item. It returns a map object (an iterator), which can be easily converted into a list, tuple, etc., using the respective type constructors (`list()`, `tuple()`, etc.).
The function must take as many arguments as there are iterables.
This is a convenient way to perform element-wise transformations and operations on data structures.


### Key Points
- `map()` is useful for applying a function to each element in an iterable.
- It returns a map object, which is an iterator.
- For multiple iterables, the function is applied in a parallel fashion.
- The result can be converted to a list or other iterable types for further use or inspection.

[Back to TOC](#Python-Questions)  


## Explain what init py does
 _init_.py is a file in Python that data scientists use to mark directories as Python packages. It signals to the Python interpreter that a directory contains code for modules and ensures that Python treats directories as modules.
The `__init__.py` file is used in Python to mark directories on disk as Python package directories. If you have a directory containing Python script files and you want to be able to import those modules into other scripts, you need to create an empty file named `__init__.py` in that directory. This file can be empty, or it can contain valid Python code.

Here are the key points about `__init__.py`:

1. **Package Initialization**: The primary purpose of the `__init__.py` file is to initialize Python packages. The presence of `__init__.py` in a directory tells Python to treat the directory as a package, which means you can import modules from that directory into your scripts.

2. **Namespace Management**: `__init__.py` can also be used to define a controlled package namespace. You can use it to selectively import or define symbols (functions, classes, variables, etc.) so that they become accessible directly from the package. For example, if your package `mypackage` has a module `mymodule`, you can import `mymodule` or specific attributes from it into the `__init__.py` file, allowing users to access them directly from `mypackage` without having to import `mymodule` explicitly.

3. **Simplifying Imports**: By using `__init__.py`, you can make your package's interface cleaner and more accessible to users. For instance, instead of having users import functions from deeply nested modules, you can import these functions into `__init__.py`, allowing users to import them directly from the package.

In summary, the `__init__.py` file serves several important functions in Python packages, including package initialization, namespace management, and making packages easier to use and import from. Despite the changes in Python 3.3 and later, `__init__.py` remains a useful and commonly used feature of Python packages.
Help with module importation from various parts of the code. This helps in the finance industry, when data scientists need to organize financial models, and in healthcare, when organizing medical records. 

[Back to TOC](#Python-Questions)  


## Reduce function
The `reduce` function in Python is part of the `functools` module and is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in the `functools` module, and we need to import it using `from functools import reduce` if we want to use it.

The `reduce` function, in essence, reduces a list or sequence into a single value by applying a binary function cumulatively to the items of the sequence, from left to right.

### Syntax
```python
reduce(function, iterable[, initializer])
```

- `function`: This is a function that takes two arguments and returns a single value. The function is applied to the items in the iterable.
- `iterable`: This is the sequence of items to reduce.
- `initializer`: (Optional) This is a value that is used as the initial value to start the reduction. If the initializer is provided, it is placed before the items of the sequence in the calculation, and serves as a default when the iterable is empty. If not provided, the first item in the iterable will be used as the initial value.

### How It Works
The `reduce` function takes the first two elements A and B in the iterable and applies the function to them to get the result, which we can call C. Then it takes C and applies the function to it and the next element in the iterable, and this process continues until there are no more elements left, resulting in a single cumulative value.

### Example
Here's an example of how to use `reduce` to calculate the factorial of a number:

```python
from functools import reduce

def multiply(x, y):
    return x * y

# Calculate the factorial of 5
numbers = range(1, 6)  # This will generate a sequence of numbers from 1 to 5
factorial = reduce(multiply, numbers)

print(factorial)
```

Output:
```
120
```

In this example, `reduce` applies the `multiply` function to the first two elements of the `numbers` sequence (1 and 2), resulting in 2. Then it applies `multiply` to the result (2) and the next element (3), resulting in 6, and so on until it processes the last element, resulting in the factorial of 5.

### Key Points
- `reduce` is not a built-in function; it needs to be imported from the `functools` module.
- It applies a function of two arguments cumulatively to the items of an iterable.
- It reduces the iterable to a single cumulative value.
- An optional initializer can be provided.
- Can be used with any function that takes two arguments and returns a single value. This makes it incredibly versatile and suitable for a wide range of tasks, including but not limited to concatenating strings, merging data structures, or computing custom aggregations.
- Simplifies Code
- More efficient than equivalent code written with explicit loops, especially with functions that are optimized for fast execution.

[Back to TOC](#Python-Questions)  


## filter function

`filter()` calls the provided function for each item in the iterable, and only includes the item in the result if the function returns `True`. The result is a `filter` object, which is an iterator that lazily produces the filtered values as you loop over them. This means that the entire list is not generated in memory at once, but rather element-by-element as you iterate.

### Advantages of Using `filter`

1. **Readability**: `filter` makes the code cleaner and more readable by abstracting away the mechanics of looping and conditionally adding items to a new list.

2. **Efficiency**: The returned `filter` object is an iterator, which means that it does not produce the list of results all at once. This can save memory and potentially increase performance for large datasets.

3. **Functional Programming Style**: `filter` encourages a functional programming style, leading to more declarative code that specifies what you want to achieve rather than how to achieve it.

4. **Versatility**: It can be used with any iterable, not just lists, making it a versatile tool for filtering data.

5. **Composability**: Functions like `filter` can be combined with other functional programming tools like `map` and `reduce` to perform complex data transformations and aggregations in a concise manner.

[Back to TOC](#Python-Questions)  


## Could you explain whether all memory gets freed when Python exits?

When Python exits, whether all memory gets freed depends on the environment and how Python is being run. In general, modern operating systems (like Windows, macOS, and Linux) are very good at reclaiming memory allocated by programs once they terminate. Here's a more detailed breakdown:

### Memory Managed by Python

Python uses a garbage collector to manage memory automatically. This means that during the execution of a Python program, the garbage collector will periodically look for Python objects that are no longer in use and reclaim their memory. However, this is during the lifetime of the program.

### At Python Exit

When a Python program exits, the Python runtime environment will attempt to clean up by:

1. **Closing open resources**: This includes file handles, network connections, and database connections. Python tries to close these properly to avoid data corruption or leaks.

2. **Garbage collection**: Python will perform a final pass of garbage collection to clean up Python objects.

3. **Freeing memory**: Memory that was allocated to Python objects is marked for release back to the operating system.

### Operating System's Role

Once the Python process terminates, the operating system takes over. Modern operating systems are designed to reclaim all resources allocated to a process once it ends. This includes memory, file handles, and other resources. So, from the perspective of the operating system, all memory allocated to the Python process should be freed upon its termination.

### Caveats

- **Memory Leaks**: If the Python program interfaces with external libraries (especially C libraries) through extensions or FFI (Foreign Function Interface), and those libraries allocate memory, it's up to those libraries to properly manage that memory. If they don't, there could be memory leaks. However, when the process terminates, the operating system should still reclaim this memory.
  
- **Subprocesses**: If your Python program spawns subprocesses and doesn't wait for them to terminate, those subprocesses might continue running beyond the lifetime of the parent Python process. Memory used by these subprocesses would not be freed when the Python process exits.

- **Embedded Python**: If Python is embedded in another application, the memory management might depend more on the host application's behavior rather than Python's own memory management mechanisms.

### Conclusion

In most cases and environments, you can expect that all memory allocated to a Python process will be freed upon its exit, thanks to the combination of Python's own cleanup efforts and the operating system's management of process resources. However, specific scenarios involving external libraries, subprocesses, or embedded Python might require additional consideration.

[Back to TOC](#Python-Questions)  










































































































