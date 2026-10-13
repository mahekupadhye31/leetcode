class MyHashMap:

    def __init__(self):
        self.hashmap=set()

    def put(self, key: int, value: int) -> None:
        for u,v in self.hashmap:
            if u==key:
                self.hashmap.remove((u,v))
                break
        self.hashmap.add((key,value))

    def get(self, key: int) -> int:
        for u,v in self.hashmap:
            if u==key:
                return v
        return -1

    def remove(self, key: int) -> None:
        copy=self.hashmap.copy()
        for u,v in copy:
            if u==key:
                self.hashmap.remove((u,v))


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)