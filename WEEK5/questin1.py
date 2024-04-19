class StudentQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student):
        self.queue.append(student)
        print(f"{student} joined the queue.")

    def dequeue(self):
        if not self.is_empty():
            student = self.queue.pop(0)
            print(f"{student} is being served.")
            return student
        else:
            print("Queue is empty. No students to dequeue.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def queue_size(self):
        return len(self.queue)


queue = StudentQueue()

students = ["John", "Alice", "Bob", "Charlie", "Emma"]

for student in students:
    queue.enqueue(student)

print("Queue size:", queue.queue_size())



