# FUnction with positional arguments
def cart(product,price):
	print("product is:", product)
	print("price is:", price)
cart("cap",300)

# Function with keyword arguments
def cart(product = "cap", price = 500):
	print("type of the product:", product)
	print("price of the product:", price)
cart()

# Function with postional and keyword arguments
def cart(price, product = "cap"):
	print("type of the product:", product)
	print("price of the product:", price)
cart(price = 600)

# Function with variable length keyword arguments
def m(*x):
	print(x)

m(10,20)


