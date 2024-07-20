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
        def linked_list_to_number(node):
            num = 0
            place = 1
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num
        
        def number_to_linked_list(num):
            dummy = ListNode(0)
            current = dummy
            if num == 0:
                return ListNode(0)
            while num:
                current.next = ListNode(num % 10)
                num //= 10
                current = current.next
            return dummy.next
        
        num1 = linked_list_to_number(l1)
        num2 = linked_list_to_number(l2)
        
        total = num1 + num2
        
        return number_to_linked_list(total)

# Helper function to create a linked list from a list of numbers
def create_linked_list(numbers):
    dummy = ListNode(0)
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end='->' if node.next else '')
        node = node.next
    print()



# testcases
l1 = create_linked_list([2, 4, 3])  # represents 342
l2 = create_linked_list([5, 6, 4])  # represents 465

sol = Solution()
result = sol.addTwoNumbers(l1, l2)
print_linked_list(result)  # Output should be 7 0 8 (which represents 807)

list1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])  # represents 9999999
list2 = create_linked_list([9, 9, 9, 9])  # represents 9999
result = sol.addTwoNumbers(list1, list2)
print_linked_list(result)  # Output should be 8 9 9 9 0 0 0 1 (which represents 10000098)

list1 = create_linked_list([0])  # represents 0
list2 = create_linked_list([0])  # represents 0
result = sol.addTwoNumbers(list1, list2)
print_linked_list(result)  # Output should be 0 (which represents 0)
