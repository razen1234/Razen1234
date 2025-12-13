class Solution:
    def isSameTree(self, p, q):
        # If both trees are null, return true, because they're indetical
        if p is None and q is None:
            return True
        # If only one of the trees/nodes is None, return false 
        if p is None or q is None:
            return False
        # Checking if values of nodes are equal and checking right and left parts fo trees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If values aren't same, return False
        return False   
