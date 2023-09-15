def findTotalCurtains(no,lst):
    total = 0
    for i in lst:
        if i/12>=1:
            total +=i//12
    return total

no = 5
lst = [3, 42, 60, 6, 14]
print(findTotalCurtains(no,lst))
        