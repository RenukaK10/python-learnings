# Function with a return statement

def balance():
	return 0
b=balance()

if b==0:
	print("balance is:",b)

elif b<=0:
	print("Balance is:",b)
else:
	print("Balance is:",b)
	

#Function with no return statement but we are assigning it to a variable then it returns None
def m1():
	print("this function is returning nothing")

x=m1()
print(x)

# Function with 2 parameter, hence assigning it to 2 variables 
def m1():
	a=10
	b=20
	return a,b
x,y=m1()
print ("first value is:",x)
print("second value is:",y)

#Function with 3 parameters and assigning it to a single variable which returns a tuple.
def m2():
	a=50
	b=40
	c="renuka"
	return a,b,c
x=m2()
print("all values:",x)
print()

# Function calling assigning to a variable
print("code start")

def f1(a,b):
	print("inside function f1 a b:",a,b)
	#print("addition of two values is:", a+b)
	print("a+b:", a+b)
	return a+b

print("taking x y from input")
x=int(input("enter value 1:"))
y=int(input("enter value 2:"))

print("calling f1")
c=f1(x,y)

print("value of c returned from f1", c)

#addition(10,20)
#addition(x,y)
