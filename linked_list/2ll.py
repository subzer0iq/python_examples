#!/usr/bin/env python

class Node():
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.end = hew_node
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert(self, after, data):
        current_node = self.head
        while current_node:
            if current_node.data == after:
                new_node = Node(data, current_node.next, current_node)
                if current_node.next:
                    current_node.next.prev = new_node
                current_node.next = new_node
                return
            current_node = current_node.next
        else:
            print(f'{after} value not found')

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.end = new_node
            return
        #current_node = self.head
        self.end.next = new_node
        new_node.prev = self.end
        self.end = new_node
        #while current_node.next:
        #    current_node = current_node.next
        #current_node.next = new_node

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' <=> ' if current_node.next else '\n')
            current_node = current_node.next

ll = LinkedList()
ll.append(234)
ll.append(89)
ll.append('sdgfg')
ll.show()
ll.prepend([123])
ll.show()
ll.insert(89,'aaaa')
ll.show()