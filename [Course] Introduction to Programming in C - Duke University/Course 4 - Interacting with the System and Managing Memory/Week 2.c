// Week 2 - Practice Quiz: malloc


// 1.
// Where does malloc allocate memory?


// On the heap


// 2.
// What is the prototype for malloc?


// void * malloc(size_t size);


// 3.
// Suppose you want p to point at an array of 16 ints, which should be allocated by malloc.
// Which one of the following is the best way to declare and initialize p?


// int * p = malloc(16 * sizeof(*p));


// Week 2 - Practice Quiz: free


// 1.
// What does free(p) do?


// Frees the block of memory pointed to by p


// 2.
// Suppose you have the following code:

int * p = malloc(sizeof(int));
int * q = p;
free(p);
free(q);

// What problem does this code exhibit with regards to the use of free?


// This code double frees a block of memory


// 3.
// Suppose you have the following code:

int xcount = 0;
char * ptr = malloc(50 * sizeof(char));
if (fgets(ptr, 50, stdin) != NULL) {
  while(*ptr != '\0') {
    if (*ptr == 'x') {
      xcount++;
    }
    ptr++;
  }
}
free(ptr);

// What problems does this code exhibit with regards to the use of free?


// This code frees a pointer not returned by malloc


// 4.
// What does free(NULL) do?


// Nothing


// Week 2 - Practice Quiz: realloc


// 1.
// What does realloc do?


// Resizes a previously allocated block.


// 2.
// Suppose you had the following code:

int * p = malloc(12*sizeof(*p));
char * q = malloc(14*sizeof(*q));
char * m = q;
q++;
int ** ptr= &p;

// Which of the pointers in the above code could be passed as the first argument to a call to 
// realloc? (Select all that apply.)


// p
// m


// Week 2 - Practice Quiz: getline


// 1.
// Suppose you have the following code: 

size_t sz = 4; 
char * line = NULL;
getline(&line, &sz, stdin);

// Which one of the following describes what the getline call on line 3 will do?


// malloc an implementation-specific amount of space.


// 2.
// Suppose you have the following code (which is very slightly different from Q1's code):

size_t sz = 4; 
char * line = malloc(42 * sizeof(*line));
getline(&line, &sz, stdin);

// What will the call to getline on line 3 assume about the amount of space it has available to 
// read characters from stdin into?


// It will assume that there are at least 4 bytes.


// 3.
// Suppose you have the following code (which is very slightly different from the previous 
// questions' code):

size_t sz = 0; 
char * line = NULL;
getline(&line, &sz, stdin);

// Further suppose that when your program calls getline, the user enters

Hello


// (including the newline character).

// Which of the following will be true of sz after the call to getline returns?


// sz will be at least 7


// 4.
// In the same situation as Question 3, where you have this code:

size_t sz = 0 ; 
char * line = NULL;
getline(&line, &sz, stdin);

// and the user enters

Hello


// (including the newline character).

// Which of the following is true of line after the call to getline returns?


// linewill point at an array malloced to hold sz chars with 'H' 'e' 'l' 'l' 'o' '\n' '\0' in the
// first 7 characters. The value of any remaining elements of the array are undefined.


// Week 2 - Practice Quiz: Valgrind's Memcheck


// 1.
// A C programmer wrote the following code to try to read in many lines of numbers, sort them,
// and print the results. However, this code has a variety of memory-related errors.

#include <stdio.h>
#include <stdlib.h>
int cmplong(const void * vp1, const void * vp2) {
  const long * p1 = vp1;
  const long * p2 = vp2;
  return *p1 - *p2;
}
int main(void) {
  char * line= NULL;
  size_t sz =0;
  long * array = NULL;
  size_t n = 0;
  while(getline(&line, &sz, stdin) > 0){
    n++;
    array=realloc(array, n * sizeof(*array));
    array[n] = strtol(line, NULL, 0);
  }
  free(line);
  qsort(&array, n, sizeof(*array), cmplong);
  for (size_t i = 0; i < n; i++) {
    printf("%ld\n", array[i]);
    free(&array[i]);
  }
  return EXIT_SUCCESS;
}

// When the programmer runs this code in valgrind, the first error is

Invalid write of size 8
at 0x400788: main (broken.c:16)
Address 0x51fc108 is 0 bytes after a block of size 8 alloc'd
at 0x4C2AB80: malloc (in ...)
by 0x4C2CF1F: realloc (in ...)
by 0x400759: main (broken.c:15)

// Which one of the following best describes the invalid behavior that Valgrind has observed?


// Line 16 of this program attempted to write 8 bytes into an invalid memory location


// 2.
// In the previous question, the last part of valgrind's error message says:

Address 0x51fc108 is 0 bytes after a block of size 8 alloc'd
at 0x4C2AB80: malloc (in ...)
by 0x4C2CF1F: realloc (in ...)
by 0x400759: main (broken.c:15)

// Valgrind not only reported that the invalid address was 0x51fc108, but that it was "0 bytes 
// after a block of size 8 alloc'd..."

// What information is Valgrind providing with this part of the error message?


// The invalid address was immediately after a block of size 8 that was allocated by a 
// call to realloc on line 15 of this program.


// 3.
// Based on the information you gained from Valgrind, what would you change about this 
// program to fix the error discussed in the previous two questions?


// Change line 16 to:
array[n-1] = strtol(line, NULL, 0);


// 4.
// There are three other errors that Valgrind will identify with the code above. We encourage you
// to take a a few minutes to use Valgrind in the PPE to find and identify these errors as it is
// great practice with Valgrind.

// Run the code in valgrind, think about what it says, identify and repair the error, then run the
// program again in Valgrind. Once you have fixed all the errors, the program should work 
// correctly. It may help to draw some pictures of what the code is doing!

// How many errors were you able to find?


// 3
