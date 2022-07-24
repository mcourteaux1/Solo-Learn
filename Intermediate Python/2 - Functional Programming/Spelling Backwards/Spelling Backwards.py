def spell(txt):
    if txt=="": 
        return txt
    else:
        print(txt[len(txt)-1])
        return spell(txt[0:len(txt)-1])
    

txt = input()
spell(txt)