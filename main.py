import time
import threading
import numpy
import matplotlib.pyplot as plotter

from ping3 import ping

def pinging():
    while not e.isSet():
        ms = ping('google.de') * 1000
        print(str(ms) + ' ms')
        # recoreded_times.append(ms)
        writeData(str(ms))
        time.sleep(2)

def writeData(data):
    with open("pings.txt", "a") as file:
        file.write(data + "\n")

def readData():
    with open("pings.txt", "r") as file:
        return file.readlines()

recoreded_times = []

thread = threading.Thread(target=pinging, args=())
e = threading.Event()
thread.start()

print('Press CTRL-C to interrupt')

while thread.is_alive():
    try:
        time.sleep(3)
    except KeyboardInterrupt:
        e.set() # set flag
        print('Stopping ping..')
        thread.join()

recoreded_times = readData()
float_times = []

for time in recoreded_times:
    tmp = time.replace("\n", "")
    float_times.append(float(time))

print('Performed ' + str(len(float_times)) + ' requests')
print(str(float_times))

plotter.plot(float_times)
plotter.ylabel('Time in ms')
plotter.xlabel('Number of ping')

axes = plotter.gca() # gca => 'get the current axes'
axes.set_ylim([0, 120])

plotter.show()