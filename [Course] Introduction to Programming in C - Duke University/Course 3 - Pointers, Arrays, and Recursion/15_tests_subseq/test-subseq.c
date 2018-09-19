#include<stdio.h>
#include<stdlib.h>

size_t maxSeq(int *array, size_t n);

void test(int *array, size_t n, size_t correct_ans){  
  if (maxSeq(array,n) != correct_ans){    
    exit(EXIT_FAILURE);    
  }  
}

int main(){
  
  int array1[] ={1,2,3,4};  
  test(array1,4,4);
  
  int array2[] = {1,2,3,3,4,5};  
  test(array2,6,3); 
  
  int array3[] = {9,8,7,6,5};  
  test(array3,5,1);  
  
  int array4[] = {};  
  test(array4,0,0);
    
  int array5[] = {1};  
  test(array5, 1, 1);

  int array6[] = {1,2,-5,-4,-3};  
  test(array6, 5, 3);
 
  return(EXIT_SUCCESS);
}
