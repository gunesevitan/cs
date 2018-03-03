/*

 * 1.5
 
 * Consider three different processors, P1 P2 and P3, executing
 * the same instruction set. P1 has a 3 GHz clock rate and a CPI of 1.5.
 * P2 has a 2.5 GHz clock rate and a CPI of 1.0. P3 has a 4.0 GHz clock 
 * rate and a CPI of 2.2.
 
 * a. Which processor has the highest performance expressed in instructions 
 * per second?
 * b. If the processors each execute a program in 10 seconds, find the number of
 * cycles and the number of instructions.
 * c. We are trying to reduce the execution time by 30% but this leads to an
 * increase of 20% in the CPI. What clock rate should we have to get this time
 * reduction?
 
 
 * Answer
 
 
 * P1 -> CPI = 1.5 | Clock Rate = 3.0 GHz | Instructions = I
 * P2 -> CPI = 1.0 | Clock Rate = 2.5 GHz | Instructions = I
 * P3 -> CPI = 2.2 | Clock Rate = 4.0 GHz | Instructions = I 
 
 * a. 
 * Instructions per Second = Clock Rate / CPI * 10^9 
 
 * P1 -> 3.0 GHz / 1.5 * 10^9 = 2.0 * 10^9 Instructions per Second
 * P2 -> 2.5 GHz / 1.0 * 10^9 = 2.5 * 10^9 Instructions per Second
 * P3 -> 4.0 GHz / 2.2 * 10^9 = 1.8 * 10^9 Instructions per Second
 
 * P2 has the highest performance expressed in Instructions per Second.
 
 * b. 
 * Clock Cycles = Time * Clock Rate
 
 * P1 -> 3.0 GHz * 10 s = 3.0 * 10^10 Clock Cycles
 * P2 -> 2.5 GHz * 10 s = 2.5 * 10^10 Clock Cycles
 * P3 -> 4.0 GHz * 10 s = 4.0 * 10^10 Clock Cycles
 
 * Instructions = Clock Cycles / CPI
 
 * P1 -> 3.0 GHz * 10 / 1.5 CPI = 2.0 * 10^10 Instructions
 * P2 -> 2.5 GHz * 10 / 1.0 CPI = 2.5 * 10^10 Instructions
 * P3 -> 4.0 GHz * 10 / 2.2 CPI = 1.8 * 10^10 Instructions
 
 * c.
 * Time = (Instructions * CPI) / Clock Rate 
 * Time * 0.7 = (Instructions * CPI * 1.2) / (New Clock Rate)
 * New Clock Rate = Clock Rate * 1.2 / 0.7 = 1.71 * Clock Rate
 
 * P1 -> 3.0 GHz * 1.71 = 2.0 * 5.13 GHz
 * P2 -> 2.5 GHz * 1.71 = 2.5 * 4.27 GHz
 * P3 -> 4.0 GHz * 1.71 = 1.8 * 6.84 GHz 
 
 */