import time
import threading
import numpy
import matplotlib.pyplot as plotter

from ping3 import ping

def pinging():
    while not e.isSet():
        ms = ping('google.de') * 1000
        print(str(ms) + ' ms')
        recoreded_times.append(ms)
        time.sleep(2)


recoreded_times = []

thread = threading.Thread(target=pinging, args=())
e = threading.Event()
thread.start()

print('Press CTRL-C to interrupt')

while thread.is_alive():
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        e.set() # set flag
        print('Stopping ping..')
        thread.join()

print('Performed ' + str(len(recoreded_times)) + ' requests')
print(str(recoreded_times))

plotter.plot(recoreded_times)
plotter.ylabel('Time in ms')
plotter.xlabel('Number of ping')

axes = plotter.gca() # gca => 'get the current axes'
axes.set_ylim([0, 120])

plotter.show()