/*

 * 1.8
 
 * The Pentium 4 Prescott processor, released in 2004, had a clock rate of 3.6
 * GHz and voltage of 1.25 V. Assume that, on average, it consumed 10 W of static
 * power and 90 W of dynamic power.
 
 * The Core i5 Ivy Bridge, released in 2012, has a clock rate of 3.4 GHz and voltage
 * of 0.9 V. Assume that, on average, it consumed 30 W of static power and 40 W of 
 * dynamic power.
 
 * 1.8.1
 
 * For each processor find the average capacitive loads.
 
 * 1.8.2
 
 * Find the percentage of the total dissipated power comprised by
 * static power and the ratio of static power to dynamic power for each technology.
 
 * 1.8.3
 
 * If the total dissipated power is to be reduced by 10%, how much 
 * should the voltage be reduced to maintain the same leakage current? 
 * Note: power is defined as the product of voltage and current.
 
 
 * Answer
 
 
 * Pentium 4 Presscott
 * Clock Rate = 3.6 GHz | Voltage = 1.25 V | Static Power = 10 W | Dynamic Power = 90 W
 
 * The Core i5 Ivy Bridge
 * Clock Rate = 3.4 GHz | Voltage = 0.90 V | Static Power = 30 W | Dynamic Power = 40 W
  
 * 1.8.1 
 
 * For each processor find the average capacitive loads.
 
 * Capacitive Load = 2 * Power / (Voltage^2 * Clock Rate)
  
 * Pentium 4 Presscott
 * Capacitive Load -> (2 * 90) / (3.6 GHz * 10^9 * 1.25^2 V ) = 3.2 * 10^-8
 
 * The Core i5 Ivy Bridge
 * Capacitive Load -> (2 * 40) / (3.4 GHz * 10^9 * 0.90^2 V ) = 2.9 * 10^-8
  
 * 1.8.2 
 
 * Find the percentage of the total dissipated power comprised by
 * static power and the ratio of static power to dynamic power for each technology.
 
 * Total Dissipated Power = Static Power + Dynamic Power
 
 * Pentium 4 Presscott 
 * Total Dissipated Power -> 10 Static Power + 90 Dynamic Power = 100
 * Ratio of Static Power to Dynamic Power -> 1/9
 
 * The Core i5 Ivy Bridge 
 * Total Dissipated Power -> 30 Static Power + 40 Dynamic Power = 70
 * Ratio of Static Power to Dynamic Power -> 3/4
 
 * 1.8.3
 
 * If the total dissipated power is to be reduced by 10%, how much 
 * should the voltage be reduced to maintain the same leakage current? 
 * Note: power is defined as the product of voltage and current.
 
 * Pentium 4 Presscott 
 * New Total Dissipated Power -> 0.9 * (10 Static Power + 90 Dynamic Power) = 90
 * New Static Power = 9 W | New Dynamic Power = 81 W
 
 * 3.2 * 10^-8 = (2 * 81) / (3.6 GHz * 10^9 * V^2 ) = 1.18 New Voltage

 * The Core i5 Ivy Bridge 
 * New Total Dissipated Power -> 0.9 * (30 Static Power + 40 Dynamic Power) = 63
 * New Static Power = 27 W | New Dynamic Power = 36 W
 
 * 2.9 * 10^-8 = (2 * 36) / (3.4 GHz * 10^9 * V^2 ) = 0.84 New Voltage
 
 */