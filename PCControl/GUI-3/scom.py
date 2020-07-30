import serial
import serial.tools.list_ports


def com(sig):

	# check serial ports 
	port_list = list(serial.tools.list_ports.comports())
	if len(port_list) == 0:
		print("no serial ports")
		return 0
	else:
		sp = str(port_list[0])
		# sp = port_list[0]
		# sp = list(sp)
		sp = sp.split()
		sp = sp[0]
		print(sp)

	ser = serial.Serial(sp, 115200, timeout = 2)
	if ser.isOpen():
		print ('串口已打开')

		# data = b'0\r\n'    #发送的数据
		data = sig    #发送的数据
		ser.write(data)      #串口写数据
		print ('You Send Data:',data)
	
		# while True:
		# 	data = ser.read(7)    #串口读20位数据
		# 	if data != b'':
		# 		break
		# print ('receive data is :',data) 
		
	else:
		print ('串口未打开')
	
	
	
	#关闭串口
	ser.close()
	
	if ser.isOpen():
		print ('串口未关闭')
	else:
		print ('串口已关闭')

if __name__ == '__main__':
	com(b'C0\r\n')