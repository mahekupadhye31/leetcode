class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left=1
        right=mountainArr.length()-2
        peak=-1

        while left<=right:
            mid=(left+right)//2
            l=mountainArr.get(mid-1)
            m=mountainArr.get(mid)
            r=mountainArr.get(mid+1)
            if l<m<r:
                left=mid+1
            elif l>m>r:
                right=mid-1
            elif l<m and m>r: 
                peak=mid
                break

        l,r=0,peak
        while l<=r:
            m=(l+r)//2
            if mountainArr.get(m)==target:
                return m
            elif mountainArr.get(m)>target:
                r=m-1
            else:
                l=m+1
        

        l,r=peak+1,mountainArr.length()-1
        while l<=r:
            m=(l+r)//2
            if mountainArr.get(m)==target:
                return m
            elif mountainArr.get(m)>target:
                l=m+1
            else:
                r=m-1
        return -1

        
        