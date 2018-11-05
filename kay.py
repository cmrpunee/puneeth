a=int(input('type value of a:'))
b=int(input('type value of b:'))
c=int(input('type value of c:'))
if(a>b&a>c):
	print("a is largest b&c")
elif(b>c):
	print("b is largest a&c")
else:
	print("c is largest")