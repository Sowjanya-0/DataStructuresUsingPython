class TreeNode(object): 
    def __init__(self,_val): 
        self.val = _val 
        self.left = None
        self.right = None
        self.height = 1
        
class AVL_Tree(object): 
    #steps:
    # 1)perform simple BST insertion
    # 2)modify the height 
    # 3)Get the Balancing Factor
    # 4)Balance The tree using required set of rotation to get balanced binary search tree,ie. AVL
    def insert(self, root, val): 
               
        #Simple Bst Insertion:
        if not root: 
            return TreeNode(val) 
        elif val < root.val: 
            root.left = self.insert(root.left, val) 
        else: 
            root.right = self.insert(root.right, val)
       
        # 2)modify the height      
        root.height = 1 + max(self.Height(root.left), self.Height(root.right)) 
        # 3)Get the Balancing Factor
        balance = self.check_Avl(root) 
        # 4)Balance The tree using required set of rotation
        
        #RR Rotation as tree is Left Skewed
        if balance > 1 and val < root.left.val: 
            return self.RR(root) 

        #LL Rotation as tree is Right Skewed
        if balance < -1 and val > root.right.val: 
            return self.LL(root) 
        #RL Rotation as tree is Left then Right Skewed
        if balance > 1 and val > root.left.val: 
            root.left = self.LL(root.left) 
            return self.RR(root) 
        #LR Rotation as tree is Right then Left Skewed
        if balance < -1 and val < root.right.val: 
            root.right = self.RR(root.right) 
            return self.LL(root) 
  
        return root 
     #LL Rotation
    def LL(self, node): 
       
        p = node.right 
        t = p.left
        #Rotations:
        p.left = node 
        node.right = t 
        #modify the heights: 
        node.height = 1 + max(self.Height(node.left), self.Height(node.right)) 
        p.height = 1 + max(self.Height(p.left), self.Height(p.right)) 
   
        return p 
    #LL Rotation
    def RR(self, node): 
  
        p = node.left 
        t = p.right
        #Rotations:
        p.right = node
        node.left = t 
        #modify the heights:
        node.height = 1 + max(self.Height(node.left), self.Height(node.right)) 
        p.height = 1 + max(self.Height(p.left), self.Height(p.right)) 
        return p 
    #Getting the Height
    def Height(self, root): 
        if not root: 
            return 0
  
        return root.height 
    #Getting the Balancing Factor
    def check_Avl(self, root): 
        if not root: 
            return 0
  
        return self.Height(root.left) - self.Height(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 


def insert_data(_data):
        mytree = AVL_Tree()
        root = None
        for i in _data:
            root = mytree.insert(root,i)
        print("Constructed AVL tree is:")
        mytree.preOrder(root)
        print()
        return root
def Search(root,val):
    if (root is None):
        return False
    elif (root.val == val):
        return True
    elif(root.val < val):
        return Search(root.right,val)
    return Search(root.left,val)
    return False

def main():
    root = insert_data([10,8,15,7,9,12,17,16,18,6,4])
    t = int(input('Enter the key to be searched:\t'))
    if(Search(root,t)):
        print()
        print('"Element found in AVL Tree"')
    else:
        print()
        print('"Element not found in AVL Tree"')
if __name__ == "__main__":
    main()
else:
    pass

