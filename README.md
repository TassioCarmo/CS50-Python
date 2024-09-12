# Functions, Variables

- Learn to read a documentation

## Creating Code with Python

- code hello.py to start coding.
- .py is the python format
- write a code for example print("hello, world")
- in the terminal write
- python hello.py

**python is not only a language but also an interpreter**

## Functions

- Functions are verbs or actions let's you do something in the program

### Arguments

- it's an input to a function that somehow influence its behaviour

### Side Effects

- it's something that appears on the screen when a function does something

### Bugs

- is a mistake in a code
- Computers take you literally andif you don't finish your thouights in the way the language expects is not going to work

### Input

- get input from the user
- It always comes as a string

```
input("what is your name")
```
### Return

- return input from the user

### Variable

- Container for some value

```
name = input("what is your name")
```

- = assigns a value to something

### Comments 

- Are notes for yourself in your code

```
# this is a comment
```

### Pseudocode

- express your thoughts succinctly, methodically, algorithmically,
- your intent, a todo list
- breaks a bigger program down into small bite-sized tasks

### print multiple

- concatenation
```
input("hello " + name)
```

- multiple arguments
- when you pass multiple arguments to print, it automatically inserts a space for you.
```
input("hello ", name )
```

### String

- A string, known as a str in Python, is a sequence of text.

### parameters

- what you can pass to a function and what those inputs are called, those are parameters

the difference between parameters and arguments

when you're talking about what you can pass to a function and what those inputs are called, those are parameters. When you actually use the function and pass in values inside of those parentheses, those inputs, those values are arguments. So we're talking about the exact same thing-- parameters and arguments are effectively the same thing, but the terms you use from looking at the problem from different directions. When we're looking at what the function can take versus what you're actually passing into the function. 

- Looking at this documentation, you’ll learn that the print function automatically includes a piece of code end='\n'. This \n indicates that the print function will automatically create a line break when run. The print function takes an argument called end` and the default is to create a new line.

So to make it not jump a line we do it like this

```
name = input("What's your name? ")
print("hello,", end="")
print(name)
```

**positional parameters** positional in the sense that the first thing you pass to print gets printed first. The second thing you pass to print after a comma gets printed second. And so forth. 

**named parameters**. Named SEP, separator, or END, E-N-D for the line ending. Those are named parameters because one, they're optional and you can pass them in at the end of your print statement, but you can also use them by name. 

### Formatting Strings

```
print("hello, \"friend\"")
```

```
print(f"hello, {name}")
```
This f is a special indicator for Python to treat this string a special way,


### Interactive mode 

- You don’t have to use the text editor window in your compiler to run Python code. Down in your terminal, you can run python alone. You will be presented with >>> in the terminal window. You can then run live, interactive code. You could type 1+1, and it will run that calculation. This mode will not commonly be used during this course.


### Integers or int

- In Python, an integer is referred to as an int.
- The use of int(x) is called “casting,” where a value is temporarily changed from one type of variable (in this case, a string) to another (here, an integer).

### Readability Wins

- When deciding on your approach to a coding task, remember that one could make a reasonable argument for many approaches to the same problem.
- Regardless of what approach you take to a programming task, remember that your code must be readable. You should use comments to give yourself and others clues about what your code is doing. Further, you should create code in a way that is readable.

### documentation Round

- round(number[n, ndigits]). Those square brackets indicate that something optional can be specified by the programmer. Therefore, you could do round(n) to round a digit to its nearest integer. Alternatively, you could code as follows:


### Functions in python Def 

- def is short for define

```
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)

```

```

# Create our own function
def hello(to):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)
```

- If you want the value of this parameter by default, if not provided by the programmer, to be equal to "world," you literally do that in the same line you're defining the function.

```
# Create our own function
def hello(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()
```

The following very small modification will call the main function and restore our program to working order:
```
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()
```

### Returning Values

```
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()


```
