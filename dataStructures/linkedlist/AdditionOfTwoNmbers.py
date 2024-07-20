# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy

        carry =0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1+v2+carry
            carry = val//10
            val = val % 10
            current.next = ListNode(val)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        

def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_linked_list(lst):
    while lst:
        print(lst.val, end='->'if lst.next else '')
        lst = lst.next
    print()


l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = Solution().addTwoNumbers(l1, l2)
print_linked_list(result)

list1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
list2 = create_linked_list([9, 9, 9, 9])
result = Solution().addTwoNumbers(list1, list2)
print_linked_list(result)

list1 = create_linked_list([0])
list2 = create_linked_list([0])
result = Solution().addTwoNumbers(list1, list2)
print_linked_list(result)