
// #include "led.h"
#include "sig.h"
#include "delay.h"
#include "key.h"
#include "sys.h"
#include "beep.h"

/************************************************
ALIENTEK战舰STM32开发板实验3
按键输入实验  
技术支持：www.openedv.com
淘宝店铺：http://eboard.taobao.com 
关注微信公众平台微信号："正点原子"，免费获取STM32资料。
广州市星翼电子科技有限公司  
作者：正点原子 @ALIENTEK
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
	delay_init();	    	 //延时函数初始化	  
	SIG_Init();			     //LED端口初始化
	KEY_Init();          	//初始化与按键连接的硬件接口
	BEEP_Init();         	//初始化蜂鸣器端口

	SIG0=0;					//先点亮红灯
	SIG1=0;					//先点亮红灯

	// u32 state = 0;
	while(1)
	{
		/*
		key=KEY_Scan(0);	//得到键值
		if(key)
		{						   
			switch(key)
			{				 
				case WKUP_PRES:	//控制LED1翻转	
					SIG1=!SIG1;
					break;
				case KEY0_PRES:	//同时控制LED0翻转 
					SIG0=!SIG0;
					break;
			}
		}else delay_ms(10); 
		*/

		/*
		key=KEY_Scan(0);	//得到键值

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
		
		
		key=KEY_Scan(0);	//得到键值
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

