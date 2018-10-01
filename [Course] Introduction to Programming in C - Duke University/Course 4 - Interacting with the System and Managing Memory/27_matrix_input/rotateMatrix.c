#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int LINE_LENGTH = 12;
int MATRIX_DIM = 10;

void rotate(char matrix[10][10]);

void rotate(char matrix[10][10]){  
  for(int i=0; i<10;i++){    
    for(int j=10-1; j>=0;j--){      
      printf("%c", matrix[j][i]);      
    }    
    printf("\n");    
  }  
  exit(0);  
}

int main(int argc, char ** argv) {
  
  if (argc != 2) {    
    fprintf(stderr, "Usage: rotateMatrix inputFileName\n");    
    return EXIT_FAILURE;    
  }
  
  FILE * f = fopen(argv[1], "r");
    
  if (f == NULL) {    
    perror("Could not open file!");    
    return EXIT_FAILURE;    
  }
    
  int height = 0;
  char line[LINE_LENGTH];
  char matrix[MATRIX_DIM][MATRIX_DIM];
  
  while(fgets(line, LINE_LENGTH, f) != NULL) {       
    if (strchr(line, '\n') == NULL) {      
      fprintf(stderr, "Input matrix line (%d)'s width is more than 10 characters.\n", height);      
      return EXIT_FAILURE;      
    }
    
    
    int whereIsNL = 0;
    
    for (int n=0; n<LINE_LENGTH; n++) {      
      if (line[n] == '\n') {	
	whereIsNL = n;	
      }      
    }
    
    if (whereIsNL < 10) {      
      fprintf(stderr, "Input matrix line (%d)'s width is %d, which is less than 10 characters.\n", height, whereIsNL);      
      return EXIT_FAILURE;      
    }
    
    for (int i=0; i<10; i++) {      
      matrix[height][i] = line[i];      
    }  
    
    height++;    
  }
    
  if(height < MATRIX_DIM) {    
    fprintf(stderr, "Input matrix height is %d (which is too small), but should be 10.", height-1);    
    return EXIT_FAILURE;    
  }
  
    
  if (height > MATRIX_DIM) {    
    fprintf(stderr, "Input matrix height is %d (which is too big), but should be 10.\n", height-1);    
    return EXIT_FAILURE;    
  }
  
  
  if (fclose(f) != 0) {    
    perror("Failed to close the file!");    
    return EXIT_FAILURE;    
  }
     
  rotate(matrix);
  
  for (int r=0; r<MATRIX_DIM; r++) {    
    for (int c=0; c<MATRIX_DIM; c++) {      
      printf("%c", matrix[r][c]);      
    }    
    printf("\n");    
  }
    
  return EXIT_SUCCESS;  
}
