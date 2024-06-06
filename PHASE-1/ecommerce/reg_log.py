import csv
class RandL:
    def Register(self,uname,pas,email,city,phnno):
        self.uname=uname
        self.pas=pas
        self.email=email
        self.city=city
        self.phno=phnno
        with open('users.csv','a',newline="") as file:
            w=csv.writer(file)
            w.writerow([self.uname,self.pas,self.email,self.city,self.phno])
        print("Registration sucess full ")
        
    def login(self,uname,pas):
        with open('users.csv','r',newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                if row['uname'] == uname and row['pas'] == pas:
                    return 1
        return 0
                

