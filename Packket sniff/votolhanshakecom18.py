import serial
ser = serial.Serial('COM18')
ser.write(b'\xC0\x14\x05\x52\x01\x14\x02\x03\x7F\x02\x94\x0A\x00\x32\x25\x80\x02\x76\x04\x5F\x00\x71\xBD\x0D') #page1
ser.write(b'\xC0\x14\x05\x52\x02\x00\x1E\x3C\x50\x5F\x0F\xA0\x23\x28\x17\x70\xA5\x2A\x0C\x1E\x1E\x0F\xE3\x0D')
ser.write(b'\xC0\x14\x05\x52\x03\x00\x1E\x50\x64\x69\x04\x1A\x00\x14\x24\xD4\x0A\x30\x18\x16\xE9\x71\x95\x0D') #version + page 3
ser.write(b'\xC0\x14\x05\x52\x04\x06\x0C\xCC\x01\x40\x04\xB0\x5C\x5C\x05\x01\xF4\x17\x70\x00\x00\x03\x20\x0D')
ser.write(b'\xC0\x14\x05\x52\x05\xC0\x01\xC0\x00\xC0\x00\xC0\x00\xC0\x11\xC0\x05\xC0\x07\xC0\x08\x03\x9F\x0D')
ser.write(b'\xC0\x14\x05\x52\x06\xC0\x09\xC0\x8A\xC0\x0B\xC0\x00\xC0\x00\xC0\x15\xC0\x0F\xC8\x92\x71\xFC\x0D')
ser.write(b'\xC0\x14\x05\x52\x07\x39\xC7\x0D\xE0\x50\xFA\x00\x00\x00\x00\x28\x02\x76\x04\x5F\x00\x71\x4B\x0D')

print("done")
