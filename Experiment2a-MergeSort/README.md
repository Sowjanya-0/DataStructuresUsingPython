# Experiment 2
## Aim of the Experiment- Write a program for implementing the following sorting methods:
a)Merge sort
### Step-by-Step procedure for the experiment
1.MergeSort(A, p, r):
2.  if p > r 
3.      return
4.  q = (p+r)/2
5.  mergeSort(A, p, q)
6.  mergeSort(A, q+1, r)
7.  merge(A, p, q, r)
