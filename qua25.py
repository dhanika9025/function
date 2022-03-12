def count(list):
    i=0
    c=0
    c1=0
    while i<len(list):
        if list[i]>0:
            c=c+1
        else:
            c1=c1+1
        i=i+1
    print(c,"positive number")
    print(c1,"negative number")
a=[2,-7,5,-64,-14] 
count(a)
    
    
    
    
    
    
    