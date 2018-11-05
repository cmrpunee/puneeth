import random
while True:
	a=input("print r to roll the die:")
	if(a=='r'):
		r=random,randint(1,6)
		print(r)
	else:
		print('wrong key')
		exit()