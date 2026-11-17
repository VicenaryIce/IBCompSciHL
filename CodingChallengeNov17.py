services = ['flat tyre','brakes','gears','full service']


class RepairJob:
    def __init__(self,jobID,name,service,price):
        self.jobID = jobID
        self.name = name
        self.service = service
        self.price = price
    def describe(self):
        self.description = "#"+str(self.jobID)+" "+self.name+" - "+self.service + " " +"("+str(self.price)+')'
        return self.description

###test = RepairJob(1,"david","oil change",200)
####test.describe()
class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self,item):
        self.list.append(item)
    def dequeue(self):
        self.list.pop(0)
    def front(self):
        return self.list[0]
    def isEmpty(self):
        if len(self.list) > 0:
            return False
        else:
            return True 

class Stack:
    def __init__(self):
        self.list = []
    def push(self,item):
        self.list.append(item)
    def pop(self):
        return self.list.pop(-1)
    def peek(self):
        return self.list[-1]
    def isEmpty(self):
        if len(self.list)>0:
            return False
        else:
            return True



def load_jobs(filename):
    jobs = []
    with open(filename,'r') as file:
        for line in file:
            values = line.strip().split(',')
            if values[2] not in services:
                print("Skipped: " +str(RepairJob(values[0],values[1],values[2],values[3]).describe()))
                continue
            else:
                job = RepairJob(values[0],values[1],values[2],values[3])
            jobs.append(job)
    return jobs
job_queue = Queue()
done_stack = Stack()

jobboss = load_jobs('jobs.txt')

for i in range(0,4):
    job_queue.enqueue(jobboss[i])
    print(job_queue[i])

