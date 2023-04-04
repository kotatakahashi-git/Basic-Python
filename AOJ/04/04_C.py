while True:
    a, op, b = map(str, input().split())
    a, b = int(a), int(b)
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a//b)
    else:
        break