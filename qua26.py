def fizz(buzz):
    if buzz%3==0 and buzz%5==0:
        print("fizzbuzz")
    elif buzz%3==0:
        print("fizz")
    elif buzz%5==0:
        print("buzz")
        
user=int(input("enter no"))
fizz(user)

    