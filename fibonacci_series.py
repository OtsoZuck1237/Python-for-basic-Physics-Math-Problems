# -*- coding: utf-8 -*-
"""Fibonacci Series.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ntql-AYM3N-6WkY36xeSRLbF_369fD7T
"""

def fib(n):
  if n<0:
    print("Invalid Input")
  else:
    a = 0
    b = 1
    c = 0
    if n == 1 or n == 0:
      print(a)
    else:
      print(a)
      print(b)
      for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)
fib(0)