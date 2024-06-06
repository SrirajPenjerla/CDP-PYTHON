'''create a class F15 with functions  lights fan and ac and display
lights:when lights fuc called it prints the colour of the light which is taken as parameter to the func
Fan: when it is called it diplays reg speed in which it is rotating which is taken as parameter for unc
ac: diplays curr room temp and the out side temp which is taken as input
display: whch diplays the diff in outside temp and room temp of ac  and fan speed'''

class F15:
    def __init__(self,st,et):
        self.st=st 
        self.et=et
        print("Today is a wondeful day !!!")
        # print(f'Class starts st{st} and end at {et}')
    
    def lights(self,colour):
        # self.colour=colour
        print(f'I am a {colour} light !!!')
    def fan(self,speed):
        self.speed=speed
        print(f'Fan is rotating at {speed} speed !!!')
    def ac(self,r_t,o_t):
        self.o_t=o_t
        self.r_t=r_t
        print(f'Room temp is:: {r_t} degrees  and out side temp is :: {o_t} degrees ')
    def display(self):
        print(f'Difference in the temp is {self.o_t-self.r_t} degrees and Fan is rotating at {self.speed} speed !!! ')
        print(f'Class starts at:{self.st}"O clock and end at {self.et}"O clock ')

s=F15(9,4)
s.lights("White")
s.fan(7)
s.ac(25,40)
s.display()