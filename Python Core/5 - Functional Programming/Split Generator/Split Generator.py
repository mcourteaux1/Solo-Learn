txt = input()

def words():
    i = 0
    list1 = txt.split()

    for word in list1:
        yield word
        i+=1

print(list(words()))