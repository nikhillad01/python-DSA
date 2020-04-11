class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):

        # Append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def iterate_item(self):
        # Iterate the list.
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val


if __name__ == '__main__':
    # Start with the empty list
    # llist = LinkedList()
    #
    # llist.head = Node('first')
    # second = Node(2)
    # third = Node(3)
    #
    # llist.head.next = second;  # Link first node with second
    # second.next = third;  # Link second node with the third node
    items = LinkedList()
    items.append_item('PHP')
    items.append_item('Python')
    items.append_item('C#')
    items.append_item('C++')
    items.append_item('Java')

    # items.iterate_item()
    for val in items.iterate_item():
        print(val)
