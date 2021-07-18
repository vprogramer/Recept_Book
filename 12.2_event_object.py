from threading import Thread, Event
import time

# Код для выполнения в независимом потоке
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

# Создать объект события, который будет использован для сигнала о запуске
started_evt = Event()
# Запустить поток и передать событие запуска
print('Launching countdown')
t = Thread(target=countdown, args=(10,started_evt))
t.start()
# Ждать запуска потока
started_evt.wait()
print('countdown is running')