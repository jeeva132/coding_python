def moveHyphen(str):
    if str is None:
        return None
    
    newstr = ''
    for i in str:
        if i == '-':
            newstr = i+newstr
        else:
            newstr +=i
    return newstr
print(moveHyphen('Move-Hyphens-to-front'))