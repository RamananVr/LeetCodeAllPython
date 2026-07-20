---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0746.Min%20Cost%20Climbing%20Stairs/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs)

## Description

<!-- description:start -->

<p>You are given an integer array <code>cost</code> where <code>cost[i]</code> is the cost of <code>i<sup>th</sup></code> step on a staircase. Once you pay the cost, you can either climb one or two steps.</p>

<p>You can either start from the step with index <code>0</code>, or the step with index <code>1</code>.</p>

<p>Return <em>the minimum cost to reach the top of the floor</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> cost = [10,<u>15</u>,20]
<strong>Output:</strong> 15
<strong>Explanation:</strong> You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> cost = [<u>1</u>,100,<u>1</u>,1,<u>1</u>,100,<u>1</u>,<u>1</u>,100,<u>1</u>]
<strong>Output:</strong> 6
<strong>Explanation:</strong> You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= cost.length &lt;= 1000</code></li>
	<li><code>0 &lt;= cost[i] &lt;= 999</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

We design a function $\textit{dfs}(i)$, which represents the minimum cost required to climb the stairs starting from the $i$-th step. Therefore, the answer is $\min(\textit{dfs}(0), \textit{dfs}(1))$.

The execution process of the function $\textit{dfs}(i)$ is as follows:

- If $i \ge \textit{len(cost)}$, it means the current position has exceeded the top of the stairs, and there is no need to climb further, so return $0$;
- Otherwise, we can choose to climb $1$ step with a cost of $\textit{cost}[i]$, then recursively call $\textit{dfs}(i + 1)$; or we can choose to climb $2$ steps with a cost of $\textit{cost}[i]$, then recursively call $\textit{dfs}(i + 2)$;
- Return the minimum cost between these two options.

To avoid repeated calculations, we use memoization search, saving the results that have already been calculated in an array or hash table.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{cost}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        return min(dfs(0), dfs(1))
```

<!-- tab:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We define $f[i]$ as the minimum cost needed to reach the $i$-th stair. Initially, $f[0] = f[1] = 0$, and the answer is $f[n]$.

When $i \ge 2$, we can reach the $i$-th stair directly from the $(i - 1)$-th stair with one step, or from the $(i - 2)$-th stair with two steps. Therefore, we have the state transition equation:

$$
f[i] = \min(f[i - 1] + \textit{cost}[i - 1], f[i - 2] + \textit{cost}[i - 2])
$$

The final answer is $f[n]$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{cost}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = min(f[i - 2] + cost[i - 2], f[i - 1] + cost[i - 1])
        return f[n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Dynamic Programming (Space Optimization)

We notice that the state transition equation for $f[i]$ only depends on $f[i - 1]$ and $f[i - 2]$. Therefore, we can use two variables $f$ and $g$ to alternately record the values of $f[i - 2]$ and $f[i - 1]$, thus optimizing the space complexity to $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f = g = 0
        for i in range(2, len(cost) + 1):
            f, g = g, min(f + cost[i - 2], g + cost[i - 1])
        return g
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
