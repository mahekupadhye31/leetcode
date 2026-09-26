class CountSquares:

    def __init__(self):
        self.store=defaultdict(int)
        self.lists=[]

    def add(self, point: List[int]) -> None:
        self.store[tuple(point)]+=1
        self.lists.append(point)

    def count(self, point: List[int]) -> int:
        squares=0
        cx,cy=point[0],point[1]
        for x,y in self.lists:
            #diagonal points detected
            if x != cx and y != cy and abs(x-cx)==abs(y-cy):
                if (cx,y) in self.store and (x,cy) in self.store:
                    squares+= (self.store[(cx,y)]*self.store[(x,cy)])

        return squares