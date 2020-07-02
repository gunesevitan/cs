/*

 * 1.14
 
 * Assume a program requires the execution of 50 x 10^6 FP instructions, 
 * 110 x 10^6 INT instructions, 80 x 10^6 L/S instructions, and 16 x 10^6 
 * branch instructions. The CPI for each type of instruction is 1, 1, 4, and 
 * 2, respectively. Assume the processor has a 2 GHz clock rate.
 
 * 1.14.1
 
 * By how much must we improve the CPI of FP instructions if we want the
 * program to run two times faster?
 
 * 1.14.2
 
 * By how much must we improve the CPI of L/S instructions if we want the 
 * program to run two times faster?
 
 * 1.14.3
 
 * By how much is the execution time of the program improved if the CPI of
 * INT and FP instructions is reduced by 40% and the CPI of L/S and Branch
 * is reduced by 30%?
  
 
 * Answer
 
  
 * FP Instructions -> 50 * 10^6
 * INT Instructions -> 110 * 10^6
 * L/S Instructions -> 80 * 10^6
 * Branch Instructions -> 16 * 10^6
 
 * Clock Rate -> 2 GHz
 

 * 1.14.1
 
 * By how much must we improve the CPI of FP instructions if we want the
 * program to run two times faster?
 
 * Total CPU Clock Cycles ->  50 * 10^6 + 110 * 10^6 + 80 * 10^6 * 4 + 16 * 10^6 * 2 = 512 * 10^6
 * Two times faster is basically half of the CPU Clock Cycles = 256 * 10^6
 * If CPI becomes 0, still the CPU Clock Cycles will be more than 256 * 10^6.
 * It's not possible to run this program two times faster.
 
 * 1.14.2
 
 * By how much must we improve the CPI of L/S instructions if we want the 
 * program to run two times faster?
 
 * Total CPU Cycles -> 512
 * L/S Cycles -> 320
 * Target CPU Cycles -> 256
 * Rest of the CPU Cycles -> 192
 
 * 192 + (320 * Factor) = 256
 * Factor = 0.5
 * CPI of the L/S instructions has to be improved  by 5 times.
 
 * 1.14.3
 
 * By how much is the execution time of the program improved if the CPI of
 * INT and FP instructions is reduced by 40% and the CPI of L/S and Branch
 * is reduced by 30%?
 
 * FP CPI -> 0.6
 * INT CPI -> 0.6
 * L/S CPI -> 2.8
 * Branch CPI -> 1.4
 
 * Total CPU Clock Cycles ->  50 * 10^6 * 0.6 + 110 * 10^6 * 0.6 + 80 * 10^6 * 2.8 + 16 * 10^6 * 1.4 = 342
 * Execution Time is improved from 512 to 342 which is 1.5 times.
 
 */