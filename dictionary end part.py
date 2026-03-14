Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"time":3,"hours":4,"sec":54}
a.copy()
{'time': 3, 'hours': 4, 'sec': 54}
a
{'time': 3, 'hours': 4, 'sec': 54}
a.get()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0
>>> a.get("sec")
54
>>> a
{'time': 3, 'hours': 4, 'sec': 54}
>>> a.clear()
>>> a
{}
>>> a={"name":"satheesh","place":"ramapuram"}
>>> print(a)
{'name': 'satheesh', 'place': 'ramapuram'}
>>> a={"name":"satheesh","place":"ramapuram","name":"mahe"}
>>> print(a)
{'name': 'mahe', 'place': 'ramapuram'}
>>> b={"name":"satheesh","place":"ramapuram","name3":"mahe"}
>>> print(b)
{'name': 'satheesh', 'place': 'ramapuram', 'name3': 'mahe'}
>>> a={"ytre":[23,45,67],"drtyeo":[76,90,87,86]}
>>> a.keys(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.keys(a)
TypeError: dict.keys() takes no arguments (1 given)
>>> a.keys()
dict_keys(['ytre', 'drtyeo'])
>>> a.values()
dict_values([[23, 45, 67], [76, 90, 87, 86]])
>>> a.items()
dict_items([('ytre', [23, 45, 67]), ('drtyeo', [76, 90, 87, 86])])
>>> print(a)
{'ytre': [23, 45, 67], 'drtyeo': [76, 90, 87, 86]}
