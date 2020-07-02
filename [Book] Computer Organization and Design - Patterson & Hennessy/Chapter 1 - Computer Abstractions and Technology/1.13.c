/*

 * 1.13
 
 * Another pitfall cited in Section 1.10 is expecting to improve the overall performance 
 * of a computer by improving only one aspect of the computer. Consider a computer running 
 * a program that requires 250 s, with 70 s spent executing FP instructions, 85 s executed 
 * L/S instructions, and 40 s spent executing branch instructions.
 
 * 1.13.1
 
 * By how much is the total time reduced if the time for FP operations is reduced 
 * by 20%?
 
 * 1.13.2
 
 * By how much is the time for INT operations reduced if the total time is reduced 
 * by 20%?
 
 * 1.13.3
 
 * Can the total time can be reduced by 20% by reducing only the time for branch
 * instructions?
  
 
 * Answer
 
  
 * T = 250 s
 * FP Instructions = 70 s
 * L/S Instructions = 85 s
 * Branch Instructions = 40 s
 

 * 1.13.1
 
 * By how much is the total time reduced if the time for FP operations is reduced 
 * by 20%?
 
 * Time Reduced = 250 - 70 / 5 = 14 Seconds Reduced 
 
 * 1.13.2
 
 * By how much is the time for INT operations reduced if the total time is reduced 
 * by 20%?
 
 * Time Old = 250 | INT Operations 55 s | Other Operations 195 s
 * Time New = 200 | INT Operations 5 s | Other Operations 195 s
 
 * INT Operations are reduced from 55 to 5 seconds.
 
 * 1.13.3
 
 * Can the total time can be reduced by 20% by reducing only the time for branch
 * instructions?
 
 * Total Time after reduction by 20% = 200
 * Branch Instructions take 40 s
 
 * Even with %100 reduction on Branch Instructions, the total time will be 210 s.

 */