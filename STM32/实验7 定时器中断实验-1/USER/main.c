#include "led.h"
#include "delay.h"
#include "key.h"
#include "sys.h"
#include "usart.h"
#include "timer.h"
 

/************************************************
 ALIENTEKս��STM32������ʵ��8
 ��ʱ���ж�ʵ��
 ����֧�֣�www.openedv.com
 �Ա����̣�http://eboard.taobao.com 
 ��ע΢�Ź���ƽ̨΢�źţ�"����ԭ��"����ѻ�ȡSTM32���ϡ�
 ������������ӿƼ����޹�˾  
 ���ߣ�����ԭ�� @ALIENTEK
************************************************/

u32* time_s = NULL;

 int main(void)
 {		
 
	delay_init();	    	 //��ʱ������ʼ��	  
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2); //����NVIC�жϷ���2:2λ��ռ���ȼ���2λ��Ӧ���ȼ�
	uart_init(115200);	 //���ڳ�ʼ��Ϊ115200
 	LED_Init();			     //LED�˿ڳ�ʼ��
	time_s = TIM3_Int_Init(9999,7199);//10Khz�ļ���Ƶ�ʣ�������9999Ϊ1000ms  

   	while(1)
	{
		//LED0=!LED0;
		//delay_ms(200);		  
		if( *time_s == 2 )
		{
			LED0 = 0;
			//delay_ms(1000);
			//*time_s = 0;
		}

		if( *time_s == 10 )
		{
			LED0 = 1;
			//delay_ms(500);
			*time_s = 0;
		}

	}	 

 
}	 
 
