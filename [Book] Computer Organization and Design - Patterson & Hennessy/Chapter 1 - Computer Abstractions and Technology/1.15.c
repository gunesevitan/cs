/*

 * 1.15
 
 
 * When a program is adapted to run on multiple processors in a multiprocessor
 * system, the execution time on each processor is comprised of computing time
 * and overhead time required for locked critical sections and/or to send data 
 * from one processor to another.
 
 * Assume a program requires t = 100 s of execution time on one processor. When 
 * run p processors, each processor requires t/p s, as well as an additional 4 s 
 * of overhead, irrespective of the number of processors. Compute the per-processor
 * execution time for 2, 4, 8, 16, 32, 64, and 128 processors. For each case, list 
 * the corresponding speedup relative to a single processor and the ratio between 
 * actual speedup versus ideal speedup (speedup if there was no overhead).
 
 
 * Answer
 
 * Processor 1 | Time 100 s | Time with Overhead 100 s| Speed Up 1.0 | Ideal Speed Up 1.0
 * Processor 2 | Time 50 s | Time with Overhead 54 s| Speed Up 1.85 | Ideal Speed Up 2.0
 * Processor 4 | Time 25 s | Time with Overhead 29 s| Speed Up 3.45 | Ideal Speed Up 4.0
 * Processor 8 | Time 12.5 s | Time with Overhead 16.5 s| Speed Up 6.06 | Ideal Speed Up 8.0 
 * Processor 16 | Time 6.25 s | Time with Overhead 10.25 s| Speed Up 9.76 | Ideal Speed Up 16.0
 * Processor 32 | Time 3.125 s | Time with Overhead 7.125 s| Speed Up 14.1 | Ideal Speed Up 32.0 
 * Processor 64 | Time 1.5625 s | Time with Overhead 5.5625 s| Speed Up 17.97 | Ideal Speed Up 64.0 
 * Processor 128 | Time 0.78125 s | Time with Overhead 4.78125 s| Speed Up 20.9 | Ideal Speed Up 128.0 
 
 */