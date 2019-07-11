def searchBigSortedArray(self, reader, target):
    count = target
    while True:
        end = reader.get(count)
        if end > target:
            break
        elif end == target:
            return count
        elif end == 2147483647:
            return -1
        else:
            count += target
    end,start = count,0
    while start+1 < end:
        mid = (start+end)//2
        mid_val = reader.get(mid)
        if mid_val > target:
            end = mid-1
        elif mid_val == target:
            end = mid 
        else:
            start = mid+1
    if reader.get(start) == target:
        return start
    elif reader.get(end) == target:
        return end
    else:
        return -1