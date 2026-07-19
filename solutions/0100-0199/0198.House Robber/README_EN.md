---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0198.House%20Robber/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [198. House Robber](https://leetcode.com/problems/house-robber)

## Description

<!-- description:start -->

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <b>without alerting the police</b></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

We design a function $\textit{dfs}(i)$, which represents the maximum amount of money that can be stolen starting from the $i$-th house. Thus, the answer is $\textit{dfs}(0)$.

The execution process of the function $\textit{dfs}(i)$ is as follows:

- If $i \ge \textit{len}(\textit{nums})$, it means all houses have been considered, and we directly return $0$;
- Otherwise, consider stealing from the $i$-th house, then $\textit{dfs}(i) = \textit{nums}[i] + \textit{dfs}(i+2)$; if not stealing from the $i$-th house, then $\textit{dfs}(i) = \textit{dfs}(i+1)$.
- Return $\max(\textit{nums}[i] + \textit{dfs}(i+2), \textit{dfs}(i+1))$.

To avoid repeated calculations, we use memoization search. The result of $\textit{dfs}(i)$ is saved in an array or hash table. Before each calculation, we first check if it has been calculated. If so, we directly return the result.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))

        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We define $f[i]$ as the maximum total amount that can be robbed from the first $i$ houses, initially $f[0]=0$, $f[1]=nums[0]$.

Consider the case where $i \gt 1$, the $i$th house has two options:

- Do not rob the $i$th house, the total amount of robbery is $f[i-1]$;
- Rob the $i$th house, the total amount of robbery is $f[i-2]+nums[i-1]$;

Therefore, we can get the state transition equation:

$$
f[i]=
\begin{cases}
0, & i=0 \\
nums[0], & i=1 \\
\max(f[i-1],f[i-2]+nums[i-1]), & i \gt 1
\end{cases}
$$

The final answer is $f[n]$, where $n$ is the length of the array.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        f[1] = nums[0]
        for i in range(2, n + 1):
            f[i] = max(f[i - 1], f[i - 2] + nums[i - 1])
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Dynamic Programming (Space Optimization)

We notice that when $i \gt 2$, $f[i]$ is only related to $f[i-1]$ and $f[i-2]$. Therefore, we can use two variables instead of an array to reduce the space complexity to $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        f = g = 0
        for x in nums:
            f, g = max(f, g), f + x
        return max(f, g)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
