x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
z=int(input("Enter z value:"))

if x>y and x>z:
    print("x is greater than remaining two values")
elif y>z:
    print("y is greater than remaining two values")
else:
    print("z is greater than remaining two values")

# Flow control of Student subject marks using input values
math = int(input("Enter your maths marks:"))
sci = int(input("enter your sci marks"))
kan = int(input("enter you kannada marks"))

a=(math+sci+kan)/3
i=int(a)
print("the total average 3 subjects are:", i,"%")
if i>90 and i<=100:
    print("A")
elif i>80 and i<=90:
    print("A")
elif i>60 and i<=80:
    print("B+")
elif i>50 and i<=60:
    print("B")
elif i>=30 and i<=35:
    print("C+")
elif i<35:
    print("fail")

