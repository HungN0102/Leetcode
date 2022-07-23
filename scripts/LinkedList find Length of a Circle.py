class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def get_length(node):
    cycleLength = 0
    current = node
    while True:
        current = current.next
        cycleLength += 1
        if current == node:
            break
    return cycleLength

def find_cycle_start(head):
    slow = head 
    fast = head 
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            cycleLength = get_length(fast)
            break
    
    slow = head
    fast = head
    
    while cycleLength > 0:
        fast = fast.next 
        cycleLength -= 1
    
    while fast != slow:
        fast = fast.next
        slow = slow.next
        
    return slow
    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

main()


get_length(head)