#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "counts.h"

counts_t * createCounts(void) {
  counts_t * c = malloc(sizeof(*c));  
  c->one_count_array = malloc(sizeof(c->one_count_array));  
  c->len = 0;  
  c->n = 0;
  
  return c;
}

void addCount(counts_t * c, const char * name) {
  
  if (name == NULL) {    
    c->n++;    
  } else {    
    int in = 0;    
    int i;
    
    for (i = 0; i < c->len; i++) {      
      if (strcmp(name, c->one_count_array[i]->str) == 0) {	
		in = 1;	
		break; 	
      }      
    }
    
    if (in == 1) {      
      c->one_count_array[i]->count++;      
    } else {      
      c->len++;      
      c->one_count_array = realloc(c->one_count_array, c->len * sizeof(*c->one_count_array));      
      c->one_count_array[c->len - 1] = malloc(sizeof(one_count_t));      
      c->one_count_array[c->len - 1]->str = name;      
      c->one_count_array[c->len - 1]->count = 1;      
    }    
  }
}

void printCounts(counts_t * c, FILE * outFile) {
  for (int i = 0; i < c->len; i++) {    
    fprintf(outFile, "%s: %d\n", c->one_count_array[i]->str, c->one_count_array[i]->count);    
  }
  
  if (c->n > 0) {    
    fprintf(outFile, "<unknown> : %d\n", c->n);    
  }
}

void freeCounts(counts_t * c) {  
  for (int i = 0; i < c->len; i++) {    
    free(c->one_count_array[i]);    
  }  
  free(c->one_count_array);  
  free(c);
}
