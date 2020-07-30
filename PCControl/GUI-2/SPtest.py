import serial
 
#连接串口

def com(sig):
	ser = serial.Serial('COM4',115200,timeout=2)
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
