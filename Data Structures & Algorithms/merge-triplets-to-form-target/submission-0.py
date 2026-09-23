class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n=len(triplets)
        first,second,third=0,0,0
        i=0
        while i<n:
            if triplets[i][0]<=target[0] and triplets[i][1]<=target[1] and triplets[i][2]<=target[2]:
                first=max(triplets[i][0],first)
                second=max(triplets[i][1],second)
                third=max(triplets[i][2],third)
            i+=1
        return [first,second,third]==target