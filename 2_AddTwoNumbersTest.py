# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, v3=0) -> ListNode:
        l1 = l1 if l1 else ListNode(0)
        l2 = l2 if l2 else ListNode(0)
        value_m = l1.val + l2.val + v3
        if value_m == 0 and l1.next is None and l2.next is None:
            return None

        return ListNode(
            val=value_m % 10, next=self.addTwoNumbers(l1.next, l2.next, value_m // 10)
        )


test_list = [
    # ([[2, 4, 3], [5, 6, 4]], [7, 0, 8]),
    # ([[0], [0]], [0]),
    ([[1], [9]], [0, 1]),
]


s = Solution()
for test in test_list:
    input, output = test
    l1, l2 = input

    def list2Node(lll):
        if len(lll) != 0:
            return ListNode(lll[0], list2Node(lll[1:-1]))
        return None

    assert s.addTwoNumbers(list2Node(l1), list2Node(l2)).val == list2Node(output).val
