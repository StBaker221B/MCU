
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

u32 state = 0;

void delay_s(u32 s)
{
	u32 i = 0;
	for(; i < s; i++ )
	{
		delay_ms(1000);
	}
}

void swap()
{
	SIG0 =! SIG0;
	delay_s(2);
}

int main(void)
{
	vu8 key=0;	
	delay_init();	    	 //��ʱ������ʼ��	  
	SIG_Init();			     //LED�˿ڳ�ʼ��
	KEY_Init();          	//��ʼ���밴�����ӵ�Ӳ���ӿ�
	BEEP_Init();         	//��ʼ���������˿�

	SIG0=0;					//�ȵ������
	SIG1=0;					//�ȵ������

	// u32 state = 0;
	while(1)
	{
		/*
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
		*/

		/*
		key=KEY_Scan(0);	//�õ���ֵ

		if(key)
		{
			switch(key)
			{
				case WKUP_PRES:
					state = 1;
				case KEY0_PRES:
					state = 0;
			}
			// SIG0 =! SIG0;
			// delay_s(2);
		}

		if( state == 1 )
		{
			SIG0 =! SIG0;
			delay_s(2);
		}
		*/
		
		
		key=KEY_Scan(0);	//�õ���ֵ
		if(key)
		{
			switch(key)
			{
				case WKUP_PRES:
					
					if(SIG1)
					{
						SIG1 =! SIG1;
					}
					
					SIG0 =! SIG0;
					break;
				case KEY0_PRES:
					
					if(SIG0)
					{
						SIG0 =! SIG0;
					}
					
					SIG1 =! SIG1;
					break;
			}
			// SIG0 =! SIG0;
			// delay_s(2);
		}
		

		//SIG0 =! SIG0;
		//SIG1 =! SIG1;
		//delay_s(2);

	}	 
}

