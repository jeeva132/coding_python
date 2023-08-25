# def rotate(arr,k):

#     newk = k%len(arr)
#     newarr = []
#     for i in arr[newk:len(arr)+1]:
#         newarr.append(i)
#         print(newarr)
    
#     for i in arr[:newk]:
#         newarr.append(i)

#     print(newarr[1],newarr[2])
#     return newarr

def rotate(nums, k,indeces):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return [nums[i] for i in indeces]
print(rotate([3,4,5],2,[1,2]))
