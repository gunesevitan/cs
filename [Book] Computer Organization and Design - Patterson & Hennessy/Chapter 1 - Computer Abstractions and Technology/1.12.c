/*

 * 1.12
 
 * Section 1.10 cites as a pitfall the utilization of a subset of the performance
 * equation as a performance metric. To illustrate this, consider the following two
 * processors. P1 has a clock rate of 4 GHz, average CPI of 0.9, and requires the 
 * execution of 5.0E9 instructions. P2 has a clock rate of 3 GHz, an average CPI of
 * 0.75, and requires the execution of 1.0E9 instructions.
 
 * 1.12.1
 
 * One usual fallacy is to consider the computer with the largest clock rate as 
 * having the highest performance. Check if this is true for P1 and P2.
 
 * 1.12.2
 
 * Another fallacy is to consider that the processor executing the largest number
 * of instructions will need a larger CPU time. Considering that processor P1 is 
 * executing a sequence of 1.0E9 instructions and that the CPI of processors P1 
 * and P2 do not change, determine the number of instructions that P2 can execute 
 * in the same time that P1 needs to execute 1.0E9 instructions.
 
 * 1.12.3
 
 * A common fallacy is to use MIPS (millions of instructions per second) to compare
 * the performance of two different processors, and consider that the processor with 
 * the largest MIPS has the largest performance. Check if this is true for P1 and P2.
 
 * 1.12.4
 
 * Another common performance figure is MFLOPS (millions of floating-point operations
 * per second), defined as 
 
 * MFLOPS = No. FP operations / (execution time * 1E6) 
 
 * but this figure has the same problems as MIPS. Assume that 40% of the instructions 
 * executed on both P1 and P2 are floating-point instructions. Find the MFLOPS figures 
 * for the processors.
 
 
 * Answer
 
  
 * P1 -> Clock Rate = 4 GHz | CPI = 0.9 | Instructions = 5.0E9
 * P2 -> Clock Rate = 3 GHz | CPI = 0.75 | Instructions = 1.0E9
 

 * 1.12.1
 
 * One usual fallacy is to consider the computer with the largest clock rate as 
 * having the highest performance. Check if this is true for P1 and P2.
 
 * P1 Time -> 0.9 CPI * 5 * 10^9 Instructions / 4 * 10^9 Clock Rate = 1.125 seconds
 * P2 Time -> 0.75 CPI * 10^9 Instructions / 3 * 10^9 Clock Rate = 0.25 seconds
 
 * Computer with largest clock rate doesn't have the largest performance here,
 * because of its lower CPI and Instruction Count.
 
 * 1.12.2
 
 * Another fallacy is to consider that the processor executing the largest number
 * of instructions will need a larger CPU time. Considering that processor P1 is 
 * executing a sequence of 1.0E9 instructions and that the CPI of processors P1 
 * and P2 do not change, determine the number of instructions that P2 can execute 
 * in the same time that P1 needs to execute 1.0E9 instructions.
 
 * P1 Time -> 0.9 CPI * 10^9 Instructions / 4 * 10^9 Clock Rate = 0.225 seconds 
 * P2 Time -> 0.75 CPI * X Instructions / 3 * 10^9 Clock Rate = 0.225 seconds
 * P2 Instructions = 9.0E9 in 0.225 seconds (9 times bigger than P1)
 
 * 1.12.3
 
 * A common fallacy is to use MIPS (millions of instructions per second) to compare
 * the performance of two different processors, and consider that the processor with 
 * the largest MIPS has the largest performance. Check if this is true for P1 and P2.
 
 * P1 MIPS = 4 * 10^9 * 10^-6 / 0.9 CPI = 4,444
 * P2 MIPS = 3 * 10^9 * 10^-6 / 0.75 CPI = 4,000
 
 * P1 has the larger MIPS, but we already determined P2 has the greater performance.
 
 * 1.12.4
 
 * Another common performance figure is MFLOPS (millions of floating-point operations
 * per second), defined as 
 
 * MFLOPS = No. FP operations / (execution time * 1E6) 
 
 * but this figure has the same problems as MIPS. Assume that 40% of the instructions 
 * executed on both P1 and P2 are floating-point instructions. Find the MFLOPS figures 
 * for the processors.
 
 * P1 -> 4 GHz Clock Rate | 0.9 CPI | 2.0E9 FP Instructions | 3.0E9 Instructions
 * P2 -> 3 GHz Clock Rate | 0.75 CPI | 4.0E8 FP Instructions | 6.0E8 Instructions
 
 * P1 Time = 0.9 CPI * 5 * 10^9 Instructions / 4 * 10^9 GHz = 1.125 seconds 
 * P1 MFLOPS = 2 * 10^9 / 1.125 * 10^6 = 1,777
 
 * P2 Time = 0.75 CPI * 10^9 Instructions / 3 * 10^9 GHz = 0.25 seconds 
 * P2 MFLOPS = 4 * 10^8 / 0.25 * 10^6 = 1,600
 
 * P1 has the larger MFLOPS, but we already determined P2 has the greater performance.
  
 */