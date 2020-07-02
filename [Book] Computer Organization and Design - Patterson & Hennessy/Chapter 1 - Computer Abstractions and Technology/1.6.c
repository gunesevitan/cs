/*

 * 1.6
 
 * Consider two different implementations of the same instruction
 * set architecture. The instructions can be divided into four classes
 * according to their CPI (class A, B, C, and D). P1 with a clock rate
 * of 2.5 GHz and CPIs of 1, 2, 3, and 3, and P2 with a clock rate of 
 * 3 GHz and CPIs of 2, 2, 2, and 2.

 * Given a program with a dynamic instruction count of 1.0E6 instructions
 * divided into classes as follows: %10 class A, %20 class B, %50 class C,
 * and %20 class D, which is faster: P1 or P2?
 
 * a. What is the global CPI for each implementation?
 
 * b. Find the clock cycles required in both cases.
 
 
 * Answer
 
 
 * P1 -> CPI A = 1.0 | CPI B = 2.0 | CPI C = 3.0 | CPI D = 3.0 | Clock Rate = 2.5 GHz
 * P1 -> CPI A = 2.0 | CPI B = 2.0 | CPI C = 2.0 | CPI D = 2.0 | Clock Rate = 3.0 GHz
 
 * Instructions = 1.0E6
 * CPI A -> Instructions %10
 * CPI B -> Instructions %20
 * CPI C -> Instructions %50
 * CPI D -> Instructions %20
 
 * Time = (Instructions * CPI) / Clock Rate

 * P1 A -> (10^6 Instructions * 0.1 Factor * 1 CPI) / 2.5 GHz * 10^9 = 4.0 * 10^-5 s 
 * P1 B -> (10^6 Instructions * 0.2 Factor * 2 CPI) / 2.5 GHz * 10^9 = 1.6 * 10^-4 s 
 * P1 C -> (10^6 Instructions * 0.5 Factor * 3 CPI) / 2.5 GHz * 10^9 = 6.0 * 10^-4 s 
 * P1 D -> (10^6 Instructions * 0.2 Factor * 3 CPI) / 2.5 GHz * 10^9 = 2.4 * 10^-4 s 
 * P1 Total Time -> 1.04 * 10^-3 s
 
 * P2 A -> (10^6 Instructions * 0.1 Factor * 2 CPI) / 3.0 GHz * 10^9 = 6.7 * 10^-5 s 
 * P2 B -> (10^6 Instructions * 0.2 Factor * 2 CPI) / 3.0 GHz * 10^9 = 1.3 * 10^-4 s 
 * P2 C -> (10^6 Instructions * 0.5 Factor * 2 CPI) / 3.0 GHz * 10^9 = 3.3 * 10^-4 s 
 * P2 D -> (10^6 Instructions * 0.2 Factor * 2 CPI) / 3.0 GHz * 10^9 = 1.3 * 10^-4 s 
 * P2 Total Time -> 0.67 * 10^-3 s
 
 * P2 Total Time < P1 Total Time (P2 is faster)
 
 * a. 
 * CPI = (Clock Rate * Time) / Instructions
 
 * P1 -> (2.5 GHz * 10^9) * (1.04 * 10^-3 s) / 10^6 Instructions = 2.6 Global CPI 
 * P2 -> (3.0 GHz * 10^9) * (0.67 * 10^-3 s) / 10^6 Instructions = 2.0 Global CPI 
  
 * b. 
 * Clock Cycles = CPI * Instructions
 
 * P1 -> 2.6 Global CPI * 10^6 Instructions = 2.6 * 10^6 Clock Cycles
 * P2 -> 2.0 Global CPI * 10^6 Instructions = 2.0 * 10^6 Clock Cycles

 */