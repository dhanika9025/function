def limit():
    i=0
    sum=0
    while i<=20:
        if i%3==0 and i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
limit()