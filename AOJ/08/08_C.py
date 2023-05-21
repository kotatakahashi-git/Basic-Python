import sys
a=input()
for line in sys.stdin:
    a+=line
a=a.lower()
for str in list("abcdefghijklmnopqrstuvwxyz"):
    print(*[str,":",a.count(str)])