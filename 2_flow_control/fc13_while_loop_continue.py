cart=[10,20,400,500,60]
for value in cart:
	if value==400:
		continue
	print(value)	

x=[10,20,"abhi","renu",400,600,"yes","no"]
for y in x:
	if y=="renu":
		continue
	if y==600:
		break
	print(y)