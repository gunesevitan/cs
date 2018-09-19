#include <stdio.h>
#include <stdlib.h>

unsigned int power(unsigned x, unsigned y);

unsigned int power(unsigned int x, unsigned int y){  
  if(x == 0 && y == 0){    
    return 1;    
  }
    
  if(y != 0){    
    return (x * power(x, y - 1));
  }else{    
    return 1;
  }
}
