class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        self.min_array = []

    def push(self, x: int) -> None:
        if not self.min_array or x <= self.min_array[-1]:
            self.min_array.append(x)
        self.array.append(x)

    def pop(self) -> None:
        if self.min_array and self.array and self.array[-1] == self.min_array[-1]:
            self.min_array.pop()

        self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.min_array[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()