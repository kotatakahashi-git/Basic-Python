s=input()
p=input()
#sは円形なので二倍してヒットするようにする
s+=s
if p in s:
	print("Yes")
else:
	print("No")