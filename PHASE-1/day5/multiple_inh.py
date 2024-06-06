class Marks:
    mth=int(input("enter the maths marks :: "))
    pyth=int(input("Enter the python marks :: "))

class Internals:
    math_int=int(input("enter math internal marks :: "))
    pyth_int=int(input("enter python internal marks :: "))

class res(Marks,Internals):
    
    def res_out(self):
        math_las=self.mth+self.math_int
        pyth_las=self.pyth + self.pyth_int
        if  math_las > 40 :
            print("pass in math")
        elif math_las < 40 :
            print("fail in math")
        if  pyth_las > 40 :
            print("pass in python")
        elif pyth_las < 40 :
            print("fail in python")

r=res()
r.res_out()