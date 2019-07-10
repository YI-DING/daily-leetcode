def kClosestNumbers(self, arr, x, k):
    if not arr or x is None or k in (None,0):
        return []
    start, end = 0, len(arr)-1
    #first the left and right num of x
    while start+1 < end:
        mid = (start+end)//2
        if arr[mid] < x:
            start = mid
        else:
            end = mid
    if arr[start] >= x:
        index = start
    elif arr[end] >= x:
        index = end
    else:
        index = len(arr)
    
    left, right = index-1, index
    result = []
    for _ in range(k):
        if left < 0:
            result.append(arr[right])
            right += 1
        elif right > len(arr)-1:
            result.append(arr[left])
            left -=1
        elif abs(arr[left]-x) > abs(arr[right]-x):
            result.append(arr[right])
            right +=1
        elif abs(arr[left]-x) < abs(arr[right]-x):
            result.append(arr[left])
            left -= 1
        else:
            result.append(arr[left])
            left -= 1
    return result