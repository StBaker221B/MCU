
// #include "led.h"
#include "sig.h"
#include "delay.h"
#include "key.h"
#include "sys.h"
#include "beep.h"
 
/************************************************
 ALIENTEKս��STM32������ʵ��3
 ��������ʵ��  
 ����֧�֣�www.openedv.com
 �Ա����̣�http://eboard.taobao.com 
 ��ע΢�Ź���ƽ̨΢�źţ�"����ԭ��"����ѻ�ȡSTM32���ϡ�
 ������������ӿƼ����޹�˾  
 ���ߣ�����ԭ�� @ALIENTEK
************************************************/


 int main(void)
 {
 	vu8 key=0;	
	delay_init();	    	 //��ʱ������ʼ��	  
 	SIG_Init();			     //LED�˿ڳ�ʼ��
	KEY_Init();          	//��ʼ���밴�����ӵ�Ӳ���ӿ�
	BEEP_Init();         	//��ʼ���������˿�
	SIG0=0;					//�ȵ������
	while(1)
	{
 		key=KEY_Scan(0);	//�õ���ֵ
	   	if(key)
		{						   
			switch(key)
			{				 
				case WKUP_PRES:	//����LED1��ת	
					SIG1=!SIG1;
					break;
				case KEY0_PRES:	//ͬʱ����LED0��ת 
					SIG0=!SIG0;
					break;
			}
		}else delay_ms(10); 
	}	 
}

