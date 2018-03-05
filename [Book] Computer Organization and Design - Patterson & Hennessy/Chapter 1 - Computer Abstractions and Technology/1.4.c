/*

 * 1.4 
 
 * Assume a color display using 8 bits for each of the
 * primary colors (red, green, blue) per pixel and a frame
 * size of 1280 × 1024.
 
 * a. What is the minimum size in bytes of the frame buffer 
 * to store a frame?
 
 * b. How long would it take, at a minimum, for the frame to be
 * sent over a 100 Mbit/s network?
 
 
 * Answer
 
 
 * a. 
 * 1280 x 1024 pixels and 3 bytes (one for red,one for green and one for blue) 
 * 1280 * 1024 * 3 Bytes = 3 932 160 Bytes (3.9 MB)
 
 * b. 
 * 100 Mbit/s = 12.5 MB/s  
 * 3.9 MB / 12.5 MB/s = 0.312 s
 
 */