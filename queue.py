MAX_ARRAY_SIZE = 100000

class Queue:
    array = [None] * MAX_ARRAY_SIZE
    start = end = 0
    def enqueue(self, a):
        assert not self.isFull(), "オーバーフローが発生しました。"
        self.array[self.end] = a
        if self.end + 1 == MAX_ARRAY_SIZE:
            self.end = 0
        else:
            self.end += 1
    def dequeue(self):
        assert not self.isEmpty(), "アンダーフローが発生しました。"
        if (self.start + 1) == MAX_ARRAY_SIZE:
            self.start = 0
            return self.array[MAX_ARRAY_SIZE - 1]
        else:
            self.start += 1
            return self.array[self.start - 1]
    def isEmpty(self):
        return self.start == self.end
    def isFull(self):
        return self.start == (self.end + 1) % MAX_ARRAY_SIZE

n, q = list(map(lambda x: int(x), input().strip().split()))

queue = Queue()

for i in range(n):
    queue.enqueue(input().strip().split())


sum_time = 0
while not queue.isEmpty():
    name, time = queue.dequeue()
    if int(time) <= q:
        sum_time += int(time)
        print(name + ' ' + str(sum_time))
    else:
        queue.enqueue([name, str(int(time) - q)])
        sum_time += q