# Function with lambda
print("Function with lambda using single parameter")
s= lambda a:a*a
print(s(4))
print()

print("Function with lambda using two parameters")
f = lambda x,y:x+y
result = f(1,2)
print(result)
print()

# map function  uses lambda function in it
print("Map function using lambda function")
without_gst_cost = [100,200,300,400]
with_gst_cost = map(lambda x:x+10,without_gst_cost)

x = list(with_gst_cost)
print("without-gst_item cost:", without_gst_cost)
print()
print("with_gst_cost:",x)
print()

# Filter function using lambda function in it 
print("Filter function using lambda function")
items_cost = [999,888,1110,1200,4000,5867,777]
gt_thousand = filter(lambda x:x>1000, items_cost)

x = list(gt_thousand)
print("eligible for discount:", x)
print()

# Reduce function using lambda function in it
from functools import reduce 
print("Reduce function using lambda function")
items_cost = [111,222,333,444]
total_cost = reduce(lambda x,y:x+y, items_cost)
print(total_cost)