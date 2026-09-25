class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        m=len(nums1)
        n=len(nums2)
        
        total_left_size=(m+n+1)//2
        left=0
        right=m

        while left<=right:
            mid=(left+right)//2    #how many we taking from nums1
            j=total_left_size-mid

            l1= nums1[mid-1] if mid>0 else float("-inf")
            l2=nums2[j-1] if j>0 else float("-inf")

            r1=nums1[mid] if mid<m else float("inf")
            r2=nums2[j] if j<n else float("inf")

            if l1>r2 :
                right=mid-1
            elif l2>r1:
                left=mid+1
            else:
                if (m+n)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
        