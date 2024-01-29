#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    name = "Guido"
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2
print(add(45,55))

def halve(number):
    return number / 2
print(halve(100))

def my_function(param):
    print("Running my_function")
    return param + 1

my_function_return_value = my_function(1)

my_function_return_value