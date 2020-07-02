// Week 2 - Practice Quiz: Compiling


// 1.
// What does the compiler do?


// Converts a program from human-readable source code to machine-readable
// instructions.


// 2.
// What is a function prototype?


// A declaration that informs the compilers of the name, return type, and parameter 
// types of a function that is defined elsewhere.


// 3.
// Which header file defines EXIT_SUCCESS and EXIT_FAILURE?


// stdlib.h


// 4.
// What is the return value from main used for?


// It informs the program that ran this program of its success or failure.


// Week 2 - Practice Quiz: Compilation Process


// 1.
// Which part of the compiler combines object files, libraries, and startup code to make an 
// executable binary?


// linker


// 2.
// What is in an object file?


// Machine-executable instructions.


// 3.
// What does the -o option to gcc do?


// Specifies the name of the output that gcc should produce.


// 4.
// If your code needs to make references to the largest value an integer can hold, why should 
// you use INT_MAX rather than writing 214783647?


// All of the above


// 5.
// If you have multiple compiler errors, what difficulties might you encounter in trying to fix the 
// later errors?


// The compiler may be confused by the earlier errors.


// Week 2 - Practice Quiz: Make and Valgrind


// 1.
// What tool is useful for building large programs with many source files?


// make


// 2.
// What tool is useful for finding memory errors?


// valgrind


// 3.
// For the following Makefile, which one of the following describes what line 1 means?

myProgram: oneFile.o anotherFile.o
    gcc -o myProgram oneFile.o anotherFile.o
oneFile.o: oneFile.c oneHeader.h someHeader.h 
    gcc -std=gnu99 -pedantic -Wall -c oneFile.c
anotherFile.o: anotherFile.c anotherHeader.h someHeader.h 
    gcc -std=gnu99 -pedantic -Wall -c anotherFile.c
	
	
// Compile myProgram from oneFile.o and anotherFile.o	


// 4.
// For the following Makefile, which one of the following describes what line 4 means?

myProgram: oneFile.o anotherFile.o
    gcc -o myProgram oneFile.o anotherFile.o
oneFile.o: oneFile.c oneHeader.h someHeader.h 
    gcc -std=gnu99 -pedantic -Wall -c oneFile.c
anotherFile.o: anotherFile.c anotherHeader.h someHeader.h 
    gcc -std=gnu99 -pedantic -Wall -c anotherFile.c
	
	
// Compile oneFile.c into an object file


// 5.
// If you valgrind your program and get the error "Conditional jump or move depends on 
// uninitialized value(s)," what should you do to get more information?


// Run valgrind with --track-origins=yes to determine the source of the error.
