n = int(input())

file = open("numbers.txt", "w+")
i = 1
while i<=n:
    file.write(str(i) + '\n')
    i+=1
file.close()


f = open("numbers.txt", "r")
print(f.read())
f.close()