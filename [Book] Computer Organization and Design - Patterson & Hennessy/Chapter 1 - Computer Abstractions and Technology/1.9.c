/*

 * 1.9
 
 * Assume for arithmetic, load/store, and branch instructions, a processor has
 * CPIs of 1, 12, and 5, respectively. Also assume that on a single processor a
 * program requires the execution of 2.56E9 arithmetic instructions, 1.28E9
 * load/store instructions, and 256 million branch instructions. Assume that
 * each processor has a 2 GHz clock frequency.
 
 * Assume that, as the program is parallelized to run over multiple cores, the
 * number of arithmetic and load/store instructions per processor is divided by
 * 0.7 x p (where p is the number of processors) but the number of branch instructions
 * per processor remains the same.
 
 * 1.9.1
 
 * Find the total execution time for this program on 1, 2, 4, and 8 processors, 
 * and show the relative speedup of the 2, 4, and 8 processor result relative to the
 * single processor result.
 
 * 1.9.2
 
 * If the CPI of the arithmetic instructions was doubled, what would the impact be
 * on the execution time of the program on 1, 2, 4, or 8 processors?
 
 * 1.9.3
 
 * To what should the CPI of load/store instructions be reduced in order for a single
 * processor to match the performance of four processors using the original CPI values?
 
 
 * Answer
 
 
 * Arithmetic Instructions
 * CPI = 1 | Instructions = 2.56E9 | Clock Rate = 2 GHz

 * Load/Store Instructions
 * CPI = 12 | Instructions = 1.28E9 | Clock Rate = 2 GHz
 
 * Branch Instructions
 * CPI = 5 | Instructions = 2.56E8 | Clock Rate = 2 GHz

  
 * 1.9.1
 
 * Execution Time = (Instructions * CPI) / Clock Rate
 
 * 1 Processor
 * Arithmetic Instructions -> (2.56E9 Instructions * 1 CPI) / 2E9 GHz = 1.28 s
 * Load/Store Instructions -> (1.28E9 Instructions * 12 CPI) / 2E9 GHz = 7.68 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 1 Processor = 9.60 s
 
 * 2 Processor
 * Arithmetic Instructions -> ((0.7 * 2) * 2.56E9 Instructions * 1 CPI) / 2E9 GHz = 0.91 s
 * Load/Store Instructions -> ((0.7 * 2) * 1.28E9 Instructions * 12 CPI) / 2E9 GHz = 5.49 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 2 Processor = 7.04 s (1.4 Speedup)
 
 * 4 Processor
 * Arithmetic Instructions -> ((0.7 * 4) * 2.56E9 Instructions * 1 CPI) / 2E9 GHz = 0.46 s
 * Load/Store Instructions -> ((0.7 * 4) * 1.28E9 Instructions * 12 CPI) / 2E9 GHz = 2.74 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 4 Processor = 3.84 s (2.5 Speedup)
 
 * 8 Processor
 * Arithmetic Instructions -> ((0.7 * 8) * 2.56E9 Instructions * 1 CPI) / 2E9 GHz = 0.23 s
 * Load/Store Instructions -> ((0.7 * 8) * 1.28E9 Instructions * 12 CPI) / 2E9 GHz = 1.37 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 8 Processor = 2.24 s (4.3 Speedup)
  
 * 1.9.2 
 
 * 1 Processor
 * Arithmetic Instructions -> (2.56E9 Instructions * 2 CPI) / 2E9 GHz = 2.56 s
 * Load/Store Instructions -> (1.28E9 Instructions * 12 CPI) / 2E9 GHz = 7.68 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 1 Processor = 10.88 s
 
 * 2 Processor
 * Arithmetic Instructions -> ((0.7 * 2) * 2.56E9 Instructions * 2 CPI) / 2E9 GHz = 1.83 s
 * Load/Store Instructions -> ((0.7 * 2) * 1.28E9 Instructions * 12 CPI) / 2E9 GHz = 5.49 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 2 Processor = 7.95 s
 
 * 4 Processor
 * Arithmetic Instructions -> ((0.7 * 4) * 2.56E9 Instructions * 2 CPI) / 2E9 GHz = 0.91 s
 * Load/Store Instructions -> ((0.7 * 4) * 1.28E9 Instructions * 12 CPI) / 2E9 GHz = 2.74 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 4 Processor = 4.30 s
 
 * 8 Processor
 * Arithmetic Instructions -> ((0.7 * 8) * 2.56E9 Instructions * 2 CPI) / 2E9 GHz = 0.46 s
 * Load/Store Instructions -> ((0.7 * 8) * 1.28E9 Instructions * 12 CPI) / 2E9 GHz = 1.37 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 8 Processor = 2.47 s
 
 * 1.9.3
 
 * 1 Processor
 * Arithmetic Instructions -> (2.56E9 Instructions * 1 CPI) / 2E9 GHz = 1.28 s
 * Load/Store Instructions -> (1.28E9 Instructions * 12 CPI) / 2E9 GHz = 7.68 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 1 Processor = 9.60 s
 
 * 4 Processor
 * Arithmetic Instructions -> ((0.7 * 4) * 2.56E9 Instructions * 1 CPI) / 2E9 GHz = 0.46 s
 * Load/Store Instructions -> ((0.7 * 4) * 1.28E9 Instructions * 12 CPI) / 2E9 GHz = 2.74 s
 * Branch Instructions -> (2.56E8 Instructions * 5 CPI) / 2E9 GHz = 0.64 s
 * Total Time with 4 Processor = 3.84 s
 
 * (1.28E9 * New CPI) / 2E9 GHz = 3.84 s (4 processor speed)
 * New CPI = 6.0
 * Old CPI reduced by %50
 
 */