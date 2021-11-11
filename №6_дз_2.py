class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def len_list(first):
    if first is None:
        return 0
    count = 0
    current = first
    while current is not None:
        current = current.next
        count += 1
    return count

first = Node(0)
current = first
for i in range(1, 10):
    current.next = Node(i)
    current = current.next
print(len_list(first))



