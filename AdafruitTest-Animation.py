#AdafruitTest-Animation.py
#for Binho host adapter

# send 16 bytes of zeroes to clear the display
def wipeScreen():
    binhoTester.startI2C(0, 0xE0)
    for i in range(16):
        binhoTester.writeByteI2C(0, 0x00)
    binhoTester.endI2C(0)
    return;

from binhoHostAdapter import binhoHostAdapter
from binhoHostAdapter import binhoUtilities
import time

binhoTesterCommPort = 'COM12' #may need to be changed

# create the binhoHostAdapter object
binhoTester = binhoHostAdapter.binhoHostAdapter(binhoTesterCommPort)

#initialize the Binho host adapter for I2C communication
binhoTester.setOperationMode(0, 'I2C')
binhoTester.setPullUpStateI2C(0, "DIS")
binhoTester.setClockI2C(0, 400000)

# initialize the character display

binhoTester.startI2C(0, 0xE0)
binhoTester.writeByteI2C(0, 0x21) # turn on oscillator
binhoTester.endI2C(0)

binhoTester.startI2C(0, 0xE0)
binhoTester.writeByteI2C(0, 0x81) # blink rate
binhoTester.endI2C(0)

binhoTester.startI2C(0, 0xE0)
binhoTester.writeByteI2C(0, 0xA0) # brightness
binhoTester.endI2C(0)

binhoTester.startI2C(0, 0xE0)
binhoTester.writeByteI2C(0, 0xEF)
binhoTester.endI2C(0)

#write/scroll letters

for j in range(0, 16, 2):
    wipeScreen()
    print(binhoTester.startI2C(0, 0xE0))
    print(binhoTester.writeByteI2C(0, j)) # sets position of the character
    print(binhoTester.writeByteI2C(0, 0x8F)) # LSByte of 'B' character mapping
    print(binhoTester.writeByteI2C(0, 0x12)) # MSByte of 'B' character mapping    
    print(binhoTester.endI2C(0))
    time.sleep(.2)
    
for j in range(0, 16, 2):
    wipeScreen()
    print(binhoTester.startI2C(0, 0xE0))
    binhoTester.writeByteI2C(0, j) # sets position of the character
    binhoTester.writeByteI2C(0, 0x00) # LSByte of 'I' character mapping
    print(binhoTester.writeByteI2C(0, 0x12)) # MSByte of 'I' character mapping    
    print(binhoTester.endI2C(0))
    time.sleep(.2)
    
for j in range(0, 16, 2):
    wipeScreen()
    print(binhoTester.startI2C(0, 0xE0))
    print(binhoTester.writeByteI2C(0, j)) # sets position of the character
    print(binhoTester.writeByteI2C(0, 0b00110110)) # LSByte of 'N' character mapping
    print(binhoTester.writeByteI2C(0, 0b00100001)) # MSByte of 'N' character mapping    
    print(binhoTester.endI2C(0))
    time.sleep(.2)

for j in range(0, 16, 2):
    wipeScreen()
    print(binhoTester.startI2C(0, 0xE0))
    print(binhoTester.writeByteI2C(0, j)) # sets position of the character
    print(binhoTester.writeByteI2C(0, 0b11110110)) # LSByte of 'H' character mapping
    print(binhoTester.writeByteI2C(0, 0b00000000)) # MSByte of 'H' character mapping    
    print(binhoTester.endI2C(0))
    time.sleep(.2)
    
for j in range(0, 16, 2):
    wipeScreen()
    print(binhoTester.startI2C(0, 0xE0))
    print(binhoTester.writeByteI2C(0, j)) # sets position of the character
    print(binhoTester.writeByteI2C(0, 63)) # LSByte of 'O' character mapping
    print(binhoTester.writeByteI2C(0, 0)) # MSByte of 'O' character mapping    
    print(binhoTester.endI2C(0))
    time.sleep(.2)
