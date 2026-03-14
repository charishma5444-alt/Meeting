Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"name":"cherry","city":"ongole"}
print(a)
{'name': 'cherry', 'city': 'ongole'}
type(a)
<class 'dict'>
a(name)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a(name)
NameError: name 'name' is not defined
a("name")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a("name")
TypeError: 'dict' object is not callable
a["name"]
'cherry'
a["city"]
'ongole'
a.keys()
dict_keys(['name', 'city'])
a.items()
dict_items([('name', 'cherry'), ('city', 'ongole')])
a.values()
dict_values(['cherry', 'ongole'])
a={"month":45,"year"=2027}
SyntaxError: ':' expected after dictionary key
a={"month":45,"year":2027}
a.update{"date":35}
SyntaxError: invalid syntax
>>> a=({"month":45,"year"=2027})
SyntaxError: ':' expected after dictionary key
>>> a=({"month":45,"year":2027})
>>> a.update({"date":23})
>>> a
{'month': 45, 'year': 2027, 'date': 23}
>>> a.update({"date":23,"time":34})
>>> a
{'month': 45, 'year': 2027, 'date': 23, 'time': 34}
>>> a={"fruit":"mango","color":"blue"}
>>> a.setdefault({"year",345})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.setdefault({"year",345})
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
>>> a.setdefault{"year",345}
SyntaxError: invalid syntax
>>> a.setdefault("year",345)
345
>>> a
{'fruit': 'mango', 'color': 'blue', 'year': 345}
>>> a={"user":"charishma","mobileno":567890542,"mailid":"ryhthim345@gmail.com"}
>>> a.pop("user")
'charishma'
>>> a
{'mobileno': 567890542, 'mailid': 'ryhthim345@gmail.com'}
>>> a.popitem()
('mailid', 'ryhthim345@gmail.com')
>>> a
{'mobileno': 567890542}
