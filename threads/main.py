import queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting " + self.name)
        self.process_data()
        print("Exiting " + self.name)


    def process_data(self):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = self.q.get()
                queueLock.release()
                print (self.name+" processing "+data)
            else:
                queueLock.release()


t = 1
nameList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for i in range(t):
    tName = "Thread-"+str(i)
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print ("Exiting Main Thread")
