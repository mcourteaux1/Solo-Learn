s = input()

def hashtagGen(text):
	text1 = text.replace(" ", "")
	text2 = '#' + text1
	
	return text2

print(hashtagGen(s))