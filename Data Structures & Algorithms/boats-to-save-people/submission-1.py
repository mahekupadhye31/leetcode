class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        taken=set()
        people.sort()
        left=0
        right=len(people)-1
        count=0

        while left<right:
            if people[left]+people[right]<=limit:
                taken.add(left)
                taken.add(right)
                count+=1
                left+=1
                right-=1
            elif people[left]+people[right]>limit:
                right-=1
            # else:
            #     left+=1
        for i in range(len(people)):
            if i not in taken:
                count+=1
        return count