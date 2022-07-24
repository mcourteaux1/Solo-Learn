text = input()
dict = {}
#your code goes here
for x in text:
    count = text.count(x)
    dict.update({x:count})
print(dict)