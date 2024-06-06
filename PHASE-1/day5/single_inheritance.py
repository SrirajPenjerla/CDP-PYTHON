# --- inhertiance ---
#----- single inheritance -----

class Faculty:
    def __init__(self,fname,dept,id):
        self.fname=fname 
        self.dept=dept
        self.id=id
    def p_info(self):
        print(f"Faculty name::'{self.fname }', department::'{self.dept}', id::'{self.id}'")

o=Faculty("loki","ds",3040)
o.p_info()   
class cse(Faculty):
    pass

o=cse("Ramu","cse",11023)
o.p_info()