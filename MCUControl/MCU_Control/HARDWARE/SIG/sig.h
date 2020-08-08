#ifndef __SIG_H
#define __SIG_H	 
#include "sys.h"

/* Initiate signal io, enable the clock of the io ports
 * signal io: PA[8], PB[8, 9], PC[0-7], PD[3, 6, 7], 
 * PE[2, 3, 6], PF[6, 7, 8], PG[6, 7, 8, 13, 14, 15]
 * sum 26 ports
 */

// PSA1 
#define PSA1_IN PCout(0)  // PC0
#define PSA1_PRO PCout(1)  // PC1	
#define PSA1_BAL PCout(2)  // PC2
#define PSA1_CLR PCout(3)  // PC3	

// PSA2 
#define PSA2_IN PCout(4)  // PC4
#define PSA2_PRO PCout(5)  // PC5	
#define PSA2_BAL PCout(6)  // PC6	
#define PSA2_CLR PCout(7)  // PC7	

// PROD
#define PROD_OUT PEout(2)  
#define PROD_PSA1 PEout(3)  	
#define PROD_PSA2 PEout(6)  	

// COL2
#define COL2_IN PBout(8)  	

void SIG_Init(void); 
		 				    
#endif
