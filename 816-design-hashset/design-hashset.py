class MyHashSet:

    def __init__(self):
        self.list=[]

    def add(self, key: int) -> None:
        temp=self.list
        for n in temp:
            if n==key:
                return
        self.list.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.list)):
            if self.list[i]==key:
                self.list.pop(i)
                return
        
    def contains(self, key: int) -> bool:
        for i in range(len(self.list)):
            if self.list[i]==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)