import csv 
class verif:
    def verify(self,uname,mail):
        with open ( 'users.csv','r',newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                if row['uname'] == uname and row['email'] == mail:
                    print("user sucessfully verified ")
                    return 1
                    
        return 0
