class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.elements.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.elements.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.elements[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if self.elements else False

# Your MyQueue object will be instantiated and called as such:
x = 5
obj = MyQueue()
obj.push(x)
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()

print(param_2, param_3, param_4)
