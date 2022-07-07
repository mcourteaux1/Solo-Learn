#change the function
def adder(x, y, *args):
    print(x+y+sum(args))

adder(2, 3)
adder(2, 3, 4)
adder(1, 2, 3, 4, 5)