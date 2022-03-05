#scope
#local
def my_fun():
    x=6
    #print("local x:",x)
    #print("local x:",id(x))
my_fun()    
#print(x)

#global
x=8
def my_fun():
    global x
    x=6
    #print("local x:",x)
    #print("local x:",id(x))
my_fun()    
#print("global x:",x)
#print("global x:",id(x))

#inner function:
def my_fun():
    x=6
    def inner_my_fun():
       print(x)
    inner_my_fun()       
my_fun()       
