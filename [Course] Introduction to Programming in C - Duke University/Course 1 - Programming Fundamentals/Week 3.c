// Week 3 - Practice Quiz: Decimal, Hex, and Binary


// 1.
// What does hex mean?


// base 16


// 2.
// A number is 75 in decimal. What is the number in binary?


// 1001011


// 3.
// A number is 75 in decimal. What is the number in hex?


// 0x4B


// 4.
// A number is 0xA4F1 in hex. What number is this in decimal?


// 42225


// Week 3 - Practice Quiz: Basic Data Types


// 1.
// If the most significant bit of a signed integer is a 1, then what kind of number is it?


// Negative


// 2.
// Which one of the following could be represented with a float but not with an int?


// 4.2


// 3.
// What is the largest numerical value that can be represented by a char? (Give your answer as a 
// decimal integer.)


// 255



// 4.
// For the following variable declaration and initialization,

char c = 'E';

// What numerical value does the variable c have? (Give your answer as a decimal integer.)


// 69


// Week 3 - Practice Quiz: Expressions Have Types


// 1.
// Which of the following are true of "casting" a value? (Choose all that apply.)


// The original value is left unmodified
// You should do it rarely


// 2.
// For the following variable,

double x = 5.2;

// What type does the expression 14 + x have?


// double


// 3.
// Consider the following operation that overflows:

char c = 250;
c += 8;

// What value does c have after the above statements are executed? (Give your answer as a
// decimal integer.)


// 2


// Week 3 - Practice Quiz: "Non-numbers"


// 1.
// Which of the following are numbers to a computer? (Check all that apply.)


// Strings
// Video
// Characters
// Images


// 2.
// What is the purpose of a null terminator?


// To indicate the end of a string


// 3.
// How large is a string?


// Strings can have different sizes.


// Week 3 - Practice Quiz: Complex, Custom Data Types


// 1.
// What is a struct?


// A programming construct that bundles variables into a logical group


// 2.
// What does typedef do?


// Make another name for an existing type


// 3.
// For the following struct definition,

struct point_tag {
  double x;
  double y;
};
typedef struct point_tag point_t;

// Which of the following correctly declare a struct? (Choose all that apply.)


// struct point_tag myPoint;
// point_t myPoint;


// Week 3 - Quiz: Types


// 1.
// What is abstraction?


// The separation of what something does from how it does it.


// 2.
// What is a string?


// A sequence of characters


// 3.
// Which of the following is NOT determined by the type of a variable?


// The scope of the variable.


// 4.
// For the following code, assuming a short integer is 16 bits,

short y = 30000;
short x = y + 10000;

// Which one of the following best describes the types present?


// The expression y + 10000 is an integer, and overflow occurs assigning to the short x.


// 5.
// What is the value of the character '!' in binary?


// 00100001


// 6.
// What is the largest value that can be represented by a 32-bit int, expressed in hex? (Be sure to 
// prepend your answer with "0x")


// 0x7FFFFFFF


// 7.
// What is the output of the following code?

double d = 4.669;
printf("My number is %.2f.",d);


// My number is 4.67.


// 8.
// For the following code,

int x = 5;
double d1 = 11/x;
double d2 = 11/(double)x;

// What is the value of d1 – d2?


// -0.2


// 9.
// For the following code with an enumerated type,

enum fruit_tag {
  BLUEBERRY,
  BANANA,
  PINEAPPLE,
  WATERMELON
};
typedef enum fruit_tag fruit_t;

void printFruit(fruit_t myFruit) {
  switch(myFruit) {
    case BLUEBERRY:
      printf("a blueberry");
      break;
    case BANANA:
      printf("a banana");
      break;
    case PINEAPPLE:
      printf("a pineapple");
      break;
    case WATERMELON:
      printf("a watermelon");
      break;
  }
}

void compareFruit(fruit_t fruit1, fruit_t fruit2) {
  if (fruit1 > fruit2) {
    printFruit(fruit1);
    printf(" is larger than ");
    printFruit(fruit2);
  }
  else {
    printFruit(fruit1);
    printf(" is smaller than ");
    printFruit(fruit2);
  }
}

int main(void) {
  fruit_t myFruit = PINEAPPLE;
  fruit_t otherFruit = BLUEBERRY;
  compareFruit(myFruit, otherFruit);
  return 0;
}

// What is the output?


// a pineapple is larger than a blueberry


// 10.
// For the following code,

enum name_tag {
  BLUEBERRY,
  BANANA,
  PINEAPPLE,
  WATERMELON
};
typedef enum name_tag name_t;

struct fruit_tag {
  name_t name;
  double size;
};
typedef struct fruit_tag fruit_t;

fruit_t getBigger(fruit_t f, double d) {
  f.size += d;
  return f;
}

int main(void) {
  fruit_t myFruit;
  myFruit.name = BANANA;
  myFruit.size = 5.2;
  myFruit = getBigger(myFruit, 3.4);
  printf("This fruit is %.2f grams.\n", myFruit.size);
  return 0;
}

// What is the output?


// This fruit is 8.60 grams.
