def calc(x):
    side = (x*4,x*x)
    return side
    

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))