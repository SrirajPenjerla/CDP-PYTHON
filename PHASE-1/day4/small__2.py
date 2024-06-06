def sec(list,min,sec_small):
    for i in range(len(list)):
        if min>list[i]:
            sec_small=min
            min=list[i]
    return min,sec_small
mylist=[22,-1,42,65,1,-4,6]
min=mylist[0]
sec_small=mylist[1]
small,seco=sec(mylist,min,sec_small)
print("second smalest num:: ",seco)