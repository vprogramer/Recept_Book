# from queue import Queue
# from threading import Thread
# import time
#
#
# # Поток, который производит данные
# def producer(out_q):
#     data = 5
#     while True:
#         # Производим данные
#         out_q.put(data)
#         time.sleep(1)
#         data = out_q.get()
#         data += 0.5
#         if data > 100:
#             break
#
#
# # Поток, который потребляет данные
# def consumer(in_q):
#     while True:
#         # Получаем данные
#         data = in_q.get()
#         # Обрабатываем данные
#         data += 3
#         print(data)
#         in_q.put(data)
#         time.sleep(1)
#         if data > 100:
#             break
#
#
#
# # Создаем разделяемую (shared) очередь и запускаем оба потока
# q = Queue()
# t1 = Thread(target=consumer, args=(q,))
# t2 = Thread(target=producer, args=(q,))
# t1.start()
# t2.start()

# def double_inputs():
#     for i in range(10):
#         x = yield i
#         print("func " + str(x))
#
#
# gen = double_inputs()
# print(next(gen))
# print('#')
# print(gen.send(10))
# print('#')
# print(next(gen))
# print('#')
# print(gen.send(6))
# print('#')
# print(next(gen))
# print('#')
# print(gen.send(94.3))
# print('#')

def func():
    output = 0
    while True:
        new = yield output
        output = new if new != None else output


genr = func()
print(genr.send(None))
print(next(genr))
print(next(genr))
print(next(genr))
