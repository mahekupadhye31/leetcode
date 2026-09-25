class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)

        while left<=right:
            mid=(left+right)//2
            partitions=1
            total=0
            for n in nums:
                total+=n
                if total>mid:
                    partitions+=1
                    total=n
            
            if partitions>k:
                left=mid+1
            else:
                right=mid-1
        return left