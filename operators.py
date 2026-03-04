Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=9
b=8
print(a+b)
17
print(a-b)
1
print(a*b)
72
print(a//b)
1
print(a/b)
1.125
print(a%b)
1
#asignment operator
a=3
b=6
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
9
a-=b
b
6
a
3
a*=8
a
24
a//=b
a
4
a/=b
a
0.6666666666666666
a**=b
a
0.08779149519890257
a%=b
a
0.08779149519890257
#comparision
a=3
b=8
a<b
True
b>a
True
a<=b
True
b>=a
True
a>=b
False
a==b
False
b==a
False
b<=a
False
#logical
a=6
b=9
a<b and a>b
False
a<=b and a>=b
False
a<=b and b>=a
True
a<b or b>a
True
a<=b or b>=a
True
a!=b or b!=a
True
a<b not b>a
SyntaxError: invalid syntax
a>b not a<b
SyntaxError: invalid syntax
# identify
a=3
if type (a) is int
SyntaxError: expected ':'
if type(a) iws int:
    
SyntaxError: invalid syntax
iof type(a) is int:
    
SyntaxError: invalid syntax
if type(a)
SyntaxError: expected ':'
 is int:
     
SyntaxError: unexpected indent
if type(a) is int:
    print ("it is int")

    
it is int
if type(a) is float
SyntaxError: expected ':'
if type(a) is float:
    print("it is float")

    

if type
SyntaxError: expected ':'
if type(a) is not float:
    print("it is int")

    
it is int
#membership
s=1,3,5,7,9
if 3 is in a:
    
SyntaxError: invalid syntax
if 3 in a:
  print(3)

  
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    if 3 in a:
TypeError: argument of type 'int' is not a container or iterable
if 3 in s:
    print(3)

    
3
#bitwisw
#bitwise
a=8
b=7
a&b
0
bin(8)
'0b1000'
bin(7)
'0b111'
a=9
b=7
a&b
1
a=5
b=7
a&b
5
>>> bin(5)
'0b101'
>>> bin(7)
'0b111'
>>> a=6
>>> a=2
>>> b=8
>>> a|b
10
>>> a=9
>>> b=8
>>> a|b
9
>>> a=5
>>> b=9
>>> a^b
12
>>> a=7
>>> b=9
>>> a^b
14
>>> a=1
>>> b=4
>>> a^b
5
