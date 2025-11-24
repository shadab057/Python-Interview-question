# what is the meaning of Dynamically typed Language? How to check the type of the data?

# Other languages every variable must declare with data type.
# int a=10;
# float b=10.5;
# char c='A';

# In python we no need to declare the variable with data type.
# Python is a dynamically typed language.
num1 = 10
num2 = 10.5
name = "John"
status = True


# To check the type of the data use type() function.
print(type(num1))   # <class 'int'>
print(type(num2))   # <class 'float'>
print(type(name))   # <class 'str'>
print(type(status)) # <class 'bool'>
print(type(100))    # <class 'int'>

# In python the data type will be assigned during runtime based on the value assigned to the variable.