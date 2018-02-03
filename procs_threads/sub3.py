import select
import threading
import time

def slow_systemcall():
    select.select([], [], [], 0.1)

threads = []
start = time.time()
for _ in range(5):
    thread = threading.Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)
    #slow_systemcall()
for thread in threads:
    thread.join()

end = time.time()

print(end - start)