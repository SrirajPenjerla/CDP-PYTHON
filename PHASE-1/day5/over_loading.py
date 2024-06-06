class Arith:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
    
obj=Arith()
# obj.add(10) # will not execute TypeError: Arith.add() missing 2 required positional arguments: 'b' and 'c'
# obj.add(10,20) # typeError: Arith.add() missing 1 required positional argument: 'c'
obj.add(1,3,4)

'''
:::Note:::
compile time polymorphism :
over loading : function is same but functionality id different like + operator can be used for 
both addition and concatination.. 1+2 and "1"+"2"..

only operator overloading is possible in python

over loading of function and constructor  in python is not possible because it only takes the latest func written as the func
it will not remember the before function
'''