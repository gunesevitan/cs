#include <stdio.h>
#include <stdlib.h>

size_t maxSeq(int *array, size_t n);

void testMaxSeq(int * array, size_t n, size_t answer){
  if (maxSeq(array, n) < 0){    
    printf("Bug1.\n");    
    exit(EXIT_FAILURE);    
  }
    
  if (maxSeq(array, n) != answer){    
    printf("Bug2. maxSeq(array, %zu) calculated to be: %zu. Expected answer was: %zu.\n", n, maxSeq(array, n), answer);    
    exit(EXIT_FAILURE);    
  }
    
  if (n == 0 && maxSeq(array, n) != 0){    
    printf("Bug3. maxSeq (array, %zu) = %zu .\n", n, maxSeq(array, n));    
    exit(EXIT_FAILURE);    
  }
    
  if (sizeof(array[0]) != sizeof(int)){    
    printf("Bug4. Array of wrong types.\n");    
    exit(EXIT_FAILURE);    
  }  
  return;  
}

int main(void){  
  int ar1[10] = {1,2,1,3,5,7,2,4,6,9};  
  int ar2[0];  
  int ar3[5] = {0,0,0,0,0};  
  int ar4[13] = {1,2,3,4,5,6,7,8,9,10,11,12,13};  
  int ar5[11] = {10,9,8,7,6,5,4,3,2,1,0};  
  int ar6[5] = {2,1,31,106,5000};  
  int ar7[4] = {-20,-13,-4,0};  
  int ar8[7] = {-1,2,-6,-8,-90,-91,-103};
    
  testMaxSeq(ar1, 10, 4);  
  testMaxSeq(ar2, 0, 0);  
  testMaxSeq(ar3, 5, 1);  
  testMaxSeq(ar4, 13, 13;;  
  testMaxSeq(ar5, 10, 1);  
  testMaxSeq(ar6, 5, 4);  
  testMaxSeq(ar7, 4, 4);  
  testMaxSeq(ar8, 7, 2);
  
  return EXIT_SUCCESS;  
}

