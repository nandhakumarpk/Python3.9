from queue import PriorityQueue

q = PriorityQueue()

num=int(input("Enter the size of the queue: "))
for i in range(num):
    q.put(int(input("Enter the number to be inserted: ")))

while not q.empty():
    next_item = q.get()
    print(next_item)
