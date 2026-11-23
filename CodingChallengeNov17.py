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
    def getJobID(self):
        return self.jobID
    def getName(self):
        return self.name

###test = RepairJob(1,"david","oil change",200)
####test.describe()
class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self,item):
        self.list.append(item)
    def dequeue(self):
        done = self.list.pop(0)
        return done 
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
                job = RepairJob(int(values[0]),values[1],values[2],float(values[3]))
            jobs.append(job)
    return jobs
job_queue = Queue()
done_stack = Stack()

jobboss = load_jobs('jobs.txt')

rack = [["", "", "", ""],
        ["", 199, "", ""],
        ["", "", "", ""]]

for i in range(0,3):
    job_queue.enqueue(jobboss[i])

for i in range(0,3):
    done_stack.push(job_queue.dequeue())
    print("Finished: " + done_stack.peek().describe())

print('Reopened: ' + done_stack.pop().describe())

def park(list,jobID):
    for i in range(len(list)):
        for x in range(len(list[i])):
            if list[i][x] == "":
                list[i][x] = jobID
                return str(jobID) + ' --> ' + '(' + str(i) +"," +str(x) + ')'
    print("Rack is full!")
    return False
def count(list):
    freeSpots = 0
    for i in range(len(list)):
        for x in range(len(list[i])):
            if list[i][x] == "":
                freeSpots +=1
    return 'Free spots: ' + str(freeSpots)

print(count(rack))
for i in jobboss:
    print(park(rack,i.getJobID()))
print(rack)

print(count(rack))

def binarySearch(list,target):

    (left,right) = 0, len(list)-1
    while left<=right:
        middle  = (left+right)//2
        if list[middle].getJobID() == target:
            return list[middle]
        elif target < list[middle].getJobID():
            right = middle-1
        elif target > list[middle].getJobID():
            left = middle+1
    return None

def nameIndexJob(list,name):
    foundJobs = []
    for i in list:
        if i.getName() ==name:
            foundJobs.append(i.describe())
    return foundJobs

def sortByPrice(list):
    sortedList = list
    

print(nameIndexJob(jobboss,'Milan'))

found_job = binarySearch(jobboss,201)

"""if found_job is not None:
    print("Found:", found_job.describe())
else:
    print("Job not found")"""

"""print(park(rack,done_stack.peek().getJobID()))
print(rack)"""


"""
    1) The reason that the services are stored in a tuple and the jobs are stored in a list is because 
    the number of services is static, because it does not change, however the number of jobs grows over time
    as more people apply for repairs. So a list allows the jobs list to grow over time and the tuple allows me to store
    data that does not need to grow. 
    2) A queue is the right structure for the workshop because it will make sure that the first item is always the item that has been waiting the longsest.
    This will make sure that people will wait for as little time as possible, because whoever has been waiting the longest will be tended to first. 
    A stack is the right structure for the last finished job because it makes it very easy for people to reverse actions that have just been done, like 
    reopening a job 
"""


    

