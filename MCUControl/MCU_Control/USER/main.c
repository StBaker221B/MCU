
#include "stm32f10x.h"
// #include<stdio.h>

#include "led.h"
#include "delay.h"
#include "key.h"
#include "sys.h"
#include "usart.h"
#include "timer.h"

#include "sig.h"


typedef enum 
{
    TIME_CONTROL = 0,
    PC_CONTROL = 1
} control_state;

u32* time_s = NULL;
// u32 time_s = 0;
u32 TIME_PERIOD = 7;

control_state cs;

void init()
{
    delay_init();
    NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
    uart_init(115200);
    LED_Init();
    SIG_Init();
    KEY_Init();

    cs = TIME_CONTROL;

    // second = &time_s;
    // time_s = TIM3_Int_Init(9999, 7199);
    time_s = TIM3_Int_Init(9999, 7199);
    // TIM3_Int_Init(9999, 7199, &time_s);

    LED0 = 1;
    LED1 = 0;
}

void timecontrol()
{
    printf("time control \r\n");

    // if( *time_s > 6)
    //     *time_s = 0;
    
    // switch(time_s)
    switch(*time_s)
    {
        // case 0:
        // case 1:
        // case 4:
        //     break;
        case 2:
            LED0 = 0;
            break;
        case 3:
            LED1 = 0;
            break;
        case 5:
            LED0 = 1;
            break;
        case 6:
            LED1 = 1;
            break;
        // case 7:
        //     *time_s = 0;
        //     break;
        // default:
        //     *time_s = 0;
        //     break;
    }
}

void pccontrol()
{
    switch(USART_RX_BUF[0])
    {
        // case 'C'
        case 0x43:
            switch(USART_RX_BUF[1])
            {
                // case '0'
                case 0x30:
                    LED0 =! LED0;
                    SIGC0 =! SIGC0;
                    break;
                // case '1'
                case 0x31:
                    LED1 =! LED1;
                    SIGC1 =! SIGC1;
                    break;
                case 0x32:
                    SIGC2 =! SIGC2;
                    break;
                case 0x33:
                    SIGC3 =! SIGC3;
                    break;
                case 0x34:
                    SIGC4 =! SIGC4;
                    break;
                case 0x35:
                    SIGC5 =! SIGC5;
                    break;
                case 0x36:
                    SIGC6 =! SIGC6;
                    break;
                case 0x37:
                    SIGC7 =! SIGC7;
                    break;
                case 0x38:
                    SIGC8 =! SIGC8;
                    break;
                case 0x39:
                    SIGC9 =! SIGC9;
                    break;

            }
            break;
    }
    USART_RX_STA=0;
}

int main()
{
    init();

    while(1)
    {
        if( *time_s > TIME_PERIOD )
        {
            *time_s = 0;
            continue;
        }

        if(USART_RX_STA & 0x8000)
        {
            cs = PC_CONTROL;
        }

        switch(cs)
        {
            case TIME_CONTROL:
                printf("TIME CONTROL \r\n");
                timecontrol();
                delay_ms(500);
                break;
            case PC_CONTROL:
                pccontrol();
                cs = TIME_CONTROL;
                delay_ms(1000);
                break;
        }

        // LED0 =! LED0;
        printf("\r\n %d \n", *time_s);
        // printf("\r\n %d \n", time_s);
        // delay_ms(1000);
    }
}
