#write a program to find the sec smallest negative number from the list without sort min and max
#-----------------------------------------------------------------------------------------------#
mylist=[22,-1,42,65,1,-4,6]
mylist=[1,2,4,0]
def sec(list,min,sec_small):
    for i in range(len(list)):
        if min>list[i]:
            min=list[i]
    for i in range(len(list)):
        if list[i] >min and list[i]< sec_small:
            sec_small=list[i]
    return min,sec_small
min=mylist[0]
sec_small=mylist[1]
small,seco=sec(mylist,min,sec_small)
print("second smalest num:: ",seco)