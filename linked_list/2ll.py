#!/usr/bin/env python

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.end= hew_node
        #new_node.next = self.head
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

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
        current_node = self.end
        while current_node:
            print(current_node.data, end=' <=> ' if current_node.prev else '\n')
            current_node = current_node.prev

ll = LinkedList()
ll.append(234)
ll.append(89)
ll.append('sdgfg')
ll.show()
ll.prepend([123])
ll.show()