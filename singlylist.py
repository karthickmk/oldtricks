class node:
    def __init__(self,data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        pl = self.head
        while pl:
            print(pl.data)
            pl = pl.link

    def inofnode(self,data, search):
        newnode = node(data)
        newnode.link = search.link
        search.link = newnode


    def append(self,data):
        newnode = node(data)

        if self.head is None:
            self.head = newnode
            return
        lastnode = self.head
        while lastnode.link:
            lastnode = lastnode.link
        lastnode.link = newnode
    def prepend(self , data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        if self.head:
            newnode.link = self.head
            self.head = newnode


llist = LinkedList()
llist.append('B')
llist.append("c")
llist.printlist()
print('/////////////////////////////////////')
llist.prepend('A')
llist.printlist()
print('/////////////////////////////////////')
llist.inofnode('d','A')
llist.printlist()
print('/////////////////////////////////////')
