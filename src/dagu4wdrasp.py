import serial
ard = serial.Serial('/dev/ttyACM0', 9600)

def move(dir):
    ard.write(dir)
    
while True:
    a = raw_input("Enter the direction ([direction] [ananlogl] [analog2])")
    move(a)
    
