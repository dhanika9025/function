def drive(speed):
    c=0
    po=0
    point=(speed-70)//5
    if speed<=70:
        print("ok")
    elif speed>70 and speed<130:
        print("po",point)
        c=c+point
    elif speed>12:
        print("lice3nse")
speed=int(input("enter no"))
drive(speed)
        
        
          