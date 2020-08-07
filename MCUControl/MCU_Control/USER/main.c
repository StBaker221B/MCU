
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
    TIME_CONTROL_START = 0,
    TIME_CONTROL_REPEAT = 1,
    PC_CONTROL = 2
} control_state;

u32* time_s = NULL;
// u32 time_s = 0;
u32 TIME_PERIOD;
control_state cs;
volatile unsigned long* port;
// volatile unsigned long* port[SWITCHES] = {NULL};
u8 report[15] = {0};

void init()
{
    delay_init();
    NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
    uart_init(115200);
    LED_Init();
    SIG_Init();
    KEY_Init();

    cs = TIME_CONTROL_START;

    // second = &time_s;
    // time_s = TIM3_Int_Init(9999, 7199);
    time_s = TIM3_Int_Init(999, 7199);  // 0.1 s 计时
    // TIM3_Int_Init(9999, 7199, &time_s);
    TIME_PERIOD = 140;
    port = NULL;
    // port = {&LED0, &LED1, 
    //         &SIGC0, &SIGC1, &SIGC2, &SIGC3, &SIGC4, 
    //         &SIGC5, &SIGC6, &SIGC7, &SIGC8, &SIGC9}
    // report = {0}

    LED0 = 1;
    LED1 = 1;
}

void timeCtrlstart()
{
    // printf("time control \r\n");

    // if( *time_s > 6)
    //     *time_s = 0;
    
    // switch(time_s)
    switch(*time_s)
    {
        case 10:  // 1 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 1;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 0;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;

            break;

        case 20:  // 2 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 1;
            PSA1_PRO = 1;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 0;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;

        case 30:  // 3 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 1;
            PSA1_PRO = 1;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 0;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;

        case 40:  // 4 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 1;
            PSA1_CLR = 0;

            PSA2_IN = 1;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 0;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;
        
        case 50:  // 5 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 1;

            PSA2_IN = 1;
            PSA2_PRO = 1;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 0;
            PROD_PSA1 = 1;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 60:  // 6 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 1;
            PSA2_PRO = 1;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 0;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 70:  // 7 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 1;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 1;
            PSA2_CLR = 0;

            PROD_OUT = 0;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       

        case 80:  // 8 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 1;
            PSA1_PRO = 1;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 1;

            PROD_OUT = 0;
            PROD_PSA1 = 0;
            PROD_PSA2 = 1;

            COL2_IN = 0;
            break;       
    
        case 90:  // 9 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 1;
            PSA1_PRO = 1;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 100:  // 10 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 1;
            PSA1_CLR = 0;

            PSA2_IN = 1;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 110:  // 11 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 1;

            PSA2_IN = 1;
            PSA2_PRO = 1;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 1;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 120:  // 12 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 1;
            PSA2_PRO = 1;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 130:  // 13 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 1;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 1;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 140:  // 14 s
            LED0 = 0;
            LED1 = 1;

            PSA1_IN = 1;
            PSA1_PRO = 1;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 1;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 1;

            COL2_IN = 0;
            break;       
    
    }
}

void timeCtrlrepeat()
{
    // repeat cycle time control
    switch(*time_s)
    {
        case 10:  // 1 s
            LED0 = 1;
            LED1 = 0;

            PSA1_IN = 1;
            PSA1_PRO = 1;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 20:  // 2 s
            LED0 = 1;
            LED1 = 0;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 1;
            PSA1_CLR = 0;

            PSA2_IN = 1;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 30:  // 3 s
            LED0 = 1;
            LED1 = 0;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 1;

            PSA2_IN = 1;
            PSA2_PRO = 1;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 1;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 40:  // 4 s
            LED0 = 1;
            LED1 = 0;

            PSA1_IN = 0;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 1;
            PSA2_PRO = 1;
            PSA2_BAL = 0;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 50:  // 5 s
            LED0 = 1;
            LED1 = 0;

            PSA1_IN = 1;
            PSA1_PRO = 0;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 1;
            PSA2_CLR = 0;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 0;

            COL2_IN = 0;
            break;       
    
        case 60:  // 6 s
            LED0 = 1;
            LED1 = 0;

            PSA1_IN = 1;
            PSA1_PRO = 1;
            PSA1_BAL = 0;
            PSA1_CLR = 0;

            PSA2_IN = 0;
            PSA2_PRO = 0;
            PSA2_BAL = 0;
            PSA2_CLR = 1;

            PROD_OUT = 1;
            PROD_PSA1 = 0;
            PROD_PSA2 = 1;

            COL2_IN = 0;
            break;       
    
    }
}

void pcCtrl()
{
    // u8 C0[2] = {"C0"}
    // u8 C1[2] = {"C1"}
    int t;
/*
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
*/
    // PSA1 
    if((USART_RX_BUF[0] == 0x50) && (USART_RX_BUF[3] == 0x31))
    {
        report[0] = 'P';
        report[1] = 'S';
        report[2] = 'A';
        report[3] = '1';
        report[4] = ' ';
        
        // IN 
        if(USART_RX_BUF[5] == 0x49)
        {
            port = &PSA1_IN;
            report[5] = 'I';
            report[6] = 'N';
            report[7] = ' ';
            report[8] = ' ';
        }
            
        // PRO 
        if(USART_RX_BUF[5] == 0x50)
        {
            port = &PSA1_PRO;
            report[5] = 'P';
            report[6] = 'R';
            report[7] = 'O';
            report[8] = ' ';
        }
        
        // BAL 
        if(USART_RX_BUF[5] == 0x42)
        {
            port = &PSA1_BAL;
            report[5] = 'B';
            report[6] = 'A';
            report[7] = 'L';
            report[8] = ' ';
        }

        // CLR 
        if(USART_RX_BUF[5] == 0x43)
        {
            port = &PSA1_CLR;
            report[5] = 'C';
            report[6] = 'L';
            report[7] = 'R';
            report[8] = ' ';
        }

        report[9] = ' ';
    }

    // PSA2
    if((USART_RX_BUF[0] == 0x50) && (USART_RX_BUF[3] == 0x32))
    {
        report[0] = 'P';
        report[1] = 'S';
        report[2] = 'A';
        report[3] = '2';
        report[4] = ' ';
        
        // IN 
        if(USART_RX_BUF[5] == 0x49)
        {
            port = &PSA2_IN;
            report[5] = 'I';
            report[6] = 'N';
            report[7] = ' ';
            report[8] = ' ';
        }
            
        // PRO 
        if(USART_RX_BUF[5] == 0x50)
        {
            port = &PSA2_PRO;
            report[5] = 'P';
            report[6] = 'R';
            report[7] = 'O';
            report[8] = ' ';
        }
        
        // BAL 
        if(USART_RX_BUF[5] == 0x42)
        {
            port = &PSA2_BAL;
            report[5] = 'B';
            report[6] = 'A';
            report[7] = 'L';
            report[8] = ' ';
        }

        // CLR 
        if(USART_RX_BUF[5] == 0x43)
        {
            port = &PSA2_CLR;
            report[5] = 'C';
            report[6] = 'L';
            report[7] = 'R';
            report[8] = ' ';
        }

        report[9] = ' ';
    }

    // PROD
    if((USART_RX_BUF[0] == 0x50) && (USART_RX_BUF[3] == 0x44))
    {
        report[0] = 'P';
        report[1] = 'R';
        report[2] = 'O';
        report[3] = 'D';
        report[4] = ' ';
        
        // OUT
        if(USART_RX_BUF[5] == 0x4F)
        {
            port = &PROD_OUT;
            report[5] = 'O';
            report[6] = 'U';
            report[7] = 'T';
            report[8] = ' ';
        }
            
        // PSA1
        if(USART_RX_BUF[8] == 0x31)
        {
            port = &PROD_PSA1;
            report[5] = 'P';
            report[6] = 'S';
            report[7] = 'A';
            report[8] = '1';
        }
        
        // PSA2
        if(USART_RX_BUF[8] == 0x32)
        {
            port = &PROD_PSA2;
            report[5] = 'P';
            report[6] = 'S';
            report[7] = 'A';
            report[8] = '2';
        }

        report[9] = ' ';
    }

    // COL2
    if((USART_RX_BUF[0] == 0x43) )
    {
        report[0] = 'C';
        report[1] = 'O';
        report[2] = 'L';
        report[3] = '2';
        report[4] = ' ';
        
        // IN
        if(USART_RX_BUF[5] == 0x49)
        {
            port = &PROD_OUT;
            report[5] = 'I';
            report[6] = 'N';
            report[7] = ' ';
            report[8] = ' ';
        }
        
        report[9] = ' ';
    }


    switch(USART_RX_BUF[10])
    {
        // case '0'
        case 0x30:
            *port = 0;
            // printf("port = 0\n");
            report[10] = '0';
            break;
        case 0x31:
            *port = 1;
            report[10] = '1';
            // printf("port = 1\n");
            break;
    }
    
    for( t = 0; t < 11; t++ )
    {
        // USART_SendData(USART1, report[t]);
        // while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);
        printf("%c", report[t]);
    }
    USART_RX_STA=0;

}

void portReport()
{
    // PSA1_IN
    if(PSA1_IN)
        printf("PSA1 IN   1");
    else
        printf("PSA1 IN   0");

    // PSA1_PRO
    if(PSA1_PRO)
        printf("PSA1 PRO  1");
    else
        printf("PSA1 PRO  0");

    // PSA1_BAL
    if(PSA1_BAL)
        printf("PSA1 BAL  1");
    else
        printf("PSA1 BAL  0");

    // PSA1_CLR
    if(PSA1_CLR)
        printf("PSA1 CLR  1");
    else
        printf("PSA1 CLR  0");

    // PSA2_IN
    if(PSA2_IN)
        printf("PSA2 IN   1");
    else
        printf("PSA2 IN   0");

    // PSA2_PRO
    if(PSA2_PRO)
        printf("PSA2 PRO  1");
    else
        printf("PSA2 PRO  0");

    // PSA2_BAL
    if(PSA2_BAL)
        printf("PSA2 BAL  1");
    else
        printf("PSA2 BAL  0");

    // PSA2_CLR
    if(PSA2_CLR)
        printf("PSA2 CLR  1");
    else
        printf("PSA2 CLR  0");

    // PRPD_OUT
    if(PROD_OUT)
        printf("PROD OUT  1");
    else
        printf("PROD OUT  0");

    // PRPD_PSA1
    if(PROD_PSA1)
        printf("PROD PSA1 1");
    else
        printf("PROD PSA1 0");

    // PRPD_PSA2
    if(PROD_PSA2)
        printf("PROD PSA2 1");
    else
        printf("PROD PSA2 0");

    // COL2_IN
    if(COL2_IN)
        printf("COL2 IN   1");
    else
        printf("COL2 IN   0");

}

int main()
{
    init();

    while(1)
    {
        if( *time_s > TIME_PERIOD )
        {
            *time_s = 0;
            cs = TIME_CONTROL_REPEAT;
            continue;
        }

        if(USART_RX_STA & 0x8000)
        {
            cs = PC_CONTROL;
        }

        switch(cs)
        {
            case TIME_CONTROL_START:
                timeCtrlstart();
                break;
            case TIME_CONTROL_REPEAT:
                // printf("TIME CONTROL \r\n");
                timeCtrlrepeat();
                // delay_ms(500);
                // report();
                break;
            case PC_CONTROL:
                pcCtrl();
                // cs = TIME_CONTROL_REPEAT;
                // report();
                // delay_ms(1000);
                break;
        }

        if((*time_s % 100) == 0)
            portReport();

        // LED0 =! LED0;
        // printf("\r\n %d \n", *time_s);
        // printf("\r\n %d \n", time_s);
        // delay_ms(1000);
    }
}
