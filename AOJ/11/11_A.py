#サイコロのクラスを作る　
#回転の動きを定義
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
    def top(self):
        return self.s1
#実際の動きを入力
#あらかじめのクラスで分岐
s1, s2, s3, s4, s5, s6 = map(int, input().split())
dice = Dice(s1, s2, s3, s4, s5, s6)
order = input()
for i in order:
    if i == 'N':
        dice.north()
    elif i == 'W':
        dice.west()
    elif i == 'E':
        dice.east()
    elif i == 'S':
        dice.south()
print(dice.top())
    