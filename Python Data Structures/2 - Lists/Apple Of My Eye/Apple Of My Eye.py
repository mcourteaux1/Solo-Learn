data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]

x = 0
color = input()

if color == 'brown':
  x = 0
elif color == 'blue':
  x = 1
elif color == 'green':
  x = 2
elif color == 'black':
  x = 3

y = sum(data,[])
y = sum(y)

print(int(((data[0][x]+data[1][x])/y)*100))
