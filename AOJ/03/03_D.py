a,b,c=(int(x) for x in input().split())
i = a
count=0
while i<=b:
    if c%i == 0:
        count = count+1
    i =i+1
print(count)   
    