Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  4 2021, 13:27:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    10/0
ZeroDivisionError: division by zero
>>> 10/'two'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    10/'two'
TypeError: unsupported operand type(s) for /: 'int' and 'str'
>>> a= int(input())
g
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a= int(input())
ValueError: invalid literal for int() with base 10: 'g'
>>> q=[]
>>> q[1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    q[1]
IndexError: list index out of range
>>> s=''
>>> s[1]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s[1]
IndexError: string index out of range
>>> s[i]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s[i]
NameError: name 'i' is not defined
>>> 