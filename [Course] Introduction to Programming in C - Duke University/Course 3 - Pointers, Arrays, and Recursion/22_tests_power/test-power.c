#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

unsigned power(unsigned x, unsigned y);

void test_power(unsigned int base, unsigned int exponent, unsigned int answer){  
  if(power(base, exponent) != answer){    
    exit(EXIT_FAILURE);    
  }  
}

int main(){  
  test_power(0, 0, 1);  
  test_power(5, 2, 25);
  test_power(UINT_MAX, 1, UINT_MAX);
  
  exit(EXIT_SUCCESS);  
}
