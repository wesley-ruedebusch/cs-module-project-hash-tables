class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return cur

            cur = cur.next

        return None  # we did not find the value

    def insert_at_head(self, value):
        # n = Node(value)
        value.next = self.head
        self.head = value

    # def append(self, value):
    #     n = Node(value)
    #     cur = self.head
    #     while cur is not None:
    #         if cur.next is None:
    #             cur.next = n

    #         cur = cur.next

    def delete(self, value):
        cur = self.head

        # Special case for deleting the head
        if cur.value == value:
            self.head = self.head.next
            cur.next = None
            return cur

        # General case
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                cur.next = None
                return cur
            else:
                prev = prev.next
                cur = cur.next

        return None