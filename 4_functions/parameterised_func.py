# Single parameterised funciton with paramter "a" and assigning value to the parameter while funciton caling.
# Value of the parameter can be of either integer, string or float data type

def testing(a):
	print("one parameterised function:",a)
	print(type(a))
	print()	
testing(3777.65)

def testing_1(d):
	print("one parameterised function:",d)
	print(type(d))
	print()
testing_1("renuka")

def testing_2(z):
	print("one parameterised function:",z)
	print(type(z))
	print()
testing_2(50)


# Taking the input of the parameter value from the user
def assign(x):
	print("parameter value", x)
k = input("enter a value")
assign(k)

# 2 parameterised function

def testing(r,b):
	print("two parameter function:",r,b)
testing(10,45)

def addition(c,t):
	print("Addition of 2 values=", (c+t))
addition(100,30)