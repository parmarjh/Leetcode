# Link : https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#    3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Accepted :

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        Ans = []
        while stack1:
            for node in stack1:
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
                    
            Ans.append([node.val for node in stack1])
            stack1 = stack2
            stack2 = []
        return Ans

# Solution2
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack1 = [[root]]
        Ans = []
        while stack1[0]:
            for node in stack1[0]:
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
            Ans.append([node.val for node in stack1[0]])
            stack1 = [stack1[1:]]
        return Ans