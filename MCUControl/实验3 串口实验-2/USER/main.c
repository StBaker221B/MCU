#include "led.h"
#include "delay.h"
#include "key.h"
#include "sys.h"
#include "usart.h"
 
 
/************************************************
 ALIENTEKս��STM32������ʵ��4
 ����ʵ�� 
 ����֧�֣�www.openedv.com
 �Ա����̣�http://eboard.taobao.com 
 ��ע΢�Ź���ƽ̨΢�źţ�"����ԭ��"����ѻ�ȡSTM32���ϡ�
 ������������ӿƼ����޹�˾  
 ���ߣ�����ԭ�� @ALIENTEK
************************************************/


 int main(void)
 {		
 	u16 t;  
	u16 len;	
	u16 times=0;
	
	u8 on[4] = {"on "};
	u8 off[4] = {"off"};

	delay_init();	    	 //��ʱ������ʼ��	  
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2); //����NVIC�жϷ���2:2λ��ռ���ȼ���2λ��Ӧ���ȼ�
	uart_init(115200);	 //���ڳ�ʼ��Ϊ115200
 	LED_Init();			     //LED�˿ڳ�ʼ��
	KEY_Init();          //��ʼ���밴�����ӵ�Ӳ���ӿ�
 	while(1)
	{
		/**
		if(USART_RX_STA&0x8000)
		{
//			LED0 =! LED0;
			//delay_ms(5000);
			//delay_ms(5000);
			//len=USART_RX_STA&0x3fff;//�õ��˴ν��յ������ݳ���
			//printf("\r\n�����͵���ϢΪ:\r\n\r\n");
			//LED0 =! LED0;
			
			
			if(USART_RX_BUF[0] == 0x30)
			{
				LED1 = 0;
				for( t = 0; t < 3; t++ )
				{
					USART_SendData(USART1, off[t]);
					while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);
				}
			}
			else
			{
				LED1 = 1;
				for( t = 0; t < 3; t++ )
				{
					USART_SendData(USART1, on[t]);
					while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);
				}
			}
			
//			for(t=0;t<len;t++)
//			{
//				USART_SendData(USART1, USART_RX_BUF[t]);//�򴮿�1��������
//				while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);//�ȴ����ͽ���
//			}
			//printf("\r\n\r\n");//���뻻��
			USART_RX_STA=0;
		}else
		{
			times++;
			if(times%5000==0)
			{
				printf("\r\nս��STM32������ ����ʵ��\r\n");
				printf("����ԭ��@ALIENTEK\r\n\r\n");
			}
			if(times%2==0)printf("����������,�Իس�������\n");  
			// if(times%5==0)LED0=!LED0;//��˸LED,��ʾϵͳ��������.
			delay_ms(1000);   
		}
		*/
		
		if(USART_RX_STA&0x8000)
		{
			switch(USART_RX_BUF[0]){
				
//				case 'B':{
				case 0x42:{
					switch(USART_RX_BUF[1]){
					
//						case '5':
						case 0x35:
							LED0 =! LED0;
							break;
						default:
							break;
					}
					break;
				}
//				case 'E':{
				case 0x45:{
					switch(USART_RX_BUF[1]){
					
//						case '5':
						case 0x35:
							LED1 =! LED1;
							break;
						default:
							break;
					}
					break;
				}
				break;					
			}
			USART_RX_STA=0;
		}
	}	 
 }

