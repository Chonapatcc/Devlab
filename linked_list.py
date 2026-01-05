class node:
    data = None;
    next_node = None;
    prev_node = None;
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

lst = [int(x) for x in input().split()]

head = None 
tail = None
for item in lst:
    if item == -1:
        break
    
    new_node = node(item)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        new_node.prev = tail
        tail = new_node
x = tail
while x is not None:
    print(x.data, end=' ')
    x = x.prev