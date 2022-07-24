tweet = input()

try:
    count = len(tweet)
    if count>42:
        raise CountError('This tweet is too long')
    
except:
    print("Error")
else:
    print("Posted")