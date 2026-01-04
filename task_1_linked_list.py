class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return self._sorted_merge(left, right)

    def _get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)

        return result


def merge_sorted_lists(list1, list2):
    merged = LinkedList()

    p1 = list1.head
    p2 = list2.head

    if not p1:
        merged.head = p2
        return merged
    if not p2:
        merged.head = p1
        return merged

    if p1.data <= p2.data:
        merged.head = p1
        p1 = p1.next
    else:
        merged.head = p2
        p2 = p2.next

    current = merged.head

    while p1 and p2:
        if p1.data <= p2.data:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next

    if p1:
        current.next = p1
    if p2:
        current.next = p2

    return merged


if __name__ == "__main__":
    print("=== Реверсування списку ===")
    llist = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        llist.append(i)
    print("Оригінальний список:")
    llist.print_list()
    llist.reverse()
    print("Реверсований список:")
    llist.print_list()

    print("\n=== Сортування списку (merge sort) ===")
    unsorted_list = LinkedList()
    for i in [64, 34, 25, 12, 22, 11, 90]:
        unsorted_list.append(i)
    print("Несортований список:")
    unsorted_list.print_list()
    unsorted_list.merge_sort()
    print("Відсортований список:")
    unsorted_list.print_list()

    print("\n=== Об'єднання двох відсортованих списків ===")
    list1 = LinkedList()
    for i in [1, 3, 5, 7]:
        list1.append(i)
    print("Перший відсортований список:")
    list1.print_list()

    list2 = LinkedList()
    for i in [2, 4, 6, 8, 10]:
        list2.append(i)
    print("Другий відсортований список:")
    list2.print_list()

    merged = merge_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    merged.print_list()
