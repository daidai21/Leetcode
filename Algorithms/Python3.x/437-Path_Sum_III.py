# dfs
# Runtime: 52 ms, faster than 100.00% of Python3 online submissions for Path Sum III.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Path Sum III.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        self.result = 0  # 定义全局结果
        cache = {0: 1}  # 定义全局路径
        self.dfs(root, sum, 0, cache)  # 递归来得到结果
        return self.result

    def dfs(self, root, sum, curr_path_sum, cache):
        if root is None: return  # 终止条件
        curr_path_sum += root.val  # 计算当前路径和
        old_path_sum = curr_path_sum - sum  # 必须的旧的路径和
        self.result += cache.get(old_path_sum, 0)  # 更新结果
        cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1  # 更新中间存储
        self.dfs(root.left, sum, curr_path_sum, cache)  # dfs分解
        self.dfs(root.right, sum, curr_path_sum, cache)
        cache[curr_path_sum] -= 1  # 当移动到其他分支时，当前路径和不再可用，因此删除一个


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        self.count = 0
        pre_dict = {0: 1}
        def dfs(p, sum, path_sum, pre_dict):
            if not p: return
            path_sum += p.val
            self.count += pre_dict.get(path_sum - sum, 0)
            pre_dict[path_sum] = pre_dict.get(path_sum, 0) + 1
            dfs(p.left, sum, path_sum, pre_dict)
            dfs(p.right, sum, path_sum, pre_dict)
            pre_dict[path_sum] -= 1

        dfs(root, sum, 0, pre_dict)
        return self.count


# dfs 找起点，每次以这个起点遍历
# Runtime: 860 ms, faster than 37.35% of Python3 online submissions for Path Sum III.
# Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Path Sum III.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: 'TreeNode', sum: 'int') -> 'int':
        self.num_of_path = 0
        self.dfs(root, sum)
        return self.num_of_path

    def dfs(self, node, sum):
        if node is None: return
        self.test(node, sum)
        self.dfs(node.left, sum)
        self.dfs(node.right, sum)

    def test(self, node, sum):
        if node is None: return
        if node.val == sum: self.num_of_path += 1
        self.test(node.left, sum - node.val)
        self.test(node.right, sum - node.val)
