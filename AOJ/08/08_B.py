while True:
    a=input()
    if a=='0':
        break
    #数値→文字列化→map１つを数値としてリスト化して合計を求める(調べました)
    print(sum(list(map(int, str(a)))))
