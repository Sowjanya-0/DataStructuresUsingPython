# Experiment 1
## Aim of the Experiment ---- 1.Write a program to perform the following operations:
b)Delete an element from a binary search tree.

### Step - by - Step Procedure for the Experiment:
1.def deleteNode(root, key):
2.    if root is None:
3.        return root
4.    if key < root.key:
5.        root.left = deleteNode(root.left, key)
6.    elif(key > root.key):
7.        root.right = deleteNode(root.right, key)
8.    else:
9.        if root.left is None:
10.           temp = root.right
11.            root = None
12.           return temp
13.       elif root.right is None:
14.            temp = root.left
15.            root = None
16.            return temp
17.       temp = minValueNode(root.right)
18.        root.key = temp.key
19.        root.right = deleteNode(root.right, temp.key)
20.   return root
