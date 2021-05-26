import collections
class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(Node)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = Node(key=key, value=value)
            return
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = Node(key=key, value=value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            if p.next is None:
                break
            p = p.next


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        self.table[index] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)