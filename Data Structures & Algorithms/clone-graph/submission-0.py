"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # brute force: copy each node and neighbors
        #    --> bottleneck when edge points to neighbors we've already seen
        #    --> we code have a mapping b/w each node and its clone
        
        # 1. return None for an empty graph
        if node is None:
            return None
        
        # 2. create a mapping between the original node --> clone
        clones = {}

        # 3. in DFS, we would return the existing clone if we've seen it before
        def clone(curr):
            if curr in clones:
                return clones[curr]
            
            # take a copy
            copy = Node(curr.val)
            clones[curr] = copy

            # each neighbor
            for nei in curr.neighbors:
                copy.neighbors.append(clone(nei))
            
            return copy
        
        return clone(node)
        # 4. otherwise, we'd create and store the clone

        # 5. for each neighbor, we clone and append
        # 6. then we return the clone of the starting node