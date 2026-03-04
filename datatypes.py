Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=4
type(a)
<class 'int'>
b=8.9
type(b)
<class 'float'>
c=code
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c=code
NameError: name 'code' is not defined. Did you forget to import 'code'?
c="code"
type(c)
<class 'str'>
d="9+8j"
print(d)
9+8j
e="true"
print(e)
true
#integers
int(5)
5
int(7.98)
7
int("hey")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    int("hey")
ValueError: invalid literal for int() with base 10: 'hey'
int(5+4j)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    int(5+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(true)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
#float
float(7)
7.0
float(4.6)
4.6
float("heyy")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float("heyy")
ValueError: could not convert string to float: 'heyy'
float(5+8j)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(5+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(true)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
#string
string(3)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    string(3)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string(6.8)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    string(6.8)
NameError: name 'string' is not defined. Did you forget to import 'string'?
string("good")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    string("good")
NameError: name 'string' is not defined. Did you forget to import 'string'?
str(9)
'9'
str(3.7)
'3.7'
str('cool')
'cool'
str(6+5j)
'(6+5j)'
str(true)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    str(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> str("true")
'true'
>>> #complex
>>> complex(7)
(7+0j)
>>> complex(4.8)
(4.8+0j)
>>> complex("hello")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complex("hello")
ValueError: complex() arg is a malformed string
>>> complex(6+9j)
(6+9j)
>>> complex("true")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex("true")
ValueError: complex() arg is a malformed string
>>> #boolean
>>> bool(8)
True
>>> bool(4.8)
True
>>> b00l('red')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b00l('red')
NameError: name 'b00l' is not defined
>>> bool('red')
True
>>> bool(5+6j)
True
>>> bool(true)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    bool(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> bool('true')
True
