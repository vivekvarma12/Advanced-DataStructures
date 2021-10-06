class LL:
    def __init__(self, data):
        self.data = data
        self.next = None
    def insrt(self, data):
        while self.next != None:
            self = self.next
        self.next = LL(data)
    def trav(self):
        while self!=None:
            print(self.data)
            self = self.next
    def rev(self):
        prev = right = None
        while self != None:
            right = self.next
            self.next = prev
            prev = self
            self = right
        while prev != 0:
            while prev != None:
                print(prev.data)
                prev = prev.next
p = LL(1)
p.insrt(2)
p.insrt(3)
p.insrt(4)
p.insrt(5)
print("Now im traversing thru inserted order in Linked List")
p.trav()
print("Now im traversing in reverse order in Linked List")
p.rev()
