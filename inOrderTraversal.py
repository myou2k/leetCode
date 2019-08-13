#In Order Traversal: https://leetcode.com/problems/binary-tree-inorder-traversal/

def inorderTraversal(self, root: TreeNode) -> List[int]:
    # /quote Trivial Recursive Solution /quote
    '''
    res = []
    def helper(root, res):
        if root != None:
            if root.left != None:
                helper(root.left, res)
            res.append(root.val)
            if root.right != None:
                helper(root.right, res)
    helper(root, res)
    return res
    '''
    #Implentation of iterative solution using stack
    stack = []
    res = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res