while True:
    x,y=(int(a) for a in input().split())
    if  x == 0 and y == 0: 
      break
    if x <= y :
          print(x,y)
    else : 
        print(y,x)