import random

a={1:'r',2: 'p',3:'s'}

while True:
	p=input("your choice r/p/s: ")

	c=a[random.randint(1,3)]
	print("your chose:",p," computer chose:",c)

	if(p=='s' and c=='p'):
		print('i won!')
	elif(p=='r'and c=='p'):
		 print('i won!')
	elif(p=='r' and c=='p'):
		 print('i losse!')
	elif(p=='p' and c=='s'):
		 print('i losse!')
	elif(p=='s' and c=='r'):
		 print('i iose!')
	elif(p=='p' and c=='r'):
		 print('i won!')
	else:
		 print('draw') 


