import sys
a=input()
for line in sys.stdin:
    a+=line
a=a.lower()
for char in list("abcdefghijklmnopqrstuvwxyz"):
    print(*[char,":",a.count(char)])
