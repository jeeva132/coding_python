def check(str1):
    
    if type(str1[0]) == int():
        return 0
    for i in str1:
        if i == '/':
            return 0
        if i == ' ':
            return 0
        
    return 1

print(check('aA1_67'))
        