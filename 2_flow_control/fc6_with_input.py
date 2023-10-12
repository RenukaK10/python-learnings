x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
z=int(input("Enter z value:"))

if x>y and x>z:
    print("x is greater than remaining two values")
elif y>z:
    print("y is greater than remaining two values")
else:
    print("z is greater than remaining two values")
