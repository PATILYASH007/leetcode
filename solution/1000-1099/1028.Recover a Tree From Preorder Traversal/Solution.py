# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        depth = 0
        num = 0
        S = traversal
        
        i = 0
        while i < len(S):
            depth = 0
            while i < len(S) and S[i] == '-':
                depth += 1
                i += 1

            num = 0
            while i < len(S) and S[i].isdigit():
                num = num * 10 + int(S[i])
                i += 1
            
            # Create the new node
            newNode = TreeNode(num)

            while len(stack) > depth:
                stack.pop()

            if stack:
                if not stack[-1].left:
                    stack[-1].left = newNode
                else:
                    stack[-1].right = newNode

            stack.append(newNode)
        return stack[0] if stack else None
