trump_cards=[(s,n) for s in['S','H','C','D']for n in range(1,14)]
a=int(input())
cards=[]
for _ in range(a):
    egara,num=input().split()
    num=int(num)
    cards.append((egara,num))
for card in trump_cards:
    if card not in cards:
       print(*card)