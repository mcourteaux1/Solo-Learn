file = open("/usercode/files/books.txt", "r")

books = file.readlines()
file.close()
print("\n".join(["".join([words[0] for words in book.split()]) for book in books]))

file.close()