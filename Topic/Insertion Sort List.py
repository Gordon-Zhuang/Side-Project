class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def put(self, head, val_array):
    while val_array:
        head.next = ListNode(val_array.pop(0))
        head = head.next
def insertionSortList(self, head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    array.sort()
    ans = ListNode(array.pop(0))
    while array:
        ans.next = ListNode(array.pop(0))
        ans = ans.next
    return ans


head = ListNode(0)
put(0, head, [4,2,1,3])
head = head.next
ans = insertionSortList(0, head)

while ans:
    print(ans.val)
    ans = ans.next