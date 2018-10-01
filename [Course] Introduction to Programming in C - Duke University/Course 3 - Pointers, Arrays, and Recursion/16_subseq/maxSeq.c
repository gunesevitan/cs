#include <stdio.h>
#include <stdlib.h>

size_t maxSeq(int * array, size_t n){
	
  size_t number_of_increasing = 0;
  
  if (n == 0){    
    return number_of_increasing;    
  } else {
	  
	  size_t maxSeq = 1;    
		size_t currentMaxSeq = 1;    
    number_of_increasing = 1;   
    
    for (size_t i = 0; i < (n - 1); i++){      
      if(array[i] < array[i+1]){	
		number_of_increasing++;	
		currentMaxSeq = number_of_increasing;
		
		if(currentMaxSeq > maxSeq){	  
		  maxSeq = currentMaxSeq;	  
		}	
      } else{	
	number_of_increasing = 1;	
	currentMaxSeq = number_of_increasing;	
      }      
    }
    return maxSeq; 
  } 
}
