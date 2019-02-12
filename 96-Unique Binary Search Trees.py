# 找规律，推公式
# (2n)! / ((n + 1)! * n!)
class Solution:
    def numTrees(self, n):
        return int(math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1)))


# dp
class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]


'''

//由1,2,3,...,n构建的二叉查找树，以i为根节点，左子树由[1,i-1]构成，其右子树由[i+1,n]构成。
//定义f(i)为以[1,i]能产生的Unique Binary Search Tree的数目
//若数组为空，则只有一种BST，即空树，f(0)=1;
//若数组仅有一个元素1，则只有一种BST，单个节点，f(1)=1;
//若数组有两个元素1，2，则有两种可能，f(2)=f(0)*f(1)+f(1)*f(0);
//若数组有三个元素1，2，3，则有f(3)=f(0)*f(2)+f(1)*f(1)+f(2)*f(0)
//由此可以得到递推公式：f(i)=f(0)*f(i-1)+...+f(k-1)*f(i-k)+...+f(i-1)*f(0)
'''
