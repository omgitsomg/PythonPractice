# This is day 17 of Python practice.
# I decided to change things up. Instead of doing arrays,
# I want to refresh my knowledge on binary trees.
# Today's problems will all be about binary trees from leetcode

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# 1.
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
def preorderTraversal(self, root):
    preorderList = []

    #if root.left:
    #    preorderList.append(root.val)
    #    preorderList += preorderTraversal(root.left)
    #elif root.right:
    #    preorderList.append(root.val)
    #    preorderList += preorderTraversal(root.right)
    #elif not(root.right) and not(root.left):
    #    preorderList.append(root.val)
    #return preorderList
    # This is my first attempt


    # If the current root exists, then append the value of the root to the List.
    # After, the List will append the node on the left of the current node.
    # Next, it will append the node on the right of the current node.
    # root -> left subtree -> right subtree
    if root:
        preorderList.append(root.val)
        preorderList += self.preorderTraversal(root.left)
        preorderList += self.preorderTraversal(root.right)

    return preorderList

# 2.
# Given the root of a binary tree, return the inorder traversal of its nodes' values.
def inorderTraversal(self, root):
    inorderList = []
    

    # Vist the left subtree -> root -> right subtree
    if root:
         inorderList += self.inorderTraversal(root.left)
         inorderList.append(root.val)
         inorderList += self.inorderTraversal(root.right)
                
                
                
    return inorderList

# 3.
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

def postorderTraversal(self, root):

    postorderList = []    
    
    # Visit left subtree -> right subtree -> root
    if root:
        postorderList += self.postorderTraversal(root.left)
        postorderList += self.postorderTraversal(root.right)
        postorderList.append(root.val)
                
    return postorderList