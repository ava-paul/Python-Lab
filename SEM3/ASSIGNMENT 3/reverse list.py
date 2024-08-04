def rev_list(arr):
    rev_arr=[]
    for i in range(len(arr)-1,-1,-1):
        rev_arr.append(arr[i])
    return rev_arr
arr=[4,8,0,1,2,4,6,12]
print(rev_list(arr))
