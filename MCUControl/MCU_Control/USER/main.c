
#include "stm32f10x.h"
// #include<stdio.h>

#include "led.h"
#include "delay.h"
#include "key.h"
#include "sys.h"
#include "usart.h"
#include "timer.h"

#include "sig.h"


#define SWITCHES 12


typedef enum 
{
    TIME_CONTROL = 0,
    PC_CONTROL = 1
} control_state;

u32* time_s = NULL;
// u32 time_s = 0;
u32 TIME_PERIOD;
control_state cs;
volatile unsigned long* port;
// volatile unsigned long* port[SWITCHES] = {NULL};
u8 report[3] = {0};

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
    time_s = TIM3_Int_Init(999, 7199);
    // TIM3_Int_Init(9999, 7199, &time_s);
    TIME_PERIOD = 61;
    port = NULL;
    // port = {&LED0, &LED1, 
    //         &SIGC0, &SIGC1, &SIGC2, &SIGC3, &SIGC4, 
    //         &SIGC5, &SIGC6, &SIGC7, &SIGC8, &SIGC9}
    // report = {0}

    LED0 = 1;
    LED1 = 0;
}

void timecontrol()
{
    // printf("time control \r\n");

    // if( *time_s > 6)
    //     *time_s = 0;
    
    // switch(time_s)
    switch(*time_s)
    {
        // case 0:
        // case 1:
        // case 4:
        //     break;
        case 20:
            LED0 = 0;
            SIGC0 = 0;
            break;
        case 30:
            LED1 = 0;
            SIGC1 = 0;
            break;
        case 50:
            LED0 = 1;
            SIGC0 = 1;
            break;
        case 60:
            LED1 = 1;
            SIGC1 = 1;
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
    // u8 C0[2] = {"C0"}
    // u8 C1[2] = {"C1"}
    int t;
    
    switch(USART_RX_BUF[0])
    {
        // case 'C'
        case 0x43:
            report[0] = 'C';
            switch(USART_RX_BUF[1])
            {
                // case '0'
                case 0x30:
                    // LED0 =! LED0;
                    // SIGC0 =! SIGC0;
                    // port = &SIGC0;
                    port = &LED0;
                    report[1] = '0';
                    break;
                // case '1'
                case 0x31:
                    // LED1 =! LED1;
                    // SIGC1 =! SIGC1;
                    // port = &SIGC1;
                    port = &LED1;
                    report[1] = '1';
                    break;
                case 0x32:
                    // SIGC2 =! SIGC2;
                    port = &SIGC2;
                    break;
                case 0x33:
                    // SIGC3 =! SIGC3;
                    port = &SIGC3;
                    break;
                case 0x34:
                    // SIGC4 =! SIGC4;
                    port = &SIGC4;
                    break;
                case 0x35:
                    // SIGC5 =! SIGC5;
                    port = &SIGC5;
                    break;
                case 0x36:
                    // SIGC6 =! SIGC6;
                    port = &SIGC6;
                    break;
                case 0x37:
                    // SIGC7 =! SIGC7;
                    port = &SIGC7;
                    break;
                case 0x38:
                    // SIGC8 =! SIGC8;
                    port = &SIGC8;
                    break;
                case 0x39:
                    // SIGC9 =! SIGC9;
                    port = &SIGC9;
                    break;
            }
            break;
    }
    switch(USART_RX_BUF[2])
    {
        // case '0'
        case 0x30:
            *port = 0;
            // printf("port = 0\n");
            report[2] = '0';
            break;
        case 0x31:
            *port = 1;
            report[2] = '1';
            // printf("port = 1\n");
            break;
    }
    
    for( t = 0; t < 3; t++ )
    {
        // USART_SendData(USART1, report[t]);
        // while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);
        printf("%c", report[t]);
    }
    USART_RX_STA=0;
}


void portreport()
{
    // C0 
    if(LED0)
        printf("C01");
    else
        printf("C00");
    // C1 
    if(LED1)
        printf("C11");
    else
        printf("C10");
    
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
                // printf("TIME CONTROL \r\n");
                timecontrol();
                // delay_ms(500);
                // report();
                break;
            case PC_CONTROL:
                pccontrol();
                cs = TIME_CONTROL;
                // report();
                // delay_ms(1000);
                break;
        }

        if((*time_s % 10) == 0)
            portreport();

        // LED0 =! LED0;
        // printf("\r\n %d \n", *time_s);
        // printf("\r\n %d \n", time_s);
        // delay_ms(1000);
    }
}
