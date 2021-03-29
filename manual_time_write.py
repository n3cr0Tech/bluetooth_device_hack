# NOTE: this code ONLY runs on Raspberry Pi
import pygatt
import time
adapter = pygatt.GATTToolBackend()
adapter.start()
print('PyGatt Adapter Started')
MAC_ADDR = 'ENTER YOUR BLE DEVICE MAC ADDRESS HERE' 
device = adapter.connect(address=MAC_ADDR, address_type=pygatt.BLEAddressType.random)
hex_command = '21ff1006140b1d023329' # alter this value for your experimentation
adapter.sendline('char-write-cmd 0x0b ' + hex_command)
print('sending ' + hex_command + ' to 0x0b')
#adapter.sendline('char-write-cmd 0x0025 a106410a1a1a30b7e320bda291')
#adapter.sendline('char-write-cmd 0x0025 a107')
#print '-->headers sent'
#adapter.sendline('char-write-cmd 0x0025 a104030501') #Mode 3 of 5 Intensity with 1Min
#time.sleep(0.3)
#adapter.sendline('char-write-cmd 0x0025 a104070f04') #Mode 7 of 15 Intensity with 4Min
#time.sleep(0.3)
#print '-->High Intensity Triggered for 4 Min duration'
adapter.stop()
print('--> Disconnected from BLE Device')