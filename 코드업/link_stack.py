class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data


print('hello')