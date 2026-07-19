---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1269.Number%20of%20Ways%20to%20Stay%20in%20the%20Same%20Place%20After%20Some%20Steps/README_EN.md
rating: 1854
source: Weekly Contest 164 Q4
tags:
    - Dynamic Programming
---

<!-- problem:start -->

# [1269. Number of Ways to Stay in the Same Place After Some Steps](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps)

## Description

<!-- description:start -->

<p>You have a pointer at index <code>0</code> in an array of size <code>arrLen</code>. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).</p>

<p>Given two integers <code>steps</code> and <code>arrLen</code>, return the number of ways such that your pointer is still at index <code>0</code> after <strong>exactly</strong> <code>steps</code> steps. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> steps = 3, arrLen = 2
<strong>Output:</strong> 4
<strong>Explanation: </strong>There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> steps = 2, arrLen = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> steps = 4, arrLen = 2
<strong>Output:</strong> 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= steps &lt;= 500</code></li>
	<li><code>1 &lt;= arrLen &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

We observe the data range of the problem and find that $steps$ does not exceed $500$, which means that we can only go to the right for up to $500$ steps.

We can design a function $dfs(i, j)$, which represents the number of schemes when we are currently at position $i$ and the remaining steps are $j$. So the answer is $dfs(0, steps)$.

The execution process of the function $dfs(i, j)$ is as follows:

1. If $i \gt j$ or $i \geq arrLen$ or $i \lt 0$ or $j \lt 0$, then return $0$.
1. If $i = 0$ and $j = 0$, then the pointer has stopped in place and there are no remaining steps, so return $1$.
1. Otherwise, we can choose to move one step to the left, one step to the right, or stay still, so return $dfs(i - 1, j - 1) + dfs(i + 1, j - 1) + dfs(i, j - 1)$. Note the modulo operation of the answer.

During the process, we can use memoization search to avoid repeated calculations.

The time complexity is $O(steps \times steps)$, and the space complexity is $O(steps \times steps)$. Where $steps$ is the number of steps given in the problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dfs(i, j):
            if i > j or i >= arrLen or i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            ans = 0
            for k in range(-1, 2):
                ans += dfs(i + k, j - 1)
                ans %= mod
            return ans

        mod = 10**9 + 7
        return dfs(0, steps)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
