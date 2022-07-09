text = input()
word = input()

def search(x,y):
    if y in x:
        print('Word found')
    else:
        print('Word not found')

search(text, word)