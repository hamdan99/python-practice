class Node:
    def __init__(self):
        self.value = 0
        self.next = None


class LinkedList:
    def __init__(self):
        self.fn = None

    def append(self, value):
        temp = self.fn
        if temp is None:
            newNode = Node()
            newNode.value = value
            self.fn = newNode
            return
        while temp.next is not None:
            temp = temp.next
        newNode = Node()
        newNode.value = value
        temp.next = newNode

    def traverse(self):
        temp = self.fn
        if self.fn is None:
            print ("list is empty")
            return
        while temp.next is not None:
            print(temp.value)
            temp = temp.next
        print(temp.value)

    def is_empty(self):
        if self.fn is None:
            return True
        return False

    def length(self):
        temp = self.fn
        counter = 0
        if self.fn is None:
            return 0
        while temp is not None:
            temp = temp.next
            counter += 1
        return counter

    def index(self,value):
        counter = 0
        temp = self.fn
        while temp.value != value:
            temp = temp.next
            counter += 1
            if temp is None:
                print("the the value does not exist")
                return
        return counter

    def remove(self, value):
        temp = self.fn
        if self.fn.value == value:
            self.fn = self.fn.next
            return
        while temp.next.value != value:
            temp = temp.next
            if temp.next is None:
                print("the the value does not exist")
                return
        temp2 = temp.next.next
        temp.next = temp2

    def pop(self):
        temp = self.fn
        if self.fn is None:
            print("there is nothing in the list")
            return
        elif self.fn.next is None:
            temp = self.fn.value
            self.fn = None
            return temp
        while temp.next.next is not None:
            temp = temp.next
        temp2 = temp.next.value
        temp.next = None
        return temp2

    def popPos(self, pos):
        temp = self.fn
        if pos == 0:
            temp3 = temp.value
            self.fn = self.fn.next
            return temp3
        counter = 1
        while counter < pos:
            temp = temp.next
            if temp.next is None:
                print("the the value does not exist")
                return
        temp3 = temp.next.value
        temp2 = temp.next.next
        temp.next = temp2
        return temp3

    def search(self, value):
        temp = self.fn
        while temp.value != value:
            temp = temp.next
            if temp is None:
                return False
        return True

    def insert(self, pos, value):
        temp = self.fn
        if self.length() < pos:
            print("the pos does not exist")
            return
        if pos == 0:
            temp2 = Node()
            temp2.value = value
            temp2.next = temp
            self.fn = temp2
            return
        counter = 1
        while counter < pos:
            temp = temp.next
            # counter += 1
            # if temp is None:
            #
            #     return
        temp2 = Node()
        temp2.value = value
        temp2.next = temp.next
        temp.next = temp2


class Queue:
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        return self.list.popPos(0)

    def is_empty(self):
        return self.list.is_empty()

    def traverse(self):
        self.list.traverse()




queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(7)
queue.enqueue(9)
queue.traverse()

queue.dequeue()
queue.traverse()

print(queue.is_empty())






#
# list = LinkedList()
# list.append(9)
# list.append(13)
# list.append(17)
# list.append(23)
# # list.append(9)
# # list.append(9)
# list.traverse()
# print("")
# # print(list.pop())
# # print("")
# # print(list.is_empty())
# # print (list.length())
# # print(list.index(99))
# # list.remove(9)
# # list.remove(9)
# # print(list.popPos(1))
# print("")
# # print(list.search(13))
# list.insert(100,19)
# list.traverse()

