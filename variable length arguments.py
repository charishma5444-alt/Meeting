'''# variable lengths
these are automatically stores in tupple and we use *arguments'''

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6)
d=[3,4,5,7,8,9]
check(*d)
e={2,4,6,8}
check(*e)
f={"name":"manohar","course":"nptel"}
check(*f)'''

'''def check(*a):
    d=1
    print(a)
    print(type(a))
    for i in a:
        if type(i)in (int,float):
            d+=i
            print(d)
check()
check(2,3,4,5)
check(3,5,7,9,3.7)
check(1,3,5,6,7.8,6.5,"manu")'''

#**args(kwargs)
'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],"names":["kamaskhi","meenakshi"],"status":["p","A"]}
check(**details)'''

'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],"names":["kamaskhi","meenakshi","visalakshi"],"status":["p","A","D"]}    
check(details)'''

'''#both*and**usage
def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6,7.8)
final(*data)
details={"idnos":[10,20,30],"names":["kamaskhi","meenakshi","visalakshi"],"status":["p","A","D"]}    
final(**details)
final(*data,**details)'''

'''#chr()
print(chr(75))
print(chr(56))
print(chr("a"))#error
print(ord("D"))'''
'''for i in range(65,91):
     print(chr(i),end=" ")'''

'''for i in range(97,123):
    print(chr(i),end=" ")'''
#ASCII
name=str(input("enter the name: "))
for i in name:
    print(i+"="+str(ord(i)))
    



























































