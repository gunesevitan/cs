/*

 * 1.7
 
 * Compilers can have a profound impact on the performance of an application.
 * Assume that for a program, compiler A results in a dynamic instruction count of
 * 1.0E9 and has an execution time of 1.1 s, while compiler B results in a dynamic
 * instruction count of 1.2E9 and an execution time of 1.5 s.
 
 * a. Find the average CPI for each program given that the processor has a clock
 * cycle time of 1 ns.
 
 * b. Assume the compiled programs run on two different processors. If the execution
 * times on the two processors are the same, how much faster is the clock of the
 * processor running compiler A’s code versus the clock of the processor running 
 * compiler B’s code?
 
  * c. A new compiler is developed that uses only 6.0E8 instructions and has an 
  * average CPI of 1.1. What is the speedup of using this new compiler versus using
  * compiler A or B on the original processor?
 
 
 * Answer
 
 
 * Compiler A -> Execution Time = 1.1 s | Instructions = 1.0 * 10^9
 * Compiler B -> Execution Time = 1.5 s | Instructions = 1.2 * 10^9
  
 * a. 
 * 1 ns = 10^-9 s
 * CPI = Execution Time / (Instructions * Clock Cycle Time)
  
 * Compiler A -> 1.1 s / 1.0 * 10^9 Instructions * 10^-9 Clock Cycle Time s = 1.10 CPI 
 * Compiler B -> 1.5 s / 1.2 * 10^9 Instructions * 10^-9 Clock Cycle Time s = 1.25 CPI 
  
 * b. 
 * Execution Time = CPI * Instructions * Clock Cycle Time
 * Execution Time A = Execution Time B
 * CPI A * Instructions A * Clock Cycle Time P1 = CPI B * Instructions B * Clock Cycle Time P2
 
 * (Clock Cycle Time P1 / Clock Cycle Time P2) = (CPI B * Instructions B ) / (CPI A * Instructions A ) 
 * (1.25 CPI * 1.2 * 10^9 Instructions) / (1.1 CPI * 1.0 * 10^9 Instructions) = 1.36
 * Clock Cycle Time P1 = 1.36 * Clock Cycle Time P2 (P1 is 36% slower than P2)
 
 * c.
 * Compiler C -> CPI = 1.1 | Instructions = 6.0 * 10^8 
 * Execution Time = CPI * Instructions * Clock Cycle Time
 * 6.0 * 10^8 Instructions * 1.1 CPI * 10^-9 Clock Cycle Time = 0.66 s
 
 * Execution Time B / Execution Time C = 1.5 / 0.66 = 2.27
 * Execution Time A / Execution Time C = 1.1 / 0.66 = 1.67

 */