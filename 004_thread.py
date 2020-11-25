from threading import Thread, Lock

# -- 1. Test thread_call back
def greeting(firstname, lastname):
    print(f"Hi {firstname} {lastname}")

thread_greeting = Thread(target=greeting, args=["Zeus", "Olympus"])
thread_greeting.start()

# -- 2.Thread class
class ThreadGreeting(Thread):

    def __init__(self, firstname):
        Thread.__init__(self)
        self.firstname = firstname

    def run(self):
        print(f"Hello {self.firstname} from {self.name}")

thr_greeting1 = ThreadGreeting("Name1")
thr_greeting2 = ThreadGreeting("Name2")

thr_greeting1.start()
thr_greeting2.start()

# -- 3. Multiple thread

class Count(Thread):
    
    def __init__(self, end_number, thread_name):
        Thread.__init__(self)
        self.name =thread_name
        self.end_number = end_number

    def run(self):
        for i in range(1, self.end_number + 1):
            print(f"{self.name} count {i}")
        
thr_count1 = Count(50, "A1")
thr_count2 = Count(50, "A2")
thr_count1.start()
thr_count1.join() # Wait until this thread complete the task
thr_count2.start()

# --