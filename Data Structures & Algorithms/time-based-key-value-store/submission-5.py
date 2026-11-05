class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        #binary search to find the timestamp needed:
        left=0
        right=len(self.store[key])-1
        while left<=right:
            mid=(left+right)//2
            if self.store[key][mid][1]==timestamp:
                return self.store[key][mid][0]
            elif self.store[key][mid][1]>timestamp:
                right=mid-1
            else:
                left=mid+1
        return self.store[key][right][0] if right >= 0 else ""