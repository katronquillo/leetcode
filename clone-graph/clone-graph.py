"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if (node is None):
            return node

        visited = set() # Set of original, fully copied nodes
        stack = deque() # Stack for DFS
        nodes = {} # Original Node : Copy Node 

        stack.append(node)
        while (len(stack) > 0):
            originalNode = stack.pop()

            if (originalNode in visited):
                continue

            visited.add(originalNode)
            
            if originalNode not in nodes:
                nodes[originalNode] = Node(originalNode.val)
            
            copyNode = nodes[originalNode]
            for neighbor in originalNode.neighbors:
                if (neighbor not in nodes):
                    nodes[neighbor] = Node(neighbor.val)
                copyNode.neighbors.append(nodes[neighbor])
                stack.append(neighbor)
        
        return nodes[node]


