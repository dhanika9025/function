from xml.dom import minicompat


def generate_range(min,max,step):
    i=min
    k=[]
    while i<=max:
        if step>0:
            k.append(i)
            i=i+step
    print(k)
generate_range(22,10,2)
generate_range(1,10,3)