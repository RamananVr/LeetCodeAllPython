---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2700-2799/2742.Painting%20the%20Walls/README_EN.md
rating: 2424
source: Weekly Contest 350 Q4
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [2742. Painting the Walls](https://leetcode.com/problems/painting-the-walls)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> integer arrays,&nbsp;<code>cost</code> and <code>time</code>, of size <code>n</code> representing the costs and the time taken to paint <code>n</code> different walls respectively. There are two painters available:</p>

<ul>
	<li>A<strong>&nbsp;paid painter</strong>&nbsp;that paints the <code>i<sup>th</sup></code> wall in <code>time[i]</code> units of time and takes <code>cost[i]</code> units of money.</li>
	<li>A<strong>&nbsp;free painter</strong> that paints&nbsp;<strong>any</strong> wall in <code>1</code> unit of time at a cost of <code>0</code>. But the&nbsp;free painter can only be used if the paid painter is already <strong>occupied</strong>.</li>
</ul>

<p>Return <em>the minimum amount of money required to paint the </em><code>n</code><em>&nbsp;walls.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> cost = [1,2,3,2], time = [1,2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The walls at index 0 and 1 will be painted by the paid painter, and it will take 3 units of time; meanwhile, the free painter will paint the walls at index 2 and 3, free of cost in 2 units of time. Thus, the total cost is 1 + 2 = 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> cost = [2,3,4,2], time = [1,1,1,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The walls at index 0 and 3 will be painted by the paid painter, and it will take 2 units of time; meanwhile, the free painter will paint the walls at index 1 and 2, free of cost in 2 units of time. Thus, the total cost is 2 + 2 = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= cost.length &lt;= 500</code></li>
	<li><code>cost.length == time.length</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= time[i] &lt;= 500</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memorization

We can consider whether each wall is painted by a paid painter or a free painter. Design a function $dfs(i, j)$, which means that from the $i$th wall, and the current remaining free painter working time is $j$, the minimum cost of painting all the remaining walls. Then the answer is $dfs(0, 0)$.

The calculation process of function $dfs(i, j)$ is as follows:

- If $n - i \le j$, it means that there are no more walls than the free painter's working time, so the remaining walls are painted by the free painter, and the cost is $0$;
- If $i \ge n$, return $+\infty$;
- Otherwise, if the $i$th wall is painted by a paid painter, the cost is $cost[i]$, then $dfs(i, j) = dfs(i + 1, j + time[i]) + cost[i]$; if the $i$th wall is painted by a free painter, the cost is $0$, then $dfs(i, j) = dfs(i + 1, j - 1)$.

Note that the parameter $j$ may be less than $0$. Therefore, in the actual coding process, except for the $Python$ language, we add an offset $n$ to $j$ so that the range of $j$ is $[0, 2n]$.

Time complexity $O(n^2)$, space complexity $O(n^2)$. Where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if n - i <= j:
                return 0
            if i >= n:
                return inf
            return min(dfs(i + 1, j + time[i]) + cost[i], dfs(i + 1, j - 1))

        n = len(cost)
        return dfs(0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
