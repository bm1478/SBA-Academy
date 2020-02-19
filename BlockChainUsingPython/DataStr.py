class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.count = 0
        self.first = None
        self.last = None

    def add(self,obj):
        node = Node(obj)
        if self.count == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.count += 1
        print(str(obj), '가', self.count, '번째 추가되었습니다.')

    def toList(self):
        list = []
        node = self.first
        for i in range(self.count):
            list.append(node.data)
            node = node.next
        return list

    def search(self,data):
        node = self.first
        prevNode = None
        for i in range(self.count):
            if node.data == data:
                return [prevNode,node]
            prevNode = node
            node = node.next

    def remove(self, listNode):
        listNode[0].next = listNode[1].next
        del listNode[1]
        self.count -=1

    def __str__(self):
        list = []
        node = self.first
        for i in range(self.count):
            list.append(node.data)
            node = node.next
        return str(list)

linkedlist = LinkedList()
linkedlist.add('a')
linkedlist.add('b')
linkedlist.add('c')
print(linkedlist.toList())
linkedlist.remove(linkedlist.search('b'))
print(linkedlist)