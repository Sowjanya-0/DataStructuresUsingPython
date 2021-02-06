# Experiment 1
## Aim of the Experiment ---- Write a program to perform the following operations:
c)Search for a key element in a binary search tree.

### Step - by - Step Procedure for the Experiment:
1.If root == NULL 
    return NULL;
2.If number == root->data 
    return root->data;
3.If number < root->data 
    return search(root->left)
4.If number > root->data 
    return search(root->right)
