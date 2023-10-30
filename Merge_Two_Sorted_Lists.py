# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional
from structure import LinkedList

class Solution:
    # recursive
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        elif not list1 or list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

    # # iterative
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     merge = head = ListNode()
    #     while list1 and list2:
    #         if list1.val <= list2.val:
    #             list1, merge.next, merge = list1.next, list1, list1
    #         else:
    #             list2, merge.next, merge = list2.next, list2, list2
    #     merge.next = list1 if list1 else list2
    #     return head.next

l1 = LinkedList()
for val in [1, 2, 4]:
    l1.append(val)
print('LinkedList 1:')
l1.print_node()

l2 = LinkedList()
for val in [1, 3, 4]:
    l2.append(val)
print('LinkedList 2:')
l2.print_node()

s = Solution()
s.mergeTwoLists(l1.head, l2.head)
print('Merged:')
l1.print_node()