from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: Optional[ListNode],list2: Optional[ListNode])-> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2



p = Solution()
# list1 = [1,2,4]
# list2 = [1,3,4]

list1 = [1,2,4]
list2 = [1,2,4]

v = p.mergeTwoLists(list1,list2)
print(v)

