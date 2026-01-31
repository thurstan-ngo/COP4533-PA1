# COP4533 Programming Assignment 1
Thurstan Ngo - 86963382  
Syed Rahman - 95234900

## Running the Matcher and Verifier
Type `python3 matcher_verifier.py` into the terminal to run the program
* This program has 2 modes: matcher and verifier
  * When prompted, type 1 for the matcher or 2 for the verifier; follow the additional prompts if needed  

Run `diff ex_out.txt output.txt` to compare the example output file and the output file created by the matcher

## Assumptions
* There are 2n lines after the first line of the input file
* For the input file, the first n lines are the hospitals' preference lists and the next n lines are the students' preference lists

## Task C
![Line graph for Task C](task-c.png)
* To evaluate the sacalability of our implementation we measured the running time for both our matching and verifier algorithms for increasing values of n.
* When looking at the graphs as n increases, the running time of the matcher and verifier also increase. This growth seems rapid and the shape appears parabolic.
* This quadratic behavior is expected as the Gale Shapely algorithm in the worst case can make n^2 proposals in the matching algorithm. The vierifier also checks unstable pairs using the preference list comparisons as well which also would scale on a order of n^2. Thus the trend from our graph is our algorithms are in order O(n^2)