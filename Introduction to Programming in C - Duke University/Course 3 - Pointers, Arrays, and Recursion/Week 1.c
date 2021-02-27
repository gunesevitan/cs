// Week 1 - Practice Quiz: Pointers Conceptually


// 1.
// What is the value of x at the end of the following piece of code?

int x = 3;
int * p = &x;
*p = 4;


// 4


// 2.
// Which of the following describes the legality/illegality of this line of code:

int * b = 42;


// Illegal: The type of 42 is not the same as the type of b.


// 3.
// Conceptually, the & operator means...


// Give me an arrow pointing at


// Week 1 - Practice Quiz: Pointers Conceptually


// 1.
// We represent pointers conceptually as arrows, but everything is a number. What number is an 
// arrow?


// An address in memory


// 2.
// Where in memory are local variables stored?


// Stack


// 3.
// A pointer with value NULL has numeric value 0. What is placed at address 0?


// Nothing


// Week 1 - Practice Quiz: Pointers to Sophisticated Types


// 1.
// Assuming a is a pointer to a struct with field x, which one of the following has the same
// semantics (meaning) as (*a).x ?


// a->x


// 2.
// If we write &e, then e must be...


// An lvalue


// 3.
// For the following code:

const int * p = &x;

// Which one of the following will result in a compiler error?


// *p = 5;
