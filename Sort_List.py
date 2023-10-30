# https://leetcode.com/problems/sort-list/

from typing import Optional
from structure import LinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # # 일반 배열을 사용할 때와 같은 방법으로 병합 -> 비효율적
        # def merge(h1, h2):
        #     head = p = ListNode()
        #     while h1 and h2:
        #         if h1.val < h2.val:
        #             p.next = h1
        #             h1, p = h1.next, p.next
        #         else:
        #             p.next = h2
        #             h2, p = h2.next, p.next
        #     p.next = h1 if h1 else h2
        #     return head.next

        # 두 연결리스트를 병합
        def merge(h1, h2):
            # h2가 빈 리스트면 h1을 리턴
            if h2 is None:
                return h1

            # h1이 없거나, h1이 h2보다 크다면 두 리스트를 스왑
            elif h1 is None or h1.val > h2.val:
                h1, h2 = h2, h1

            # if문을 거치면 h1의 값이 h2보다 낮아지므로 h1의 다음 노드를 가져와 재귀
            h1.next = merge(h1.next, h2)
            return h1

        # 연결 리스트를 병합 정렬
        def merge_sort(h):
            # 리스트가 없거나 길이가 1이면 그대로 리턴
            if h is None or h.next is None:
                return h

            # 빠른 런너와 느린 런너를 이용해 리스트의 중앙 부분을 찾는다
            slow = fast = h
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            h2, slow.next = slow.next, None

            # 중앙부분을 찾았으면 좌, 우로 나누어 다시 병합 정렬을 시행해주고 최종적으로 병합한다
            return merge(merge_sort(h), merge_sort(h2))

        return merge_sort(head)

lst = LinkedList()
for val in [-1, 5, 3, 4, 0]:
    lst.append(val)
print('LinkedList:')
lst.print_node()

s = Solution()
s.sortList(lst.head)
print('Merge Sorted:')
lst.print_node()
