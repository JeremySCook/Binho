#test

from binhoHostAdapter import binhoHostAdapter
from binhoHostAdapter import binhoUtilities
import time

binhoTesterCommPort = 'COM12' #may need to be changed

# create the binhoHostAdapter object
binhoTester = binhoHostAdapter.binhoHostAdapter(binhoTesterCommPort)

binhoTester.setOperationMode(0, 'I2C')
binhoTester.setPullUpStateI2C(0, "DIS")
binhoTester.setClockI2C(0, 400000)

# initialize the display
print(binhoTester.startI2C(0, 0xE0))
print(binhoTester.writeByteI2C(0, 0x21))
print(binhoTester.writeByteI2C(0, 0x81))
print(binhoTester.writeByteI2C(0, 0xA0))
print(binhoTester.writeByteI2C(0, 0xEF))
print(binhoTester.endI2C(0))

# send 16 bytes of zeroes to clear the display
binhoTester.startI2C(0, 0xE0)
for i in range(16):
        binhoTester.writeByteI2C(0, 0x00)
binhoTester.endI2C(0)

print("set the '8' character in the 0 position")
print(binhoTester.startI2C(0, 0xE0))
print(binhoTester.writeByteI2C(0, 0x00)) # sets position of the character
print(binhoTester.writeByteI2C(0, 0xFF)) # LSByte of '8' character mapping
print(binhoTester.writeByteI2C(0, 0x00)) # MSByte of '8' character mapping
print(binhoTester.endI2C(0))
