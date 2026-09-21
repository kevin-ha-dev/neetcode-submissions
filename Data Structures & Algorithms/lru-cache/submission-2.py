class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            #fetching node from cache
            node: Node = self.cache[key]
            # remove node from current position
            node.prev.next = node.next
            node.next.prev = node.prev
            # move node to front of list right.prev
            prev: Node = self.right.prev
            
            prev.next = node
            node.prev = prev

            node.next = self.right
            self.right.prev = node
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # check if key in cache
        if key in self.cache:
            node: Node = self.cache[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            del self.cache[key]
        # create new node and append to mru and cache
        node: Node = Node(key, value)
        self.cache[key] = node

        # sandwhich node between prev and right
        prev: Node = self.right.prev
        node.next = self.right
        node.prev = prev
        node.prev.next = node
        self.right.prev = node

        # check capacity, if len(cache) > capacity remove LRU and cache value

        if len(self.cache) > self.capacity: 
            lru: Node = self.left.next
            self.left.next = lru.next
            lru.next.prev = self.left

            del self.cache[lru.key]
            
            




