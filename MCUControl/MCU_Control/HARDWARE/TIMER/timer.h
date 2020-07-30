#ifndef __TIMER_H
#define __TIMER_H
#include "sys.h"
//////////////////////////////////////////////////////////////////////////////////	 
//������ֻ��ѧϰʹ�ã�δ���������ɣ��������������κ���;
//ALIENTEKս��STM32������
//��ʱ�� ��������	   
//����ԭ��@ALIENTEK
//������̳:www.openedv.com
//�޸�����:2012/9/3
//�汾��V1.0
//��Ȩ���У�����ؾ���
//Copyright(C) �������������ӿƼ����޹�˾ 2009-2019
//All rights reserved									  
//////////////////////////////////////////////////////////////////////////////////   

//u32 time_s;

//void TIM3_Int_Init(u16 arr,u16 psc);

// u32* TIM3_Int_Init(u16 arr, u16 psc, u32* second);
// void TIM3_Int_Init(u16 arr, u16 psc, u32* second);

u32* TIM3_Int_Init(u16 arr,u16 psc);

// u32* self_second;

#endif
