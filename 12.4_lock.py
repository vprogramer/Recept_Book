import threading

class SharedCounter:
    '''
    Объект счетчика, который может быть общим для нескольких потоков.
    '''
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.RLock()

    def incr(self,delta=1):
        '''
        Инкрементирует счетчик с блокировкой.
        '''
        for i in range(10):
            with self._value_lock:
                self._value += delta
                print(1)

    def decr(self,delta=1):
        '''
        Декрементирует счетчик с блокировкой.
        '''
        for i in range(10):
            with self._value_lock:
                self._value -= delta
                print(2)

    def value(self):
        return self._value


sc = SharedCounter()
t1 = threading.Thread(target=sc.incr)
t2 = threading.Thread(target=sc.decr, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()
print(sc.value())
