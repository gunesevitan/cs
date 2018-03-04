/*

 * 1.10
 
 * Assume a 15 cm diameter wafer has a cost of 12, contains 84 dies, and has 
 * 0.02 defects/cm^2. Assume a 20 cm diameter wafer has a cost of 15, contains 100
 * dies, and has 0.031 defects/cm^2.
 
 * 1.10.1
 
 * Find the yield for both wafers
 
 * 1.10.2
 
 * Find the cost per good die for both wafers.
 
 * 1.10.3
 
 * If the number of dies per wafer is increased by 10% and the defects per area
 * unit increases by 15%, find the die area and yield.
 
 * 1.10.4
 
 * Assume a fabrication process improves the yield from 0.92 to 0.95. Find the 
 * defects per area unit for each version of the technology given a die area 
 * of 200 mm^2.
 
 
 * Answer
 
 
 * Cost per Die = Cost per Wafer / Dies per Wafer * Yied
 
 * Dies per Wafer = Wafer Area / Die Area 
 
 * Yield = 1 / (1 + (Defects per Area * Die Area / 2))^2
 
 * Die Area = (Diameter / 2)^2 * pi 

  
 * 1.10.1
 
 * Find the yield for both wafers
 
 * Wafer 1 -> 7.5^2 (r^2) * pi / 84 = 2.10 cm^2 Die Area
 * Wafer 2 -> 10^2 (r^2) * pi / 100 = 3.14 cm^2 Die Area
 
 * Wafer 1 -> 1 / (1 + (0.020 Defects/cm^2 * 2.10 cm^2 / 2))^2 = 95.9% Yield
 * Wafer 2 -> 1 / (1 + (0.031 Defects/cm^2 * 3.14 cm^2 / 2))^2 = 90.9% Yield
 
 * 1.10.2 
 
 * Find the cost per good die for both wafers.
 
 * Wafer 1 -> 12 Wafer Cost / 84 Dies per Wafer * 0.959 Yield = 0.136
 * Wafer 2 -> 15 Wafer Cost / 100 Dies per Wafer * 0.909 Yield = 0.136

 
 * 1.10.3
 
 * If the number of dies per wafer is increased by 10% and the defects per area
 * unit increases by 15%, find the die area and yield.
 
 * Wafer 1 -> 84 * 1.1 (%10 increase) = 92 New Dies per Wafer 
 * Wafer 2 -> 100 * 1.1 (%10 increase)= 110 New Dies per Wafer 
 
 * Wafer 1 -> 0.020 * 1.15 (%15 increase) = 0.023 New Defects/cm^2
 * Wafer 2 -> 0.031 * 1.15 (%15 increase) = 0.035 New Defects/cm^2
 
 * Wafer 1 -> 7.5^2 (r^2) * pi / 92 = 1.92 cm^2 Die Area
 * Wafer 2 -> 10^2 (r^2) * pi / 110 = 2.86 cm^2 Die Area
 
 * Wafer 1 -> 1 / (1 + (0.023 Defects/cm^2 * 1.92 cm^2 / 2))^2 = 95.7% New Yield
 * Wafer 2 -> 1 / (1 + (0.035 Defects/cm^2 * 2.86 cm^2 / 2))^2 = 90.7% New Yield
 
 * 1.10.4
 
 * Assume a fabrication process improves the yield from 0.92 to 0.95. Find the 
 * defects per area unit for each version of the technology given a die area 
 * of 200 mm^2.
 
 * New Die Area = 2 cm^2
 * Technology 1 Yield = 0.92
 * Technology 2 Yield = 0.95
 
 * Technology 1 -> (1 - 0.92^0.5) / (0.92^0.5 * 2 / 2) = 0.043 New Defects/cm2
 * Technology 2 -> (1 - 0.95^0.5) / (0.95^0.5 * 2 / 2) = 0.026 New Defects/cm2
  
 */