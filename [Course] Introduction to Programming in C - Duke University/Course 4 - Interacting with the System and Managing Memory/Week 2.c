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















