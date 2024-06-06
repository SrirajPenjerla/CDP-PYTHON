class bhAAi:
    def laugh(self):
        print("uhhaha ha hahahahaha")
    def chip(self):
        print("chipi chipi ")
class meme(bhAAi):
    def chip(self):
        super().chip()
        print("chipi chipi chapa chapa dubi dubi daba daba magico mi dubi dubi boom boom boom")
m=meme()
m.laugh()
m.chip()

'''
run time polymorphism:

over riding
we can change the functionality of the function as we want only if we inherit the func
'''