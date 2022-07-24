try:
    name = input()
    if len(name)<4:
        raise CountError
    else:
        print('Account Created')
    
except:
    print("Invalid Name")