"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #with help of hashmap and dfs(clone) we can create a clone of the graph
        oldtonew={}

        def clone(node):
            if node in oldtonew:
                return oldtonew[node]
            
            copy=Node(node.val)
            oldtonew[node]=copy

            for neigh in node.neighbors:
                copy.neighbors.append(clone(neigh))
            return copy

        return clone(node) if node else None

        