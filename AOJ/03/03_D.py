i, b, c=(int(x) for x in input().split())
count=0
while i<=b:
    if c%i == 0:
        count += 1
    i +=  1
print(count)   
    