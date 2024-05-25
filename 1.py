class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is None:
            return None

        res = self.head
        self.head = res.next
        res.next = None
        return res

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        self.insert_node_at_end(new_node)

    def insert_node_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def reverse(self):
        if self.head is None:
            return self

        head = self.head
        rest = head.next
        head.next = None
        while rest:
            cur = rest
            rest = rest.next
            cur.next = head
            head = cur
        self.head = head

    def sort(self):
        if self.head is None:
            return self

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next

            if sorted_list is None or sorted_list.data > current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                node = sorted_list
                while node.next is not None and node.next.data < current.data:
                    node = node.next

                current.next = node.next
                node.next = current

            current = next_node

        self.head = sorted_list

    def merge(self, list):
        self.sort()
        list.sort()

        host = self
        res = LinkedList()

        host_el = host.pop()
        list_el = list.pop()
        while list_el is not None or host_el is not None:
            if list_el is None:
                res.insert_node_at_end(host_el)
                host_el = host.pop()
                continue

            if host_el is None:
                res.insert_node_at_end(list_el)
                list_el = list.pop()
                continue

            if list_el.data > host_el.data:
                res.insert_node_at_end(host_el)
                host_el = host.pop()
            else:
                res.insert_node_at_end(list_el)
                list_el = list.pop()

        self.head = res.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


def test_linked_list():
    # Test reverse method
    list1 = LinkedList()
    list1.insert_at_end(12)
    list1.insert_at_end(4)
    list1.insert_at_end(6)
    list1.reverse()
    assert list1.pop().data == 6
    assert list1.pop().data == 4
    assert list1.pop().data == 12

    # Test sort method
    list2 = LinkedList()
    list2.insert_at_end(12)
    list2.insert_at_end(4)
    list2.insert_at_end(6)
    list2.sort()
    assert list2.pop().data == 4
    assert list2.pop().data == 6
    assert list2.pop().data == 12

    # Test merge method
    list3 = LinkedList()
    list3.insert_at_end(12)
    list3.insert_at_end(4)
    list3.insert_at_end(6)

    list4 = LinkedList()
    list4.insert_at_end(3)
    list4.insert_at_end(5)
    list4.insert_at_end(7)

    list3.merge(list4)
    assert list3.pop().data == 3
    assert list3.pop().data == 4
    assert list3.pop().data == 5
    assert list3.pop().data == 6
    assert list3.pop().data == 7
    assert list3.pop().data == 12


if __name__ == "__main__":
    test_linked_list()
