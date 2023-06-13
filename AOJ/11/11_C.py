#サイコロのクラスを作る
class Dice(object):
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
    #同じサイコロであることの定義
    def SameDice(self, anotherDice):
        if self.s1 == anotherDice.s1 and \
           self.s2 == anotherDice.s2 and \
           self.s3 == anotherDice.s3 and \
           self.s4 == anotherDice.s4 and \
           self.s5 == anotherDice.s5 and \
           self.s6 == anotherDice.s6:
            return True
        return False

#実際に数値を代入する
s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice1 = Dice(s1, s2, s3, s4, s5, s6)
s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice2 = Dice(s1, s2, s3, s4, s5, s6)
#回転させて試す
#northに三回　westに三回で一周(ここからは調べた)解釈が合っていないかもしれないです
flag = False
for j in range(6):
    if j % 2 == 0:
        dice2.north()
    else:
        dice2.west()
#3面あってたら自動的に一緒なことが確定する
    for k in range(4):
        dice2.rotate()
        if dice2.SameDice(dice1):
            flag = True
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")
