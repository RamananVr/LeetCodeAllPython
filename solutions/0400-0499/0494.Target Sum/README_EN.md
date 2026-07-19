---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0494.Target%20Sum/README_EN.md
tags:
    - Array
    - Dynamic Programming
    - Backtracking
---

<!-- problem:start -->

# [494. Target Sum](https://leetcode.com/problems/target-sum)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and an integer <code>target</code>.</p>

<p>You want to build an <strong>expression</strong> out of nums by adding one of the symbols <code>&#39;+&#39;</code> and <code>&#39;-&#39;</code> before each integer in nums and then concatenate all the integers.</p>

<ul>
	<li>For example, if <code>nums = [2, 1]</code>, you can add a <code>&#39;+&#39;</code> before <code>2</code> and a <code>&#39;-&#39;</code> before <code>1</code> and concatenate them to build the expression <code>&quot;+2-1&quot;</code>.</li>
</ul>

<p>Return the number of different <strong>expressions</strong> that you can build, which evaluates to <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], target = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1], target = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= sum(nums[i]) &lt;= 1000</code></li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

Let's denote the sum of all elements in the array $\textit{nums}$ as $s$, and the sum of elements to which we assign a negative sign as $x$. Therefore, the sum of elements with a positive sign is $s - x$. We have:

$$
(s - x) - x = \textit{target} \Rightarrow x = \frac{s - \textit{target}}{2}
$$

Since $x \geq 0$ and $x$ must be an integer, it follows that $s \geq \textit{target}$ and $s - \textit{target}$ must be even. If these two conditions are not met, we directly return $0$.

Next, we can transform the problem into: selecting several elements from the array $\textit{nums}$ such that the sum of these elements equals $\frac{s - \textit{target}}{2}$. We are asked how many ways there are to make such a selection.

We can use dynamic programming to solve this problem. Define $f[i][j]$ as the number of ways to select several elements from the first $i$ elements of the array $\textit{nums}$ such that the sum of these elements equals $j$.

For $\textit{nums}[i - 1]$, we have two choices: to select or not to select. If we do not select $\textit{nums}[i - 1]$, then $f[i][j] = f[i - 1][j]$; if we do select $\textit{nums}[i - 1]$, then $f[i][j] = f[i - 1][j - \textit{nums}[i - 1]]$. Therefore, the state transition equation is:

$$
f[i][j] = f[i - 1][j] + f[i - 1][j - \textit{nums}[i - 1]]
$$

This selection is based on the premise that $j \geq \textit{nums}[i - 1]$.

The final answer is $f[m][n]$, where $m$ is the length of the array $\textit{nums}$, and $n = \frac{s - \textit{target}}{2}$.

The time complexity is $O(m \times n)$, and the space complexity is $O(m \times n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target or (s - target) % 2:
            return 0
        m, n = len(nums), (s - target) // 2
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums, 1):
            for j in range(n + 1):
                f[i][j] = f[i - 1][j]
                if j >= x:
                    f[i][j] += f[i - 1][j - x]
        return f[m][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming (Space Optimization)

We can observe that in the state transition equation of Solution 1, the value of $f[i][j]$ is only related to $f[i - 1][j]$ and $f[i - 1][j - \textit{nums}[i - 1]]$. Therefore, we can eliminate the first dimension of the space and use only a one-dimensional array.

The time complexity is $O(m \times n)$, and the space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if s < target or (s - target) % 2:
            return 0
        n = (s - target) // 2
        f = [0] * (n + 1)
        f[0] = 1
        for x in nums:
            for j in range(n, x - 1, -1):
                f[j] += f[j - x]
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
