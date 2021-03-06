
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
    AUTO_START = 0,
    AUTO_REPEAT = 1,
    MANUAL = 2
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

    cs = AUTO_START;

    // second = &time_s;
    // time_s = TIM3_Int_Init(9999, 7199);
    time_s = TIM3_Int_Init(999, 7199);  // 0.1 s 计时
    // TIM3_Int_Init(9999, 7199, &time_s);

    // TIME_PERIOD = 140;
    port = NULL;
    // port = {&LED0, &LED1, 
    //         &SIGC0, &SIGC1, &SIGC2, &SIGC3, &SIGC4, 
    //         &SIGC5, &SIGC6, &SIGC7, &SIGC8, &SIGC9}
    // report = {0}

    LED0 = 1;
    LED1 = 1;
}

void ctrlDecide()
{
    if(USART_RX_STA & 0x8000)
    {
        // SET 
        if((USART_RX_BUF[0] == 0x53) && (USART_RX_BUF[1] == 0x45)
            && (USART_RX_BUF[2] == 0x54))
        {
            // START 
            if(USART_RX_BUF[4] == 0x53)
            {
                cs = AUTO_START;
                USART_RX_STA=0;
            }
            // REPEAT 
            else if(USART_RX_BUF[4] == 0x52)
            {
                cs = AUTO_REPEAT;
                USART_RX_STA=0;
            }
            // MANUAL 
            else if(USART_RX_BUF[4] == 0x4D)
            {
                cs = MANUAL;
                USART_RX_STA=0;
            }
        }
        else
        {
            cs = MANUAL;
        }

    }
}

void autoCtrlstart()
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

        case 141:  // over 14 s   
            *time_s = 0;
            cs = AUTO_REPEAT;
            break;
    
    }
}

void autoCtrlrepeat()
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

            COL2_IN = 1;
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

            COL2_IN = 1;
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

            COL2_IN = 1;
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

            COL2_IN = 1;
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

            COL2_IN = 1;
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

            COL2_IN = 1;
            break;    

        case 61:  // over 6 s
            *time_s = 0;
            cs = AUTO_REPEAT;
            break;
    }
}

void manualCtrl()
{
    int t;

    if(USART_RX_STA & 0x8000)
    {
        report[0] = '*';
        report[1] = ' ';
        // PSA1 
        if((USART_RX_BUF[0] == 0x50) && (USART_RX_BUF[3] == 0x31))
        {
            report[2] = 'P';
            report[3] = 'S';
            report[4] = 'A';
            report[5] = '1';
            report[6] = ' ';
            
            // IN 
            if(USART_RX_BUF[5] == 0x49)
            {
                port = &PSA1_IN;
                report[7] = 'I';
                report[8] = 'N';
                report[9] = ' ';
                report[10] = ' ';
            }
                
            // PRO 
            else if(USART_RX_BUF[5] == 0x50)
            {
                port = &PSA1_PRO;
                report[7] = 'P';
                report[8] = 'R';
                report[9] = 'O';
                report[10] = ' ';
            }
            
            // BAL 
            else if(USART_RX_BUF[5] == 0x42)
            {
                port = &PSA1_BAL;
                report[7] = 'B';
                report[8] = 'A';
                report[9] = 'L';
                report[10] = ' ';
            }

            // CLR 
            else if(USART_RX_BUF[5] == 0x43)
            {
                port = &PSA1_CLR;
                report[7] = 'C';
                report[8] = 'L';
                report[9] = 'R';
                report[10] = ' ';
            }

            report[11] = ' ';
        }

        // PSA2
        else if((USART_RX_BUF[0] == 0x50) && (USART_RX_BUF[3] == 0x32))
        {
            report[2] = 'P';
            report[3] = 'S';
            report[4] = 'A';
            report[5] = '2';
            report[6] = ' ';
            
            // IN 
            if(USART_RX_BUF[5] == 0x49)
            {
                port = &PSA2_IN;
                report[7] = 'I';
                report[8] = 'N';
                report[9] = ' ';
                report[10] = ' ';
            }
                
            // PRO 
            else if(USART_RX_BUF[5] == 0x50)
            {
                port = &PSA2_PRO;
                report[7] = 'P';
                report[8] = 'R';
                report[9] = 'O';
                report[10] = ' ';
            }
            
            // BAL 
            else if(USART_RX_BUF[5] == 0x42)
            {
                port = &PSA2_BAL;
                report[7] = 'B';
                report[8] = 'A';
                report[9] = 'L';
                report[10] = ' ';
            }

            // CLR 
            else if(USART_RX_BUF[5] == 0x43)
            {
                port = &PSA2_CLR;
                report[7] = 'C';
                report[8] = 'L';
                report[9] = 'R';
                report[10] = ' ';
            }

            report[11] = ' ';
        }

        // PROD
        else if((USART_RX_BUF[0] == 0x50) && (USART_RX_BUF[3] == 0x44))
        {
            report[2] = 'P';
            report[3] = 'R';
            report[4] = 'O';
            report[5] = 'D';
            report[6] = ' ';
            
            // OUT
            if(USART_RX_BUF[5] == 0x4F)
            {
                port = &PROD_OUT;
                report[7] = 'O';
                report[8] = 'U';
                report[9] = 'T';
                report[10] = ' ';
            }
                
            // PSA1
            else if(USART_RX_BUF[8] == 0x31)
            {
                port = &PROD_PSA1;
                report[7] = 'P';
                report[8] = 'S';
                report[9] = 'A';
                report[10] = '1';
            }
            
            // PSA2
            else if(USART_RX_BUF[8] == 0x32)
            {
                port = &PROD_PSA2;
                report[7] = 'P';
                report[8] = 'S';
                report[9] = 'A';
                report[10] = '2';
            }

            report[11] = ' ';
        }

        // COL2
        else if((USART_RX_BUF[0] == 0x43) )
        {
            report[2] = 'C';
            report[3] = 'O';
            report[4] = 'L';
            report[5] = '2';
            report[6] = ' ';
            
            // IN
            if(USART_RX_BUF[5] == 0x49)
            {
                port = &COL2_IN;
                report[7] = 'I';
                report[8] = 'N';
                report[9] = ' ';
                report[10] = ' ';
            }
            
            report[11] = ' ';
        }

        switch(USART_RX_BUF[10])
        {
            // case '0'
            case 0x30:
                *port = 0;
                // printf("port = 0\n");
                report[12] = '0';
                break;
            case 0x31:
                *port = 1;
                report[12] = '1';
                // printf("port = 1\n");
                break;
        }

        report[13] = ' ';
        report[14] = '*';
        
        for( t = 0; t < 15; t++ )
        {
            // USART_SendData(USART1, report[t]);
            // while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);
            printf("%c", report[t]);
        }
        
        if((USART_RX_BUF[0] == 0x53) && (USART_RX_BUF[1] == 0x45)
            && (USART_RX_BUF[2] == 0x54))
        {
            ctrlDecide();
        }

        USART_RX_STA=0;
    }
}


void portReport()
{
    // PSA1_IN
    if(PSA1_IN)
        printf("* PSA1 IN   1 *");
    else
        printf("* PSA1 IN   0 *");

    // PSA1_PRO
    if(PSA1_PRO)
        printf("* PSA1 PRO  1 *");
    else
        printf("* PSA1 PRO  0 *");

    // PSA1_BAL
    if(PSA1_BAL)
        printf("* PSA1 BAL  1 *");
    else
        printf("* PSA1 BAL  0 *");

    // PSA1_CLR
    if(PSA1_CLR)
        printf("* PSA1 CLR  1 *");
    else
        printf("* PSA1 CLR  0 *");

    // PSA2_IN
    if(PSA2_IN)
        printf("* PSA2 IN   1* ");
    else
        printf("* PSA2 IN   0 *");

    // PSA2_PRO
    if(PSA2_PRO)
        printf("* PSA2 PRO  1 *");
    else
        printf("* PSA2 PRO  0 *");

    // PSA2_BAL
    if(PSA2_BAL)
        printf("* PSA2 BAL  1 *");
    else
        printf("* PSA2 BAL  0 *");

    // PSA2_CLR
    if(PSA2_CLR)
        printf("* PSA2 CLR  1 *");
    else
        printf("* PSA2 CLR  0 *");

    // PRPD_OUT
    if(PROD_OUT)
        printf("* PROD OUT  1 *");
    else
        printf("* PROD OUT  0 *");

    // PRPD_PSA1
    if(PROD_PSA1)
        printf("* PROD PSA1 1 *");
    else
        printf("* PROD PSA1 0 *");

    // PRPD_PSA2
    if(PROD_PSA2)
        printf("* PROD PSA2 1 *");
    else
        printf("* PROD PSA2 0 *");

    // COL2_IN
    if(COL2_IN)
        printf("* COL2 IN   1 *");
    else
        printf("* COL2 IN   0 *");

}

void timeReport()
{
    // int t;
    // t = *time_s;
    printf("* TIME %u *", *time_s);
    // if(*time_s == 1)
    // {
    //     printf("TIME      1");
    // }
}

void controlReport()
{
    switch(cs)
    {
        case AUTO_START:
            printf("* CONTROL AUTO_START *");
            break;
        case AUTO_REPEAT:
            printf("* CONTROL AUTO_REPEAT *");
            break;
        case MANUAL:
            printf("* CONTROL MANUAL *");
            break;
    }

}

int main()
{
    init();

    while(1)
    {
        // if( *time_s > TIME_PERIOD )
        // {
        //     *time_s = 0;
        //     cs = TIME_CONTROL_REPEAT;
        //     continue;
        // }
        ctrlDecide();
        // printf("%d\n", cs);

        // if(USART_RX_STA & 0x8000)
        // {
        //     // cs = PC_CONTROL;
        //     ctrlDecide();
        // }

        switch(cs)
        {
            case AUTO_START:
                if(*time_s > 141)
                {
                    *time_s = 0;
                }
                autoCtrlstart();
                break;
            case AUTO_REPEAT:
                // printf("TIME CONTROL \r\n");
                if(*time_s > 61)
                {
                    *time_s = 0;
                }
                autoCtrlrepeat();
                // delay_ms(500);
                // report();
                break;
            case MANUAL:
                LED0 = 0;
                LED1 = 0;
                // while(USART_RX_BUF[0] == 0x00)
                // {
                //     ;
                // }
                manualCtrl();
                // cs = TIME_CONTROL_REPEAT;
                // report();
                // delay_ms(1000);
                break;
        }

        if((*time_s % 10) == 0)
            // printf("%d\n", *time_s);
            controlReport();
            portReport();
            timeReport();
            // ;

        // LED0 =! LED0;
        // printf("\r\n %d \n", *time_s);
        // printf("\r\n %d \n", time_s);
        // delay_ms(1000);
    }
}
