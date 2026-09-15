class Node:                              # FIX: LRUCache itself was trying to double as a Node —
    def __init__(self, key, val):        # split them into two separate classes
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        # self.key=key.    these are node attributes
        # self.value=value
        # self.next=None.   this too
        # self.prev=None

        self.head = Node(0, 0)           # FIX: sentinel nodes were missing entirely —
        self.tail = Node(0, 0)           # insert() referenced self.head.next but self.head
        self.head.next = self.tail       # never existed anywhere
        self.tail.prev = self.head
        
    def remove(self,node):
        nextnode=node.next
        prevnode=node.prev
        prevnode.next=nextnode
        nextnode.prev=prevnode
    
    def insert(self,node):
        nextnode=self.head.next
        self.head.next=node
        node.next=nextnode
        nextnode.prev=node
        node.prev=self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node=Node(key,value)
            self.insert(node)
            self.cache[key]=node

        else:
            node=self.cache[key]
            self.remove(node)
            newnode=Node(key,value)
            self.insert(newnode)
            del self.cache[key]
            self.cache[key]=newnode
            
        if len(self.cache)>self.capacity:
            lru=self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

        
