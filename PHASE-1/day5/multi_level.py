'''
create  a class of name placements which has a func info which displays we have " we have === palcements and counting "
create another class named dept eith func display which will display the names of deot present in the clg 
create a class pragati with the funnc welcome which displlay msg welcome to prgsti eng clg we are glad to have u on board 
this prgati class should also display the details about dept and placements 
'''

class Placements :

    def info(self):
        print("we have 675 palcements and still counting ...")

class dept(Placements):
    def display(self):
        print("::The available departments are::")
        print("cse\tece\tmech\tcivil\tDatasciece")
        
class pragati(dept):
    def welcome(self):
        print(":::welcome to pragati engineering college:::\n:::we are glad to have you on board:::")
        print("::our placemnts ::")
        # self.info()
        # self.display()
        

p1=pragati()
p1.welcome()
p1.info()
p1.display()