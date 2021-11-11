class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_length(first):
    if first.value == None:
        return 0
    current = first
    count = 1
    while current.next is not None:
        count += 1
        current = current.next
    return count

def print_list(first):
    current = first
    while current is not None:
        print(current.value)
        current = current.next

def get_by_index(first, index):
    current = first
    while index != 0:
        index -= 1
        current = current.next
    return current.value

first = Node(0)
current = first
for i in range(4, 11):
    current.next = Node(i)
    current = current.next
print_list(first)
print()
print(get_by_index(first, int(input())))