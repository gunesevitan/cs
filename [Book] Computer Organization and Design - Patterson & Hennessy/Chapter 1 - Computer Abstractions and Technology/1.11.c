/*

 * 1.11
 
 * The results of the SPEC CPU2006 bzip2 benchmark running on an AMD 
 * Barcelona has an instruction count of 2.389E12, and execution time 
 * of 750 s and a reference time of 9650 s.
 
 * 1.11.1
 
 * Find the CPI if the clock cycle time is 0.333ns.
 
 * 1.11.2
 
 * Find the SPECratio.
 
 * 1.11.3
 
 * Find the increase in CPU time if the number of instructions of the 
 * benchmark is increased by 10% without affecting the CPI.
 
 * 1.11.4
 
 * Find the increase in CPU time if the number of instructions of the
 * benchmark is increased by 10% and CPI is increased by 5%.
 
 * 1.11.5
 
 * Find the change in the SPECratio for this change.
 
 * 1.11.6
 
 * Suppose that we are developing a new version of the AMD Barcelona 
 * processor with a 4GHz clock rate. We have added some additional
 * instructions to the instruction set in such a way that the number of
 * instructions has been reduced by 15%. The execution time is reduced to
 * 700 s and the new SPECratio is 13.7. Find the new CPI.
 
 * 1.11.7
 
 * This CPI value is larger than obtained in 1.11.1 as the clock rate was
 * increased from 3 GHz to 4 GHz. Determine whether the increase in the CPI
 * is similar to that of the clock rate. If they are dissimilar, why?
 
 * 1.11.8
 
 * By how much thas the CPU time been reduced?
 
 * 1.11.9
 
 * For a second benchmark, libquantum, assume an execution time of 960 ns, CPI 
 * of 1.61, and clock rate of 3 GHz. If the execution time is reduced by an 
 * additional 10% without affecting the CPI and with a clock rate of 4 GHz, 
 * determine the number of instructions.
 
 * 1.11.10
 
 * Determine the clock rate required to give a further 10% reduction in CPU time 
 * while maintaining the number of instructions and with the CPI unchanged.
 
 * 1.11.11
 
 * Determine the clock rate if the CPI is reduced by 15% and the CPU time by 20%
 * while the number of instructions is unchanged.
 
 
 * Answer
 
 
 * 1.11.1
 
 * Find the CPI if the clock cycle time is 0.333ns.
 
 * CPI = Execution Time * Clock Rate / Instructions
 * 0.333 ns = 3 GHz
 * 750 * 3 * 10^9 / 2.389E12 = 0.94 CPI 
 
 * 1.11.2 
 
 * Find the SPECratio.
 
 * SPECratio = Reference Time / Execution Time
 * 9650 / 750 = 12.8 SPECratio
 
 * 1.11.3
 
 * Find the increase in CPU time if the number of instructions of the 
 * benchmark is increased by 10% without affecting the CPI.
 
 * Execution Time = CPI * Instructions / Clock Rate
 * Instructions * 1.1 = New Instructions
 * If CPI doesn't change, the increase is %10.
 
 * 1.11.4
 
 * Find the increase in CPU time if the number of instructions of the
 * benchmark is increased by 10% and CPI is increased by 5%.
 
 * Instructions * 1.1 = New Instructions
 * CPI * 1.05 = New CPI
 * Execution Time = CPI * 1.05 * Instructions * 1.1 / Clock Rate 
 * If everything is assumed as 1 the original value is 1 and the increased value is 1.155
 * The increase from 1 to 1.155 is %15.5.
 
 * 1.11.5
 
 * Find the change in the SPECratio for this change.
 
 * SPECratio(old) / SPECratio(new) = CPU time(old) / CPU time(new)
 * 1 / 1.1555 = 0.86. SPECratio is decreased by 14%.
 
 * 1.11.6
 
 * Suppose that we are developing a new version of the AMD Barcelona 
 * processor with a 4GHz clock rate. We have added some additional
 * instructions to the instruction set in such a way that the number of
 * instructions has been reduced by 15%. The execution time is reduced to
 * 700 s and the new SPECratio is 13.7. Find the new CPI.
 
 * Instructions -> 2.389E12 * 0.85 = 2030 * 10^9 New Instructions
 * Clock Rate -> 4 GHz
 * Execution Time -> 700 s
 * SPECratio -> 13.7
 * CPI = Execution Time * Clock Rate / Instructions
 * 700 s * 4 * 10^9 GHz / 2.389E12 * 0.85 Instructions = 1.379 CPI
 
 * 1.11.7
 
 * This CPI value is larger than obtained in 1.11.1 as the clock rate was
 * increased from 3 GHz to 4 GHz. Determine whether the increase in the CPI
 * is similar to that of the clock rate. If they are dissimilar, why?
 
 * 4 GHz / 3 GHz = 1.33
 * 1.379 CPI / 0.94 CPI = 1.467
 * They are not similar because the instruction count is also changed.
 
 * 1.11.8
 
 * By how much thas the CPU time been reduced?
 
 * CPU Time Old = 750
 * CPU Time New = 700
 * 750 -> 700 = %6.67 decrease in CPU Time.
 
 * 1.11.9
 
 * For a second benchmark, libquantum, assume an execution time of 960 ns, CPI 
 * of 1.61, and clock rate of 3 GHz. If the execution time is reduced by an 
 * additional 10% without affecting the CPI and with a clock rate of 4 GHz, 
 * determine the number of instructions.
 
 * Execution Time = 960 * 0.9 = 864 ns
 * Clock Rate = 4 GHz
 * CPI = 1.61
 * Instructions = Execution Time * Clock Rate / CPI
 * 864 Execution Time * 4 * 10^9 / 1.61 CPI = 2146.5 * 10^9 Instructions
 
 * 1.11.10
 
 * Determine the clock rate required to give a further 10% reduction in CPU time 
 * while maintaining the number of instructions and with the CPI unchanged.
 
 * Execution Time = 960 * 0.9 = 864 ns
 * CPI = 1.61
 * Clock Rate = Instructions * CPI / Execution Time
 * 2146 * 10^9 Instructions * 1.61 CPI / 864 ns = 3.33 GHz
 
 * 1.11.11
 
 * Determine the clock rate if the CPI is reduced by 15% and the CPU time by 20%
 * while the number of instructions is unchanged.

 * Instructions = Execution Time * Clock Rate / CPI
 * 960 Execution Time * 3 * 10^9 GHz / 1.61 CPI = 1788 * 10^9 Instructions
 
 * CPI = 1.61 -> 1.36 (%15 Reduced)
 * Execution Time = 960 -> 768 (%20 Reduced)
 
 * Clock Rate = Instructions * CPI / Execution Time
 * 1788 * 10^9 Instructions * 1.36 Reduced CPI / 768 Reduced Time = 3.16 GHz Clock Rate
  
 */