import random

dataArray = []
for _ in range(7):
    dataArray.append(random.randint(1, 100))

node = Node()
node.data = dataArray[0]
head = node
node.link = head
memory.append(node)

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    node.link = head
    memory.append(node)

