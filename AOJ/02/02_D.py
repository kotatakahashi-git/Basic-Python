W,H,x,y,r=(int(x) for x in input().split())
if y+r>H or x+r>W or y-r<0 or x-r<0:
    print('No')
else:
    print('Yes')
