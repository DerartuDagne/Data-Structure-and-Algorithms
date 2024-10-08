# -*- coding: utf-8 -*-
"""Evaluate an Expression Using a Stack.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16T_gE1ya0YK5QGYeXRVqKFji01KidYx8

#Evaluate an Expression Using a Stack

The code evaluates a postfix expression (Reverse Polish Notation) using a stack. In postfix notation, operators follow their operands, and this allows for straightforward evaluation using a stack data structure.

How It Works:

Initialization:

An empty stack is created to hold operands temporarily as they are processed.
Processing Each Character:

Operands: When an operand (a number) is encountered, it is pushed onto the stack.
Operators: When an operator (+, -, *, /) is encountered, the code performs the following steps:
Pop Operands: Pop the top two operands from the stack. These will be used as the right and left operands for the operation.
Perform Operation: Apply the operator to these operands in the correct order (left operand first, then right operand).
Push Result: Push the result of the operation back onto the stack.
Final Result:

After processing all characters, the stack will contain a single element, which is the result of the postfix expression
"""

def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for char in expression:
        if char in operators:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
        else:
            stack.append(int(char))

    return stack[0]

# Usage
expression = "231*+9-"
print(evaluate_postfix(expression))  # Output: -4