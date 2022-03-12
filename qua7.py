def weight():
    bmi = int(input("enter no"))
    if bmi<=18.5:
        print("underweight")
    elif bmi>18.5 and bmi<=25.5:
        print("normal")
    elif bmi>25.5 and bmi<=30.0:
        print("overweight")
    elif bmi>30:
        print("obese")
weight()  