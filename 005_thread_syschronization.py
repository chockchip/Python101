from threading import Thread, Lock

GLOBAL_COUNT = 0

lock = Lock()

class Counter(Thread):

    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        global GLOBAL_COUNT

        while GLOBAL_COUNT <= 100:
            lock.acquire()
            n = GLOBAL_COUNT
            GLOBAL_COUNT += 1
            lock.release()
            print(f"Conut {n} by {self.name}")

counter_number1 = Counter()
counter_number2 = Counter()

counter_number1.start()
counter_number2.start()