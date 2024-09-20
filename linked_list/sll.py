#!/usr/bin/env python

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.end = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next and (current_node.next.data < data):
            current_node = current_node.next

        # Вставляем новую ячейку после current
        new_node.next = current_node.next
        current_node.next = new_node


    def show(self):
        current_node = self.head.next
        while current_node:
            print(current_node.data, end=' => ' if current_node.next else '\n')
            current_node = current_node.next

ll = LinkedList()
ll.append(234)
ll.append(125)
ll.append(89)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(-5)
ll.append(123)
ll.show()