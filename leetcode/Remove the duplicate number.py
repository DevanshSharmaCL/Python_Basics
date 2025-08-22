def __init__(self, value, next=None):
    self.value = value
    self.next = next

def RemoveDuplicate(head):
    current = head
    while current and current.next:
        if current.val==current.next.val:
            current.next=current.next.next
        else:
            current=current.next
    return print(head(1,2,3,3,4,4,5))