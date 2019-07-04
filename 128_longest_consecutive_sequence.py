def longestConsecutive(self, num):
    sett,past,longest=set(num),set(),0
    for number in sett:
        if number in past:
            continue 
        else:
            past.add(number)
        count,left,right=1,number-1,number+1
        while left in sett:
            past.add(left)
            count,left=count+1,left-1
        while right in sett:
            past.add(right)
            count,right=count+1,right+1
        longest=max(longest,count)
    return longest