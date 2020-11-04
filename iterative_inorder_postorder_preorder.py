# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



#Given a binary tree, return the inorder traversal of its nodes' values.
#Follow up: Recursive solution is trivial, could you do it iteratively?
# link : https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

TreeNode,List =0, [0]  # Extra 
class Solution:
    def inorderTraversal(self, root: TreeNode):
        ans = []
        lst = []
        if not root:
            return []
        while(lst or root):
            if root:
                lst.append(root)
                root = root.left
            else:
                root = lst.pop()
                ans.append(root.val)
                root = root.right
                
        return ans

## PREORDER
#Given a binary tree, return the preorder traversal of its nodes' values.
#Follow up: Recursive solution is trivial, could you do it iteratively?
#link : https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

class Solution2:
    def preorderTraversal(self, root: TreeNode):  # -> List[int]:
        lst = []
        if root:
            lst.append(root)
        ans = []
        while(lst):
            Head = lst.pop()
            if Head.right :
                lst.append(Head.right)
            if Head.left :
                lst.append(Head.left)
            ans.append(Head.val)
        return ans
            

#Given a binary tree, return the postorder traversal of its nodes' values.
#Follow up: Recursive solution is trivial, could you do it iteratively?
#link :https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/


# Given the root of a binary tree, return the postorder traversal of its nodes' values.
# Follow up: Recursive solution is trivial, could you do it iteratively?
# link : https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution3:
    def postorderTraversal(self, root: TreeNode):  # -> List[int]:
        stack1 = []
        stack2 = []
        # ans =[]
        if not root:
            return []
        stack1.append(root)
        while(stack1):
            root = stack1.pop()
            stack2.append(root)
            if root.left:
                stack1.append(root.left)
            if root.right:
                stack1.append(root.right)
        # while(stack2):
        #     ans.append(stack2.pop().val)
        return [root.val for root in  reversed(stack2)]



## TODO:
# MORRIS TRAVERSAL : WHICH HELPS TO REDUCE EXTRA SPACE COMPLEXITY (STACK OR WHATEVER)
#                    By chaging the shape of tree (either left skew or right skew)
#                    
            
        
 