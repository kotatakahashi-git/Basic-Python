#クラスを作る
class Dice():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
    def east(self):
        prev_s6 = self.s6
        self.s6 = self.s3
        self.s3 = self.s1
        self.s1 = self.s4
        self.s4 = prev_s6
    def west(self):
        prev_s6 = self.s6
        self.s6 = self.s4
        self.s4 = self.s1
        self.s1 = self.s3
        self.s3 = prev_s6
    def north(self):
        prev_s6 = self.s6
        self.s6 = self.s5
        self.s5 = self.s1
        self.s1 = self.s2
        self.s2 = prev_s6
    def south(self):
        prev_s6 = self.s6
        self.s6 = self.s2
        self.s2 = self.s1
        self.s1 = self.s5
        self.s5 = prev_s6
    def rotate(self):
        prev_s2 = self.s2
        self.s2 = self.s4
        self.s4 = self.s5
        self.s5 = self.s3
        self.s3 = prev_s2
 #一緒か確認　11-cをクラスの中に入れる       
    def SameDice(self, anotherDice):
        for i in range(6):
            if i % 2 == 0:
                self.north()
            else:
                self.west()
            for j in range(4):
                self.rotate()
                if self.s1 == anotherDice.s1 and \
                   self.s2 == anotherDice.s2 and \
                   self.s3 == anotherDice.s3 and \
                   self.s4 == anotherDice.s4 and \
                   self.s5 == anotherDice.s5 and \
                   self.s6 == anotherDice.s6:
                    return True
        return False
#数値を代入
dices = []
n = int(input())
for i in range(n):
    s1, s2, s3, s4, s5, s6 = map(int, input().split())
    dices.append(Dice(s1, s2, s3, s4, s5, s6))
#実際に一緒のサイコロがないか調べる
flag = False
for i in range(n):
    j = i+1
    while j < n:
        if dices[i].SameDice(dices[j]):
            flag = True
            break
        j += 1

if flag:
    print("No")
else:
    print("Yes")
