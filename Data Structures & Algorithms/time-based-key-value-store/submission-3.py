class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values=self.store[key]
        left=0
        right=len(values)-1
        while left<=right:
            mid=(left+right)//2
            if values[mid][1]==timestamp:
                return values[mid][0]
            elif values[mid][1]>timestamp:
                right=mid-1
            else:
                left=mid+1
        if right == -1:
            return ""

        return values[right][0]