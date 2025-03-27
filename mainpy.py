import serial

aruinoData = serial.Serial('com4', 9600)

def ledOn():
    aruinoData.write('1')

def ledOff():
    aruinoData.write('0')

t=0
while(t<2000):
    if(t % 10 == 0):
        print(t)
    t +=1

ledOff()

print("done")