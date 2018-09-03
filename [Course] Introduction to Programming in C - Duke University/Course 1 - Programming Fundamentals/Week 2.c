// Week 2 - Practice Quiz: Variables and Expressions


// 1.
// For the following statements:

int x;
int y = x;

// Which one of the following best describes the error?


// The uninitialized variable x is used.


// 2.
// For the following statements:

int a1 = 2;
3 = a1;

// Which one of the following best describes the error?


// '3' is not an lvalue.


// 3.
// For the following statements:

int x = 3;
int y;
int z = x + 2 * 4;

// Which one of the following correctly depicts the state of the program after these statements 
// are executed?


// x = 3, y = ?, z = 11


// 4.
// For the following statements:

int a;
int b;
a = 5;
b = a % 2 - (a + 1) / 2;

// Which one of the following correctly depicts the state of the program after these statements 
// are executed?


// a = 5, b = -2


// Week 2 - Practice Quiz: Functions


// 1. 
// For the following code:

int myFunction(int n) {
  int x = n * 2;
  int y = (x + 1) % 3;
  return y - x;
}

// What does myFunction(4) evaluate to?


// -8


// 2. 
// For the following code:

int g (int x, int y) {
  x = x + y;
  int z = 2 * x - y;
  return z;
}

// What does g(-2, 5) evaluate to?


// 1


// Week 2 - Practice Quiz: Printing


// 1. 
// For the following code:

int a = -1;
int b = a * 5;
printf("a is %d, and b is %d.\n", a, b);

// What is the output?


// a is -1, and b is -5.


// 2. 
// For the following code:

int x = -1;
int y = 3;
x = x + y;
printf("x - y is %d.\n", x - y);

// What is the output?


// x - y is -1.


// Week 2 - Practice Quiz: Logical Operators


// 1. 
// Is the following expression true or false?

-1 * -2 == 14 % 4


// True


// 2. 
// Is the following conditional statement true or false?

int x = 6;
-3 < 5 || !(x % 3 == 0)


// True


// Week 2 - Practice Quiz: Conditional Statements


// 1. 
// Given the following code:

int g (int x, int y) {
  switch(x - y) {
  case 0:
    return x;
  case 4:
    y = y + 1;
    break;
  case 7:
    x = x - 1;
  case 9:
    return x*y;
  case 3:
    y = x + 9;
  default:
    return y - x;
  }
return y;
}

// What does g(14, 7) evaluate to?


// 91


// 2. 
// Consider the following code:

int f (int x, int y) {
  if (x + 2 < y) {
    x = x + 3;
    return y * x;
  }
  else {
    return x + y + 2;
  }
}

// What does f(5, 10) evaluate to?


// 80


// Week 2 - Practice Quiz: While Loops


// 1. 
// For the following code:

void f (int x, int y) {
  while (x < y) {
    printf("%d ", y - x);
    x = x + 1;
    y = y - 1;
  }
}

// What is the output for f(-1, 4)?


// 5 3 1


// Week 2 - Practice Quiz: Loops


// 1. 
// For the following code:

int f (int n) {
  int ans = 0;
  for (int i = 1; i < n; i++) {
    if (i < n/2) {
      ans -= i;
    }
    else {
      ans += i;
    }
  }
  return ans;
}

// What does f(7) evaluate to?

// Hint: don't forget that dividing integers results in an integer answer. For example, 9/4 = 2.


// 15


// 2. 
// Consider the following code:

int g (int x, int n) {
  for (int i = 0; i < n; i++) {
    if (i % 2 == 0) {
      x *= i + 1;
      continue;
    }
    x--;
    if (x == 0) {
      break;
    }
  }
  return x;
}

// What does g(2, 3) evaluate to?


// 3


// Week 2 - Quiz: Reading Code


// 1. 
// What is an lvalue?


// A value that can name a box.


// 2. 
// What does scope mean?


// The region of code in which a variable is visible.


// 3.
// Suppose you have the line of code:

int a = f(x,y);

// Which of the following best describes how you determine what value to put in the box for a?


// 1.Create a frame for f, copying the values of x and y into the boxes named for its 
// parameters.
// 2. Move the execution arrow into f, and execute code line by line.
// 3. When your execution arrow reaches a statement of the form return expression; the 
// value of that expression is what you will end up putting in the box for a (after you 
// destroy the frame, and return the execution arrow to the call site).


// 4. 
// If C did not have the keyword "for" but you wanted to write something where a for-loop were 
// the natural choice, what could you use instead?


// while


// 5. 
// What is the difference between printing a value and returning a value?


// Printing a value gives it to the user, while returning a value gives it to other code for 
// further computation.


// 6. 
// For the following erroneous code:

int f (int x) { 
  int answer = 0        
  for (int i = 0; i < X; i++) {  
    answer += i * i;             
  }                              
  return answer;

// What is the error on line 2?


// missing ;


// 7. 
// Execute the following code by hand:

int main (void) {
  int a = 2;
  int b = 6;
  while (a <= b) {
    if (a % 2 == 1) {
      printf("a is %d\n", a);
    }
    else {
      printf("b is %d\n", b);
      for (int i = 0; i < b - a ; i++) {
        printf("a * i + b = %d\n", a * i + b);
      }
    }
    a++;
    b--;
  }
  return 0;
}

// Which one of the following gives the correct output?


// b is 6
// a * i + b = 6
// a * i + b = 8
// a * i + b = 10
// a * i + b = 12
// a is 3
// b is 4


// 8. 
// Execute the following code by hand:

int anotherFunction(int a, int b) {
  int answer = 42;
  int x = 0;
  printf("In anotherFunction(%d,%d)\n",a,b);
  while (b > a) {
    printf("a is %d, b is %d\n", a, b);
    answer = answer + (b - a);
    b -= x;
    a += x / 2;
    x++;
  }
  return answer;
}

int someFunction(int x, int y) {
  int a = x + y;
  if (x < y) {
    for (int i = 0; i < x; i++) {
      printf("In the loop with i = %d, a = %d\n", i, a);
      a = a + x;
    }
  }
  else {
    y = anotherFunction(y,a+4);
  }
  return a * y;
}

int main(void) {
  int x = 2;
  int a = someFunction(x,3);
  printf("a = %d\n", a);
  printf("x = %d\n", x);
  return 0;
}

// Which one of the following gives the correct output?


// In the loop with i = 0, a = 5
// In the loop with i = 1, a = 7
// a = 27
// x = 2

