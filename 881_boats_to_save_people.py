class Solution:
    def numRescueBoats(self, people: List[int], limit: int):
        if not people:
            return 0
        if len(people) == 1:
            return 1
        people.sort()
        end = len(people) - 1
        start = 0
        result = 0
        while start + 1 < end :
            if people[end] >= limit:
                result += 1
                end -= 1
            # heaviest people lighter that limit:
            elif people[start] + people[end] <= limit:
                result += 1
                end -= 1
                start += 1
            else:#lightest + heaviest > limit 
                result += 1
                end -= 1
        #start + 1 == end or start == end
        if start == end:
            return result + 1
        else:
            return result + 1 if people[start] + people[end] <= limit else result + 2
#cleaner solution from leetcode:
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans