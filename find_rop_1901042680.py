def find_rop(a, length):
    temp = [0] * length
    return merge_sort(a, temp, 0, len(a) - 1)
    
def merge_sort(a, temp, left, right):
    count = 0
    if right > left:
        mid = (right + left) // 2
        count += merge_sort(a, temp, left, mid)
        count += merge_sort(a, temp, mid + 1, right)
        count += merge(a, temp, left, mid + 1, right)
        
    return count
    
def merge(a, temp, left, mid, right):
    count = 0
    i = left
    j = mid
    k = left
    
    while (i <= mid - 1) and (j <= right):
        if a[i] <= a[j]:
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            count += mid - i
            k += 1
            j += 1
            
    while i <= mid - 1:
        temp[k] = a[i]
        k += 1
        i += 1
        
    while j <= right:
        temp[k] = a[j]
        k += 1
        j += 1
    
    for i in range(left, right):
        a[i] = temp[i]
        
    return count
    
a = [5,3,5,7,34,1,2]
print("number: ", find_rop(a, len(a)))