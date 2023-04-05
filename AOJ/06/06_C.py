uni_domi=[[[0for r in range(10)]for f in range(3)]for b in range(4)]
n=int(input())
for i in range(n):
    b,f,r,v = map(int, input().split())
    uni_domi[b-1][f-1][r-1]+=v
#棟ごとに分ける
for b in range(4):
    for f in uni_domi[b]:
        print('',*f)
    #bのが3以外の時に分け目を表示する
    if b!=3:
        print('#'*20)