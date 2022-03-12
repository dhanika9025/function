


def letter():
    a=" The Quick Hrow Fox"
    i=0
    c=0
    c1=0
    while i<len(a):
        if a[i]>="a"  and a[i]<="z":
            c=c+1
        if a[i]>="A"  and a[i]<="Z":
            c1=c1+1
        i=i+1
    print("no.of uppercase characters :-",c1)
    print("no.of lowercase character :-",c)
letter()
    
    
    
    
    
    

    
    
    
    
    
    
    
    

        