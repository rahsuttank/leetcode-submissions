# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        ans = defaultdict(int)

        def dfs(node):
            if node is None:
                return 0
            tmp = 0
            # if node.left:
            tmp += dfs(node.left)
            tmp += dfs(node.right)
            tmp += node.val
            ans[tmp] += 1
            return tmp
        
        dfs(root)
        # res = []
        res = [key for key in ans.keys() if ans[key] == max(ans.values())]
        # print(maxKey)
        # for key, freq in ans.items():
        return res
            


            
        