# -*- coding: utf-8 -*-
"""Prime Numbers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pQ_IXgP-CYKrt5P_vIZdUn9NBKeGXDzq
"""

b = int(input("Please input the beginning of interval: "))
e = int(input("Please input the end of interval: "))
for i in range(b, e+1):
  if i > 0:
    for k in range(2,i):
      if i%k == 0:
        break
    else:
      print(i)

