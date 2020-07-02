// Week 1 - Practice Quiz: The Operating System


// 1.
// How does a program interact with "the outside world"?


// The program makes a system call.


// 2.
// What is errno?


// A global variable which stores a numeric code for the last error caused by a failed 
// system call


// 3.
// Which of the following is an activity that the program needs to ask the operating system to 
// perform for it? (Select ALL that are correct.)


// Read data from a file from the disk
// Send data over the Internet


// Week 1 - Practice Quiz: Command Line Arguments and Process Creation


// 1.
// How do you declare main if you want to access the program's command line arguments?


// int main(int argc, char ** argv)


// 2.
// What is in argv[0]?


// The name of the program.


// 3.
// What does fork do?


// Creates a copy of the current process.


// Week 1 - Practice Quiz: Opening Files and fgetc


// 1.
// How do you know if a call to fopen failed?


// If fopen fails, it returns NULL.


// 2.
// Suppose you wrote the following line of code

FILE * f = fopen("myfile.txt", "r");

// and the call to fopen succeeded. What is f's current position, immediately after this call to
// fopen?


// The start of the file.


// 3.
// Suppose you have

x = fgetc(f);

// What is the proper type of x?


// int


// Week 1 - Practice Quiz: Reading encryption.c


// 1.
// All three questions in this quiz refer to the following C program. Assume you have compiled it
// and have an executable named encrypt in your current directory.

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void encrypt(FILE * f, int key) {    
  int c;    
  while ((c = fgetc(f)) != EOF) {        
    if (isalpha(c)) {            
      c = tolower(c);            
      c -= 'a';            
      c += key;            
      c %= 26;            
      c += 'a';        
    }        
    printf("%c", c);    
  }
}

int main(int argc, char ** argv) {  
  if (argc != 3) {    
    fprintf(stderr,"Usage: encrypt key inputFileName\n");    
    return EXIT_FAILURE;  
  }  
  int key = atoi(argv[1]);  
  if (key == 0) {    
    fprintf(stderr,"Invalid key (%s): must be a non-zero integer\n", argv[1]);    
    return EXIT_FAILURE;  
  }  
  FILE * f = fopen(argv[2], "r");  
  if (f == NULL) {    
    perror("Could not open file");    
    return EXIT_FAILURE;  
  }  
  encrypt(f,key);  
  if (fclose(f) != 0) {    
    perror("Failed to close the input file!");    
    return EXIT_FAILURE;  
  }  
  return EXIT_SUCCESS;
}

// Assume also that you have a file input.txt with the following contents:

An example
Of the input.

// What will be printed to stderr if the command line input is:

./encrypt input.txt


// Usage: encrypt key inputFileName


// 2.
// What will be printed to stderr if the command line input is:

./encrypt 0 input.txt


// Invalid key (0): must be a non-zero integer


// 3.
// What will be printed to stdout if the command line input is:

./encrypt 7 input.txt


// hu lehtwsl vm aol puwba.


// Week 1 - Practice Quiz: Writing and Closing Files


// 1.
// Suppose that you write the following line of code:

FILE * f = fopen("myfile.txt", "w");

// Which of the following operations could you do successfully to f? (Select all that apply.)


// fclose
// fprintf


// 2.
// Which of the following accurately describes the similarities and differences between fputs 
// and fprintf?


// Both fputs and fprintf write strings to files. However, fprintf performs %-format
// conversion, while fputs does not.


// 3.
// Suppose your program opens a file, writes a lot of data into it, and then closes the file.

// If there is not enough space on the disk for all the data that you wrote, at what point is your 
// program guaranteed to know about the problem?


// When fclose returns.


// 4.
// UNIX and Linux simplify interaction with the outside world by (as much as possible) making
// everything look like a(n):


// File