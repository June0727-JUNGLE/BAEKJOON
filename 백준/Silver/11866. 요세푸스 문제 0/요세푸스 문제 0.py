class RingQueue:
    def __init__(self, size):
        self.size = size
        self.data = [0] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, value):
        if self.count == self.size:
            raise IndexError("Queue is full")
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("Queue is empty")
        value = self.data[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def rotate(self, k):
        for _ in range(k):
            self.enqueue(self.dequeue())

    def is_empty(self):
        return self.count == 0


def josephus(n, k):
    q = RingQueue(n)
    for i in range(1, n + 1):
        q.enqueue(i)

    result = []
    while not q.is_empty():
        q.rotate(k - 1)
        result.append(q.dequeue())

    return result


n, k = map(int, input().split())
answer = josephus(n, k)

print("<" + ", ".join(map(str, answer)) + ">")
