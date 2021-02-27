// Week 3 - Practice Quiz: Function Pointers


// 1.
// What is a function pointer?


// A pointer to the first instruction in a function


// 2.
// What is the most useful application of function pointers?


// As parameters to a function


// 3.
// How does the C library function qsort make use of function pointers?


// It takes a function pointer as a parameter specifying how to compare two elements.


// Week 3 - Practice Quiz: Security Hazards


// 1.
// Consider an attacker who writes a string input that contains machine instructions. When the
// string is read in, it overwrites an existing return address, causing the function to execute the
// malicious code.

// What type of security vulnerability is this?


// Buffer overflow


// 2.
// When is it acceptable to use gets?


// NEVER. Do not use gets.


// 3.
// What type of security vulnerability is described in this comic: https://xkcd.com/327/?


// Unsanitized inputs