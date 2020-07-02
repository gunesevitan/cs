#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int len = 12;
int len = 10;

void rotate(char matrix[10][10]);

void rotate(char matrix[10][10]){  
  for(int i = 0; i < 10; i++){    
    for(int j = 9; j > =0; j--){      
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
  char line[len];
  char matrix[len][len];
  
  while(fgets(line, len, f) != NULL) {       
    if (strchr(line, '\n') == NULL) {      
      fprintf(stderr, "Input matrix line (%d)'s width is more than 10 characters.\n", height);      
      return EXIT_FAILURE;      
    }
        
    int nl_index = 0;
    
    for (int n = 0; n < len; n++) {      
      if (line[n] == '\n') {	
		nl_index = n;	
      }      
    }
    
    if (nl_index < 10) {      
      fprintf(stderr, "Input matrix line (%d)'s width is %d, which is less than 10 characters.\n", height, nl_index);      
      return EXIT_FAILURE;      
    }
    
    for (int i = 0; i < 10; i++) {      
      matrix[height][i] = line[i];      
    }      
    height++;    
  }
    
  if (height < len) {    
    fprintf(stderr, "Input matrix height is %d (which is too small), but should be 10.", height - 1);    
    return EXIT_FAILURE;    
  }
  
  if (height > len) {    
    fprintf(stderr, "Input matrix height is %d (which is too big), but should be 10.\n", height - 1);    
    return EXIT_FAILURE;    
  }  
  
  if (fclose(f) != 0) {    
    perror("Failed to close the file!");    
    return EXIT_FAILURE;    
  }
     
  rotate(matrix);
  
  for (int r = 0; r < len; r++) {    
    for (int c = 0; c < len; c++) {      
      printf("%c", matrix[r][c]);      
    }    
    printf("\n");    
  }
    
  return EXIT_SUCCESS;  
}
