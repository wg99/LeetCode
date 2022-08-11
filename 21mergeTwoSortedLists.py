class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    newList = ListNode()
    head = newList
    while list1 or list2:
        l1val = list1.val if list1 else float('inf')
        l2val = list2.val if list2 else float('inf')
        if l1val < l2val:
            newList.next = ListNode(list1.val)
            list1 = list1.next
        else:
            newList.next = ListNode(list2.val)
            list2 = list2.next
        newList = newList.next
    return head.next
