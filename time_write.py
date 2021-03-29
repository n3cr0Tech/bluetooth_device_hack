import pygatt
from datetime import datetime
 
def write_date_time_update_command_to_bluetooth(mac_addr):        
    tokenized_date_time = get_tokenized_date_time()    
    hexCommand = get_hex_command(extract_date(tokenized_date_time[0]), extract_time(tokenized_date_time[1]))
    # Run gatttool interactively.
    print("Running gatttool...")    
    adapter = pygatt.GATTToolBackend()
    adapter.start()
    print('PyGatt Adapter Started')
    device = adapter.connect(address=mac_addr, address_type=pygatt.BLEAddressType.random)
    print('Ready to send commands to BLE device')
    adapter.sendline('char-write-cmd 0x0b ' + hexCommand)
    print('sending ' + hexCommand + ' to 0x0b')
    adapter.stop()
    print('Disconnected from BLE device')

def get_tokenized_date_time():
    date_time_now = datetime.now() 
    dt_string = date_time_now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    tokenized_date_time = dt_string.split(' ')   
    return tokenized_date_time

# takes 'dd/mm/YY'
# returns [dd, mm, YY]
def extract_date(date_string):    
    return date_string.split('/')    

# takes H:M:S
# returns [H, M, s]
def extract_time(time_string):
    return time_string.split(':')

# date_today is mm/dd/yy
#time is HH:MM:SS
def get_hex_command(date_today, time):
    # hexBuilder will have for example: 21ff1006{14}{0b}{1d}{02}{33}{29} where the last six segments are dynamic    
    year = int(date_today[2][2:4]) #only take the last 2 digits of the year    
    month = int(date_today[1])    
    day = int(date_today[0])    
    hexBuilder = '21ff1006' 
    hexBuilder += decimal_to_hex(year)
    hexBuilder += decimal_to_hex(month)
    hexBuilder += decimal_to_hex(day)    
    hour = int(time[0])
    minute = int(time[1])
    seconds = int(time[2])
    hexBuilder += decimal_to_hex(hour)
    hexBuilder += decimal_to_hex(minute)
    hexBuilder += decimal_to_hex(seconds)
    print('hex command: ' + hexBuilder)
    return hexBuilder
    
# gets a 3
# converts to a 0x3
# returns '03'
def decimal_to_hex(dec):    
    hex_val = hex(dec)
    tokenized_val = hex_val.split('0x') #remove the '0x'
    result = tokenized_val[1]
    if len(result) == 1:
        result = '0' + result
    print('converted dec: ' + str(dec) + " into hex: " + result)
    return result


MAC_ADDR = 'BLE MAC ADDRESS GOES HERE'
write_date_time_update_command_to_bluetooth(MAC_ADDR) 