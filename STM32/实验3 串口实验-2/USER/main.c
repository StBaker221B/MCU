#include "led.h"
#include "delay.h"
#include "key.h"
#include "sys.h"
#include "usart.h"
 
 
/************************************************
 ALIENTEK战舰STM32开发板实验4
 串口实验 
 技术支持：www.openedv.com
 淘宝店铺：http://eboard.taobao.com 
 关注微信公众平台微信号："正点原子"，免费获取STM32资料。
 广州市星翼电子科技有限公司  
 作者：正点原子 @ALIENTEK
************************************************/


 int main(void)
 {		
 	u16 t;  
	u16 len;	
	u16 times=0;
	
	u8 on[4] = {"on "};
	u8 off[4] = {"off"};

	delay_init();	    	 //延时函数初始化	  
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2); //设置NVIC中断分组2:2位抢占优先级，2位响应优先级
	uart_init(115200);	 //串口初始化为115200
 	LED_Init();			     //LED端口初始化
	KEY_Init();          //初始化与按键连接的硬件接口
 	while(1)
	{
		/**
		if(USART_RX_STA&0x8000)
		{
//			LED0 =! LED0;
			//delay_ms(5000);
			//delay_ms(5000);
			//len=USART_RX_STA&0x3fff;//得到此次接收到的数据长度
			//printf("\r\n您发送的消息为:\r\n\r\n");
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
//				USART_SendData(USART1, USART_RX_BUF[t]);//向串口1发送数据
//				while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);//等待发送结束
//			}
			//printf("\r\n\r\n");//插入换行
			USART_RX_STA=0;
		}else
		{
			times++;
			if(times%5000==0)
			{
				printf("\r\n战舰STM32开发板 串口实验\r\n");
				printf("正点原子@ALIENTEK\r\n\r\n");
			}
			if(times%2==0)printf("请输入数据,以回车键结束\n");  
			// if(times%5==0)LED0=!LED0;//闪烁LED,提示系统正在运行.
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

