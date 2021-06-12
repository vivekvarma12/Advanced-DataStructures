class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    def printing(self):
        if self.left:
            self.left.printing()
        print(self.data, end=" ")
        if self.right:
            self.right.printing()
    def search(self, data):
        print(self.data)
        if data < self.data:
            if self.left is None:
                print("Sorry buddy, not in the list...!")
            return self.left.search(data)
        elif data > self.data:
            if self.right is None:
                print("Sorry buddy, not in the list...!")
            return self.right.search(data)
        else:
            print("Found....!")


root = Node(8)
root.insert(1)
root.insert(9)
root.insert(3)
root.insert(10)
#root.insert(5)
#root.insert(6)
root.printing()
root.search()


