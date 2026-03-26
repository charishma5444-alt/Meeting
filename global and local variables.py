'''#1.variables inside and outside the function is called global and local variables
2. a variable define above the function and is accesible to the entire global space is called global variable
3. a variable inside the function is called local variable'''


#GLOBAL AND LOCAL VARIABLES
#FIRST CASE OF GLOBAL VARIABLES

a=4
def check():
    print("inside value is",a)
check()
print("outside value is",a)
