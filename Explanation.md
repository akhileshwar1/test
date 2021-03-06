# I have divided the problem into two subproblems:
* Creating the priority score 2D matrix of size [m,n] from the given priority lists.
* Creating an arrangement 2D matrix of size [s,m] where every row pertains to a time slot where all the companies(columns) are interviewing simultaneously.



## Subproblem 1 is solved by Function score_map:

* Input: c_pr denotes company lists and s_pr denotes students lists.
For example, c_pr=[[1,2],[2,1]] and s_pr=[[1,2],[2,1]].
Here c_pr[0] is the list of company 1 and it says that it prefers student 1 over 2. Likewise, s_pr[0] is for student 1 saying he prefers company 1 over 2.

* Output: A matrix of size [m,n] where cell matrix[i][j] denotes the overall preference of the ith company and jth student for each other. For example,
          let's say that company 1 and student 1 rank each other at the starting index of their lists, the priority score at cell matrix[1][1] would then be                 1+1=2.

* Code: It starts with the outer loop that goes through all the company's lists. For every number coming out of list,
we find the corresponding student list and see where that particular company ranks for that student. We then add the company's rank in student's list+ student's rank in company's list and store
it in matrix[i][j].



## Subproblem2 is solved by function arrange:

* Input: a 2D score matrix outputted by the previous function.

* Output: an arrangement 2D matrix where every cell matrix[i][j] represents a tuple (a,b)
where a is the priority score and b is the number of the student being interviewed at slot i by company j. 

* Code: Firstly it converts every list in the score matrix into a binary MINheap. I use binary Minheap priority queue because it has **O(logn)** time to take the minimum and readjust.
It then creates an empty matrix of size [s,m] and loops over every cell and fills it with a tuple from the binary heap of that particular company
in such a way that a student is not repeated in a particular row or column of the matrix.

**Sample input and outputs are present in the code file under the comment samples.**



