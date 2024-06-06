'''
Create a class  ticket which will be the abstract class inside that create the func book ticket which will be the 
abstarct method and has noting in it .

create a class make my trip which will use the book ticket func from ticket class to take the details such as 
name,phnno,email,journey date and display an img thank u for booking ticket in make my trip

create a class irctc which will use the book ticket func from ticket class to take the same details as make my trip
but in the end it will give an option to the user to select weather it is one way or round trip if user option is 
round trip it again asks the user to enter the reuturn date as well then prints display an img thank u for 
choosin irctc
else 
it prints thnk you choosing irctc

create a class indigo which takes all the details as ircttc and just asks which mode of tramsports u want to go in
train flight or bus 
displays thnk u for choosing indigo

'''
from abc import ABC,abstractmethod
class Ticket(ABC):
    @abstractmethod
    def book_ticket(self):
        pass

class Make_mytrip(Ticket):
    def book_ticket(self,name):
        print(f"welcome  to Make my trip,{name}")
        # name=input("Enter your name :: ")
        phn=int(input("Enter your phone number :: "))
        email=input("Enter your mail id :: ")
        jd=input("Enter the journey date :: ")
        print("-----Thank you for choosing Make My Trip----")
class Irctc(Ticket):
    def book_ticket(self,name):
        print(f"welcome to IRCTC , {name} ")
        phn=int(input("Enter your phone number :: "))
        email=input("Enter your mail id :: ")
        jd=input("Enter the journey date :: ")
        print("enter the type of journey from below")
        n=input("1.single trip\t2.round trip\n")
        n=n.lower()
        if n == "round"or n=="2":
            rd=input("Enter the return journey date :: ")
            print("-----Thank you for choosing IRCTC----")
        else:
            print("-----Thank you for choosing IRCTC----")

class Indigo(Ticket):
    def book_ticket(self,name):
        print(f"welcome to Indigo , {name} ")
        # name=input("Enter your name :: ")
        phn=int(input("Enter your phone number :: "))
        email=input("Enter your mail id :: ")
        jd=input("Enter the journey date :: ")
        print("enter the type of journey from below")
        n=input("1.single trip\t2.round trip\n")
        n=n.lower()
        if n == "round"or n=="2":
            rd=input("Enter the return journey date :: ")
            print("Enter the mode of transport from below ")
            mode=input("1.Train\t2.Bus\t3.Plane\n")
            print("-----Thank you for choosing Indigo---")
        else:
            print("Enter the mode of transport from below ")
            mode=input("1.Train\t2.Bus\t3.Plane\n")
            print("-----Thank you for choosing Indigo---")

o1=Make_mytrip()
o2=Irctc()
o3=Indigo()

o1.book_ticket(input("Enter your name :: "))
o2.book_ticket(input("Enter your name :: "))
o3.book_ticket(input("Enter your name :: "))