#ifndef __SIG_H
#define __SIG_H	 
#include "sys.h"
//////////////////////////////////////////////////////////////////////////////////	 
//������ֻ��ѧϰʹ�ã�δ���������ɣ��������������κ���;
//ALIENTEKս��STM32������
//LED��������	   
//����ԭ��@ALIENTEK
//������̳:www.openedv.com
//�޸�����:2012/9/2
//�汾��V1.0
//��Ȩ���У�����ؾ���
//Copyright(C) �������������ӿƼ����޹�˾ 2009-2019
//All rights reserved									  
////////////////////////////////////////////////////////////////////////////////// 

#define SIGC0 PCout(0)  // PC0
#define SIGC1 PCout(1)  // PC1	
#define SIGC2 PCout(2)  // PC2
#define SIGC3 PCout(3)  // PC3	
#define SIGC4 PCout(4)  // PC4
#define SIGC5 PCout(5)  // PC5	
#define SIGC6 PCout(6)  // PC6	
#define SIGC7 PCout(7)  // PC7	
#define SIGC8 PCout(8)  // PC8	
#define SIGC9 PCout(9)  // PC9	

void SIG_Init(void);  //��ʼ��
		 				    
#endif
