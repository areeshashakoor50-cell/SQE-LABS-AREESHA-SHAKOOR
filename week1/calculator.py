"""
Simple calculator module for SQE Lab 1
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exp):
    return base ** exp


def is_even(n):
    return n % 2 == 0