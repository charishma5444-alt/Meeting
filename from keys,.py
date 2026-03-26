#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))'''

#print(dict(a))

'''b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"cherry")
print(b)'''

#evaxl()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple collections intlo one 

a=[10,20,30,40,50]
names=["honey","sweety","kittu","bittu"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

d=tuple(zip(a,names))
print(d)

e=set(zip(a,names))
print(e)

f=dict(zip(a,names))
print(f)

#enumerATE()->we can give counter to the collection
'''names=["cherry","uma","mohan","mahe","mahesh"]
for i in range(len(names)):
    print(i,names[i])


b=list(enumerate(names))
print(b)

b=list(enumerate(names,100))
print(b)'''


'''x=int(input("enter rows: "))
for i in range(x):
    for j in range(x):
        print("*", end=" ")
    print()'''

'''y=int(input("enter rows: "))
for i in range(1,y+1):
    print("*"*i)'''

'''k=int(input("Enter the number of rows: "))

for i in range(1,k+1):
    print(" " *(k-i), end="")
    print("* "*i)'''






















    

