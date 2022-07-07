import re

phone = input()
phone = re.sub('^00','+',phone)
print(phone)