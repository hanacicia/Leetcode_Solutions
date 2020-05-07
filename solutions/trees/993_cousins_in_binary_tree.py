993_cousins_in_binary_tree.py

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
      
        queue = [root]
        while 1:
            parent = []
            child_queue=[]
            stop_adding = False
            while queue:
                node = queue.pop()
                
                if node:
                    if node.left:
                        if node.left.val in set([x,y]):
                            parent.append(node.val)
                            stop_adding = True
                        elif stop_adding == False:
                            child_queue.append(node.left)
                    if node.right:
                        if node.right.val in set([x,y]):
                            print(node.right,node.val )
                            parent.append(node.val)
                            stop_adding = True
                        elif stop_adding == False:
                            child_queue.append(node.right)
            if len(set(parent)) ==2:
                return True
            elif len(parent)==0:
                queue = child_queue
            else:
                return False
            print(len(child_queue))
            if len(child_queue)==0:
                return False
