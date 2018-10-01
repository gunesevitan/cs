#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kv.h"
#include "counts.h"
#include "outname.h"

char * removeNewline(char * c) {  
  char * pos;  
  pos = strchr(c, '\n');  
  *pos = '\0';  
  return c;  
}

counts_t * countFile(const char * filename, kvarray_t * kvPairs) {
  
  counts_t * c = createCounts();  
  FILE * f = fopen(filename, "r");  
  
  if (f == NULL) {    
    perror("fopen");    
    fprintf(stderr, "Could not open %s\n", filename);    
    return NULL;    
  } 
  
  char * line = NULL;  
  size_t size = 0;  
  char * key;  
  char * value;
  
  while(getline(&line, &size, f) > 0) {
    key = removeNewline(line);    
    value = lookupValue(kvPairs, key);        
    addCount(c, value);    
    free(line);    
    line = NULL;    
  }  
  free(line); 
  
  if (fclose(f) != 0) {    
    perror("fclose");    
    fprintf(stderr, "Could not close %s\n", filename);    
    return NULL;    
  }  
  return c;
}

int main(int argc, char ** argv) {

  if (argc < 3) {    
    fprintf(stderr, "Usage: count_values kvPairsFile listFile1 listFile2 ...\n");    
    exit(EXIT_FAILURE);    
  }
  
  kvarray_t * kv_pairs = readKVs(argv[1]);
  
  if (kv_pairs == NULL) {    
    fprintf(stderr, "argv[1] needs to be a file\n");    
    exit(EXIT_FAILURE);    
  }  
   
  for (int i = 2; i < argc; i++) {          
    counts_t * c = countFile(argv[i], kv_pairs);        
    char * outName = computeOutputFileName(argv[i]);  
    FILE * f = fopen(outName, "w");
    
    if (f == NULL) {      
      perror("fopen");      
      fprintf(stderr, "Could not open %s\n", outName);      
      exit(EXIT_FAILURE);      
    }    
      
    printCounts(c, f);
    
    if (fclose(f) != 0) {      
      perror("fclose");      
      fprintf(stderr, "Could not close %s\n", outName);      
      exit(EXIT_FAILURE);      
    }          
    free(outName);    
    freeCounts(c);    
  } 
  
  freeKVs(kv_pairs);
  return EXIT_SUCCESS;
}
