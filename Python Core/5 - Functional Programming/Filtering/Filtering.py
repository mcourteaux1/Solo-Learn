names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

res = list(filter(lambda x: len(x)>5, names))
print(res)