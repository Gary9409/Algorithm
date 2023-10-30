class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val=0):
        if self.head is None:
            self.head = ListNode(val, None)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = ListNode(val, None)

    def print_node(self):
        if self.head is None:
            return
        node = self.head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        print(arr)