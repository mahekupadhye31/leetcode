class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length=mountainArr.length()
        left,right=1,mountainArr.length()-2
        while left<=right:
            mid=(left+right)//2
            l,m,r=mountainArr.get(mid-1),mountainArr.get(mid),mountainArr.get(mid+1)
            if l<m<r:
                left=mid+1
            elif l>m>r:
                right=mid-1
            else:
                break
        
        peak=mid

        l=0
        r=peak
        while l<=r:
            m=(l+r)//2
            if mountainArr.get(m)==target:
                return m
            elif mountainArr.get(m)>target:
                r=m-1
            else:
                l=m+1
        
        l=peak+1
        r=length-1
        while l<=r:
            m=(l+r)//2
            if mountainArr.get(m)==target:
                return m
            elif mountainArr.get(m)>target:
                l=m+1
            else:
                r=m-1
        return -1