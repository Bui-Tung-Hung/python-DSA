class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None 
    
    def add(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            return self.head 
        newNode.next = self.head 
        self.head = newNode
    def remove(self):
        if self.head is None:
            return 
        elif self.head.next is None:
            return self.head.value
        else:
            answer = self.head.value 
            self.head = self.head.next 
            return answer
    def display(self):
        if self.head == None:
            print("Your linked list is empty!")
            return 
        current = self.head 
        while current != None:
            print(current.value, end=" ")
            current = current.next

linkedlist = LinkedList()
linkedlist.add(2)
linkedlist.add(5)
linkedlist.add(7)
linkedlist.add(9)
linkedlist.remove()
linkedlist.remove()
linkedlist.display()