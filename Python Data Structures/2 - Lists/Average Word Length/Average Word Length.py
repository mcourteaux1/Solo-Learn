text = input()
x = text.split()
count = 0
i = 0
while i<len(x):
    count+=len(x[i])
    i+=1
print(count/len(x))