import threading
import time

start = time.time()

def one():
    while True:
        print(10)
        if time.time() - start > 100:
            break

t1 = threading.Thread(target=one, daemon=True)
t1.start()
t1.join()


