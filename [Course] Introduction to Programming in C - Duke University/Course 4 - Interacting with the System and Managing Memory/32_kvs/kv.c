#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "kv.h"


kvpair_t * get_pair(char * line) {
  
  char *key, *value;  
  kvpair_t * kv_pair = malloc(sizeof(*kv_pair)); 
  
  key = strsep(&line, "=");  
  value = strsep(&line, "\n");  
  kv_pair->key = strdup(key);  
  kv_pair->value = strdup(value);
  
  return kv_pair;  
}

void addPairToArray(kvarray_t * pairs, kvpair_t * kvpair) {  
  pairs->numPairs++;  
  pairs->kvpairs = realloc(pairs->kvpairs, pairs->numPairs * sizeof(*kvpair));  
  pairs->kvpairs[pairs->numPairs - 1] = kvpair;  
}

kvarray_t * readKVs(const char * fname) {

  FILE * f = fopen(fname, "r");
  
  if (f == NULL) {    
    perror("fopen");    
    fprintf(stderr, "Trying to open %s\n", fname);    
    return NULL;    
  } 
  
  kvarray_t * kv_array = malloc(sizeof(*kv_array));  
  kv_array->kvpairs = NULL;  
  kv_array->numPairs = 0;
  
  char * line = NULL;  
  size_t size = 0;
  
  while (getline(&line, &size, f) > 0) {    
    kvpair_t * kv_pair = get_pair(line);    
    addPairToArray(kv_array, kv_pair);    
    free(line);    
    line = NULL;    
  }
  
  free(line); 
  
  if (fclose(f) != 0) {    
    perror("fclose");    
    fprintf(stderr, "Trying to close %s\n", fname);    
    return NULL;    
  }  
  return kv_array;
}

void freeKVs(kvarray_t * pairs) {
  for (int i = 0; i < pairs->numPairs; i++) {    
    free(pairs->kvpairs[i]->key);    
    free(pairs->kvpairs[i]->value);    
    free(pairs->kvpairs[i]);    
  }  
  free(pairs->kvpairs);  
  free(pairs);
}

void printKVs(kvarray_t * pairs) {    
  for (int i = 0; i < pairs->numPairs; i++) {    
    printf("Key = '%s' Value = '%s'\n", pairs->kvpairs[i]->key, pairs->kvpairs[i]->value);    
  }
}

char * lookupValue(kvarray_t * pairs, const char * key) {
    
  for (int i = 0; i < pairs->numPairs; i++) {    
    if (strcmp(pairs->kvpairs[i]->key, key) == 0) {      
      return pairs->kvpairs[i]->value;      
    }    
  }  
  return NULL;  
}
