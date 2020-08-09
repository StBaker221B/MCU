import serial
import serial.tools.list_ports

def spopen():
	port_list = list(serial.tools.list_ports.comports())
	if len(port_list) == 0:
		print("no serial ports")
		return 0
	else:
		sp = str(port_list[0])
		sp = sp.split()
		sp = sp[0]
		print(sp)

	ser = serial.Serial(sp, 115200, timeout = 0.1)
	if ser.isOpen():
		print("sp open")
		return ser
	else:
		print ("sp not open")

def spcom(ser, sig):
	# data = sig    #发送的数据
	# ser.write(data)      #串口写数据
	# if ser.isOpen():
		# print("sp open")
		# return ser
	ser.write(sig)      #串口写数据
		# print ('You Send Data:',data)

	# else:
		# print ("sp not open")

	# ser.write(sig)      #串口写数据
	# print ('You Send Data:',data)
	
		# while True:
		# 	data = ser.read(7)    #串口读20位数据
		# 	if data != b'':
		# 		break
		# print ('receive data is :',data) 
		
	# else:
	# 	print ('串口未打开')
	
	
def spcheck(ser):
    rx = []
    while True:
        if(ser.in_waiting):
            rx.append(ser.read(1).decode("utf-8"))
            l = len(rx)
            if(rx[0] != '*'):
                if(l == 1):
                    rx = []
                else:
                    for i in range(l-1):
                        rx[i] = rx[i+1]
            if(l > 3):
                if(rx[l-1] == '*'):
                    message = ''.join(rx)
                    print(message)
                    rx = []

    #         if(l > 14):
    #             if 
	# data = ser.read(4)
	# if data != b'':
	# 	print(data)

def spclose(ser):
	ser.close()

if __name__ == '__main__':
    ser = spopen()
    spcheck(ser)