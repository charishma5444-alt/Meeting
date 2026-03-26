#keyword and positional arguments
'''def Details(id,name,mailid):
    id=39
    name="cherry"
    mailid="che@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id="35",name="amar",mailid="amar@gmail.com")
Details(id="87",name="ravi",mailid="ravi@gmail.com")
Details(24,"ramu","ramu@gmail.com")
Details("siva","si@gmail.com",54)
Details(name="ravi",id="87",mailid="ravi@gmail.com")'''    
    
'''a=10
b=20
a,b=b,a
print(a,b)
print("a value is",a)
print("b value is",b)'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("a value is",a)
print("b value is",b)'''


'''a=10
b=20
temp=a
a=b
b=temp
print("a value is",a)
print("b value is",b)'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d"%(a,b))'''


#default arguments
'''def grocery(item,price):
    print("item is %s" %item)
    print("item is %d" %price)
grocery("honey",123)'''

'''def grocery(item="ghee",price=234):
    print("item is %s" %item)
    print("item is %d" %price)
grocery()'''

'''def grocery(item,price=980):
    print("item is %s" %item)
    print("item is %d" %price)
grocery("honey")'''

'''def grocery(item="ghee",price):
    #non-def arg follows def arg
    print("item is %s" %item)
    print("item is %d" %price)
grocery(567)'''


'''def bakery(cake_name,price,qty):
    print("cake name is %s" %cake_name)
    print("priceis %d" %price)
    print("qty is %.2f kg" %qty)
bakery("honey cake",500,2)'''


'''def bakery(cake_name="honey cake",price=500,qty=2):
    print("cake name is %s" %cake_name)
    print("priceis %d" %price)
    print("qty is %.2f kg" %qty)
bakery()'''


'''def bakery(cake_name,price=500,qty=2):
    print("cake name is %s" %cake_name)
    print("priceis %d" %price)
    print("qty is %.2f kg" %qty)
bakery("honey cake")'''

'''def bakery(cake_name="honey cake",price,qty):
    #non def arg follows def arg
    print("cake name is %s" %cake_name)
    print("priceis %d" %price)
    print("qty is %.2f kg" %qty)
bakery(560,6)'''

#*arguments(* is used to unpack the elements)

'''a=[3,4,5,6,7,8,9,10]
print(a)
print(*a)
print(type(a))'''

'''b=[2,3,4,5,6,8,9,10,11]
print(b)
print(*b)
print(type(b))'''

'''b={2,3,4,5,6,8,9,10,11}
print(b)
print(*b)
print(type(b))'''

'''a={"name":"jyo","year":2098,"month":6}
print(a)
print(*a)'''

'''a="amarraghu"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10,11,12
print(a)
print(b)
print(c)#error'''

'''a,b,c=2,4,6
print(a)
print(b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10,11,12
print(*a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,10,11,12
print(a)
print(*b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10,11,12
print(a)
print(b)
print(*c)'''

'''a,b,c="amarraghu"
print(a)
print(b)
print(c)#error'''

'''a,*b,c="amarraghu"
print(a)
print(*b)
print(c)'''

'''a,b,*c="amarraghu"
print(a)
print(b)
print(*c)'''

a,b,c="ama"
print(a)
print(b)
print(c)




































































































































































































































































































































































































































































































































































































































































































































































































































