class MedianFinder:

    def __init__(self):
        self.arr=[]
        self.count=0
    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        n=len(self.arr)
        mid=n//2
        if n%2==1:
            return self.arr[mid]
        else:
            return (self.arr[mid-1]+self.arr[mid])/2