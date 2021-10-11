class LL:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def insrt_or_append(self, data, pos = None):
        if pos != None:
            c = 1
            while c != pos-1:
                c+=1
                self = self.next
            r =  self.next
            f = LL(data)
            self.next = f
            f.next = r
        else:
            while self.next != None:
                self = self.next
            self.next = LL(data)
            
    def trav(self):
        while self != None:
            print(self.data)
            self = self.next
            
    def reverse(self):
        prev = fwd = None
        while self != None:
            fwd = self.next
            self.next = prev
            prev = self
            self = fwd
        self = prev
        while self != None:
            print(self.data)
            self = self.next
            
s = LL(1)
s.insrt_or_append(2)
s.insrt_or_append(3)
s.insrt_or_append(4)
s.insrt_or_append(5,4)
s.insrt_or_append(6)
s.insrt_or_append(8)
s.insrt_or_append(10, 2)
s.trav()
print("While reversing the order:")
s.reverse()




"""
O/P :
1
10
2
3
5
4
6
8
While reversing the order:
8
6
4
5
3
2
10
1
"""
