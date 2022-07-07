file = open("pull_ups.txt")
n = int(input())

list = file.readlines()
print(list[n])

file.close()