#test

from binhoHostAdapter import binhoHostAdapter
from binhoHostAdapter import binhoUtilities
import time

binhoTesterCommPort = 'COM12' #may need to be changed

# create the binhoHostAdapter object
binhoTester = binhoHostAdapter.binhoHostAdapter(binhoTesterCommPort)

print(binhoTester.setLEDColor('YELLOW'))
time.sleep(1)
print(binhoTester.setLEDColor('RED'))
time.sleep(1)
print(binhoTester.setLEDColor('BLUE'))
