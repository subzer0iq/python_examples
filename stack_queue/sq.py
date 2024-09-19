#!/usr/bin/env python

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.len = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.len += 1
    
    def pop(self, item):
        if not self.is_empty():
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            self.len -= 1
            return popped_node.value
        else:
            raise IndexError('pop from empty stack')
    
    def peek(self):
        if not self.is_empty():
            return self.head.value
        else:
            rise IndexError('peek from empty stack')

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.len
    
    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' => ' if current_node.next else '\n')
            current_node = current_node.next


class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.len = 0

    def push(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.head.value

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.len
            