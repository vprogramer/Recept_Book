from queue import Queue
from threading import Thread


def producer(out_q):
    while True:
        global data
        data += 2
        if data > 40:
            break
        out_q.put(data)
        print(data)


def consumer(in_q):
    while True:
        data = in_q.get()
        if data > 40:
            break
        data += 5
        print(data)


data = 0
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Finish: ' + str(data))