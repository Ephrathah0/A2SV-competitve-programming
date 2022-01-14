class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
            
        while len(self.s2):
            self.s1.append(self.s2.pop())
        self.s1.append(x)

    def pop(self) -> int:
        
        while len(self.s1):
            self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self) -> int:
        while len(self.s1):
            self.s2.append(self.s1.pop())
        return self.s2[-1]
    
    def empty(self) -> bool:
        return len(self.s1) == 0  and 0 == len(self.s2)