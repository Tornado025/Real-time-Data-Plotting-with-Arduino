import matplotlib.pyplot as plt
import time
import random
import serial

x_data = []
y_data = []

plt.ion() 
fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-', label="Live Data")
serialport=serial.Serial('COM3',baudrate=9600,timeout=1)

# Set up plot limits and labels
ax.set_xlim(0, 10)  # Initial X-axis limit
ax.set_ylim(0, 100)  # Initial Y-axis limit
ax.set_xlabel("TIME")
ax.set_ylabel("TEMP")
ax.set_title("Temp Loss vs Time???")
ax.legend()

def update_plot():
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    # Dynamically adjust axis limits
    ax.set_xlim(0,10)
    ax.set_ylim(0,100)
    fig.canvas.draw()
    fig.canvas.flush_events()

try:
    while True:
        arduinodat=serialport.readline().decode('ascii')
        print(arduinodat)
        lis=arduinodat.strip().split(',')
        if(lis[0]!=''):
            y_data.append(float(lis[0]))
            x_data.append(float(lis[1]))
        update_plot() 
        time.sleep(0.1) 

except KeyboardInterrupt:
    print("Real-time plotting stopped by user.")
finally:
    plt.ioff()
    plt.show()
