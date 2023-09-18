str1="manumanumanumalayalammanumanu"
def pali(str1):
    if str1==str1[::-1]:
        return True
    else:
        return False
list1=[]
for i in range(len(str1)):
    for j in range(i+1,len(str1)):
        if pali(str1[i:j]):
            if len(str1[i:j])>1:
                list1.append(str1[i:j])
list2=[]
for i in list1:
    list2.append(len(i))

ind=list2.index(max(list2))
print(ind)
print(list1[ind])