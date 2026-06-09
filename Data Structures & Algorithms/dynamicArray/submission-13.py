class DynamicArray:
    
    # O(1)
    def __init__(self, capacity: int):
        self.arr = []
        self.cap = capacity

    # O(1)
    def get(self, i: int) -> int:
        return self.arr[i]

    # O(1)
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # O(1)
    def pushback(self, n: int) -> None:
        if (len(self.arr) >= self.cap): self.resize()
        self.arr.append(n)  # Avg / Ammortized O(1)

    # O(n)
    def popback(self) -> int:
        ret = self.arr[-1]
        self.arr = self.arr[:-1]
        return ret
 
    # O(1)
    def resize(self) -> None:
        self.cap *= 2

    # O(1)
    def getSize(self) -> int:
        return len(self.arr)
        
    # O(1)
    def getCapacity(self) -> int:
        return self.cap
