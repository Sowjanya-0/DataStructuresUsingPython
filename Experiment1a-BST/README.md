# Experiment 1
## Aim of the Experiment ---- 1.Write a program to perform the following operations:
a)Insert an element into a binary search tree.

### Step - by - Step Procedure for the Experiment:
1.if root is None:
2.   root = node
3. else:
4.   if root.data > node.data:
5.      if root.l_child is None:
6.         root.l_child = node
7.      else:
8.         binary_insert(root.l_child, node)
9.   else:
10.     if root.r_child is None:
11.        root.r_child = node
12.     else:
13.        binary_insert(root.r_child, node)
