Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="my day is great"
a[9]
' '
a[6]
' '
a[3]+a[4]+a[5]
'day'
c="simple is better than complex"
a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
'y day '
c[1]+c[2]+c[3]+c[4]+c[5]+c[6]
'imple '
c[0]+c[1]+c[2]+c[3]+c[4]+c[5]
'simple'
c[22]+c[23]+c[24]+c[25]+c[26]+c[27]+c[28]
'complex'
d="i am learning python"
d[5]+d[6]+d[7]+d[8]+d[9]
'learn'
d[14]+d[15]+d[16]+d[17]+d[18]+d[19]
'python'
a="my day is great"
a="my day is great"
a[3]
'd'
#negative
h="you are great"
h[-1]+h[-2]+h[-3]+h[-4]+h[-5]
'taerg'
h[-5]+h[-4]+h[-3]+h[-2]+h[-1]
'great'
a="vijayawada is a royal city"
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
a[-4]+a[-3]+a[-2]+a[-1]
'city'
a[-15]+a[-14]
'is'
b="vizag is a city of destiny"
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
b[-15]+b[-14]+b[-13]+b[-12]
'city'
b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'
a="amar raghu"
a[0:4]
'amar'
a[6:10]
'aghu'
a[:7]
'amar ra'
a[6;]
SyntaxError: invalid syntax
a[:]
'amar raghu'
#slicing
c="codegnan it solutions"
c[11:13]
' s'
c[10:12]
't '
c[11:12]
' '
c[10:11]
't'
c[9:11]
'it'
c[13:20]
'olution'
c[12:20]
'solution'
c[4:8]
'gnan'
h="python full stack course"
a[7:11]
'ghu'
h[7:11]
'full'
p="work hard until you succeed"
p[-17:-12]
'until'
p[-27:-23]
'work'
p[-22:-18]
'hard'
p[-11:-8]
'you'
p[-7:]
'succeed'
s="time is very precious"
s[-14:10]
' ve'
s[-14:-10]
' ver'
s[-14:-9]
' very'
a[-8:]
'ar raghu'
s[-8:]
'precious'
#striding
f="data science"
f[::]
'data science'
fr[::1]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    fr[::1]
NameError: name 'fr' is not defined. Did you mean: 'f'?
\
>>> f[::1]
'data science'
>>> f[::4]
'd e'
>>> f[::-1]
'ecneics atad'
>>> n="mechine learning"
>>> n[::4]
'miln'
>>> n[3:9]
'hine l'
>>> n[::6]
'men'
>>> n[::9]
'me'
>>> n[::6]
'men'
>>> n[::7]
'm n'
>>> n[::2]
'mcielann'
>>> n[5:]
'ne learning'
>>> n[::4]
'miln'
>>> n[::8]
'ml'
