while True:
    n,x=map(int,input().split())
    if n==0 and x==0:
        break
    ans=0
   #組み合わせが重複しないようにする
   #range関数は１からnまでを定義したい時は（1,n+1)
    for a in range(1,n+1):
        for b in range(a+1, n+1):
            for c in range(b+1, n+1):
                if a+b+c == x:
                     ans +=1
    #ansの定義をした行に合わせる＊while True ではない場合も考慮
    print(ans)
