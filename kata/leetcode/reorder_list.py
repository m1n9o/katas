import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def init_list(self, data):
        self.head = ListNode(data[0])

        head = self.head
        p = self.head

        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head

    def print_list(self, head):
        p = head
        while p:
            print(p.val)
            p = p.next

    def push_in_list(self):
        result = []
        p = self.head
        while p:
            result.append(p.val)
            p = p.next
        return result


def length_of_linked_list(node):
    count = 0
    while node:
        count += 1
        node = node.next
    return count


class Solution:
    def reorderList(self, head: ListNode) -> None:
        length_of_left_list = math.ceil(length_of_linked_list(head) / 2)
        # 1. divide it into two linked list
        p = head
        while length_of_left_list - 1 > 0:
            p = p.next
            length_of_left_list -= 1

        head_of_right_list = p.next
        p.next = None

        # 2. revert second linked list
        head_of_right_list = self.reverseList(head_of_right_list)

        # 3. insert each ele
        p = head
        q = head_of_right_list
        while q:
            temp = p.next
            if q:
                next_ele = q.next
            else:
                next_ele = None
            q.next = temp
            p.next = q

            p = temp
            q = next_ele

        return p

    @staticmethod
    def reverseList(head):
        if head is None or head.next is None:
            return head
        current = head
        pre = None
        while current:
            head = current
            tmp = current.next
            current.next = pre
            pre = current
            current = tmp
        return head


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.init_list(data=[1, 2, 3, 4])

    Solution().reorderList(linked_list.head)
