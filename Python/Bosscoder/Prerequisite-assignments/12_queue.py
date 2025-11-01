# Implement a basic queue class with enqueue, dequeue, and isEmpty operations using an array. Include a method to display the current queue contents.
class QueueImpl:
    def __init__(self):
        self.queue = []
        
    def Enqueue(self, value):
        self.queue.append(value)

    def Dequeue(self):
        if self.queue:
            self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) == 0

    def getQueue(self):
        return [str(x) for x in self.queue]


if __name__ == "__main__":
    q = QueueImpl()
    print(q.Enqueue("a"))
    print(q.Enqueue("b"))
    print(q.Enqueue("c"))
    print(q.Dequeue())
    print(q.Dequeue())
    print(q.getQueue())