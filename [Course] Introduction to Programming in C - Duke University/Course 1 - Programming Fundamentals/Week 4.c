// Week 4 - Peer-graded Assignment: Writing a Sorting Algorithm


// This peer-reviewed assignment is an opportunity for you to develop an algorithm of your own and have other learners execute it
// to give you feedback on its correctness and specificity.

// You will write an algorithm that sorts temperature data from least to greatest. To do this, you will work through the first four of
// the Seven Steps.

// When you have submitted a generalized algorithm, other learners will execute your algorithm on new data and give you 
// feedback on its correctness and specificity.


s = 0 (where the repetition starts)
N is the length of the list.


Repeat until start < N:
    1) current_smallest and i are assigned with s'th element in the list.
    2) Repeat until i < N:
        1) If the i'th element is lesser than current_smallest: 
                Then i'th element becomes the new current_smallest
        2) i = i + 1
    3) Swap the current_smallest with s'th element
    4) s = s + 1 