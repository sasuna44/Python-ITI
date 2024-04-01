import json

class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if self.is_empty():
            print("queue is empty")
            return -1
        return self.items.pop(0)  
################ task exten
class QueueOutOfRangeException(Exception):
    pass

class newQueue(Queue):
    queues = {}

    def __init__(self, name, size):
        super().__init__()
        self.name = name
        self.size = size
        newQueue.queues[name] = self.__dict__

    def insert(self, value):
        if len(self.items) >= self.size:
            raise QueueOutOfRangeException("The queue is full it cant add new elemts")
        super().insert(value)

    def pop(self):
        if self.is_empty():
            print("queue is empty")
            return -1
        return super().pop()

    @classmethod
    def save(cls, file_name):
        try:
            with open(file_name, 'w') as fileobject:
                json.dump(cls.queues, fileobject, indent=4)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, 'r') as fileobject:
                data = json.load(fileobject)
        except Exception as e:
            print(e)
            return []
        else:
            return data


try:
    q1 = newQueue("queue1", 3)
    q2 = newQueue("queue2", 3)

    q1.insert(10)
    q1.insert(20)
    q2.insert(30)
    q2.insert(40)

    print("queue 1:", q1.items)
    print("queue 2:", q2.items)

    newQueue.save("lab3.json")

    newQueue.load("lab3.json")
    print("Loaded :", newQueue.queues)
except QueueOutOfRangeException as e:
    print("Error:", e)
