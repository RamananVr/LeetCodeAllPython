---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2200-2299/2297.Jump%20Game%20VIII/README_EN.md
tags:
    - Stack
    - Graph
    - Array
    - Dynamic Programming
    - Shortest Path
    - Monotonic Stack
---

<!-- problem:start -->

# [2297. Jump Game VIII 🔒](https://leetcode.com/problems/jump-game-viii)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code>. You are initially standing at index <code>0</code>. You can jump from index <code>i</code> to index <code>j</code> where <code>i &lt; j</code> if:</p>

<ul>
	<li><code>nums[i] &lt;= nums[j]</code> and <code>nums[k] &lt; nums[i]</code> for all indexes <code>k</code> in the range <code>i &lt; k &lt; j</code>, or</li>
	<li><code>nums[i] &gt; nums[j]</code> and <code>nums[k] &gt;= nums[i]</code> for all indexes <code>k</code> in the range <code>i &lt; k &lt; j</code>.</li>
</ul>

<p>You are also given an integer array <code>costs</code> of length <code>n</code> where <code>costs[i]</code> denotes the cost of jumping <strong>to</strong> index <code>i</code>.</p>

<p>Return <em>the <strong>minimum</strong> cost to jump to the index </em><code>n - 1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4,4,1], costs = [3,7,6,4,2]
<strong>Output:</strong> 8
<strong>Explanation:</strong> You start at index 0.
- Jump to index 2 with a cost of costs[2] = 6.
- Jump to index 4 with a cost of costs[4] = 2.
The total cost is 8. It can be proven that 8 is the minimum cost needed.
Two other possible paths are from index 0 -&gt; 1 -&gt; 4 and index 0 -&gt; 2 -&gt; 3 -&gt; 4.
These have a total cost of 9 and 12, respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,2], costs = [1,1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Start at index 0.
- Jump to index 1 with a cost of costs[1] = 1.
- Jump to index 2 with a cost of costs[2] = 1.
The total cost is 2. Note that you cannot jump directly from index 0 to index 2 because nums[0] &lt;= nums[1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length == costs.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i], costs[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack + Dynamic Programming

According to the problem description, we need to find the next position $j$ where $\textit{nums}[j]$ is greater than or equal to $\textit{nums}[i]$, and the next position $j$ where $\textit{nums}[j]$ is less than $\textit{nums}[i]$. We can use a monotonic stack to find these two positions in $O(n)$ time, and then construct an adjacency list $g$, where $g[i]$ represents the indices that index $i$ can jump to.

Then we use dynamic programming to find the minimum cost. Let $f[i]$ represent the minimum cost to jump to index $i$. Initially, $f[0] = 0$ and the rest $f[i] = \infty$. We enumerate the indices $i$ from small to large. For each $i$, we enumerate each index $j$ in $g[i]$ and perform the state transition $f[j] = \min(f[j], f[i] + \textit{costs}[j])$. The answer is $f[n - 1]$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        g = defaultdict(list)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] < nums[i]:
                stk.pop()
            if stk:
                g[i].append(stk[-1])
            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                g[i].append(stk[-1])
            stk.append(i)

        f = [inf] * n
        f[0] = 0
        for i in range(n):
            for j in g[i]:
                f[j] = min(f[j], f[i] + costs[j])
        return f[n - 1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
