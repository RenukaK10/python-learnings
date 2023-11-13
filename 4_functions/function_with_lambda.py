# Function with lambda
s= lambda a:a*a
print(s(4))
print()

f = lambda x,y:x+y
result = f(1,2)
print(result)

# map function  uses lambda function in it

without_gst_cost = [100,200,300,400]
with_gst_cost = map(lambda x:x+10,without_gst_cost)

x = list(with_gst_cost)
print("without-gst_item cost:", without_gst_cost)
print("with_gst_cost:",x)

# Filter function using lambda function in it 
items_cost = [999,888,1110,1200,4000,5867,777]
gt_thousand = filter(lambda x:x>1000, items_cost)

x = list(gt_thousand)
print("eligible for discount:", x)