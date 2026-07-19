---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1500-1599/1595.Minimum%20Cost%20to%20Connect%20Two%20Groups%20of%20Points/README_EN.md
rating: 2537
source: Weekly Contest 207 Q4
tags:
    - Bit Manipulation
    - Array
    - Dynamic Programming
    - Bitmask
    - Matrix
---

<!-- problem:start -->

# [1595. Minimum Cost to Connect Two Groups of Points](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points)

## Description

<!-- description:start -->

<p>You are given two groups of points where the first group has <code>size<sub>1</sub></code> points, the second group has <code>size<sub>2</sub></code> points, and <code>size<sub>1</sub> &gt;= size<sub>2</sub></code>.</p>

<p>The <code>cost</code> of the connection between any two points are given in an <code>size<sub>1</sub> x size<sub>2</sub></code> matrix where <code>cost[i][j]</code> is the cost of connecting point <code>i</code> of the first group and point <code>j</code> of the second group. The groups are connected if <strong>each point in both groups is connected to one or more points in the opposite group</strong>. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.</p>

<p>Return <em>the minimum cost it takes to connect the two groups</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1595.Minimum%20Cost%20to%20Connect%20Two%20Groups%20of%20Points/images/ex1.jpg" style="width: 322px; height: 243px;" />
<pre>
<strong>Input:</strong> cost = [[15, 96], [36, 2]]
<strong>Output:</strong> 17
<strong>Explanation</strong>: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1500-1599/1595.Minimum%20Cost%20to%20Connect%20Two%20Groups%20of%20Points/images/ex2.jpg" style="width: 322px; height: 403px;" />
<pre>
<strong>Input:</strong> cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
<strong>Output:</strong> 4
<strong>Explanation</strong>: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
<strong>Output:</strong> 10
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>size<sub>1</sub> == cost.length</code></li>
	<li><code>size<sub>2</sub> == cost[i].length</code></li>
	<li><code>1 &lt;= size<sub>1</sub>, size<sub>2</sub> &lt;= 12</code></li>
	<li><code>size<sub>1</sub> &gt;= size<sub>2</sub></code></li>
	<li><code>0 &lt;= cost[i][j] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bitmask Dynamic Programming

Let $m$ and $n$ denote the number of points in the first group and the second group, respectively.

Since $1 \leq n \leq m \leq 12$, we can use an integer to represent the state of points in the second group — specifically, a binary integer of length $n$, where bit $k$ being $1$ means the $k$-th point in the second group is connected to some point in the first group, and $0$ means it is not.

Next, we define $f[i][j]$ as the minimum cost when the first $i$ points in the first group are all connected, and the state of points in the second group is $j$. Initially, $f[0][0] = 0$ and all other values are positive infinity. The answer is $f[m][2^n - 1]$.

Consider $f[i][j]$ where $i \geq 1$. We enumerate each point $k$ in the second group. If point $k$ is connected to the $i$-th point in the first group, we discuss the following two cases:

- If point $k$ is only connected to the $i$-th point in the first group, then $f[i][j]$ can be transitioned from $f[i][j \oplus 2^k]$ or $f[i - 1][j \oplus 2^k]$, where $\oplus$ denotes the XOR operation;
- If point $k$ is connected to the $i$-th point in the first group as well as other points, then $f[i][j]$ can be transitioned from $f[i - 1][j]$.

In both cases, we take the minimum transition value:

$$
f[i][j] = \min_{k \in \{0, 1, \cdots, n - 1\}} \{f[i][j \oplus 2^k], f[i - 1][j \oplus 2^k], f[i - 1][j]\} + cost[i - 1][k]
$$

Finally, we return $f[m][2^n - 1]$.

The time complexity is $O(m \times n \times 2^n)$ and the space complexity is $O(m \times 2^n)$, where $m$ and $n$ are the number of points in the first group and the second group, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        f = [[inf] * (1 << n) for _ in range(m + 1)]
        f[0][0] = 0
        for i in range(1, m + 1):
            for j in range(1 << n):
                for k in range(n):
                    if (j >> k & 1) == 0:
                        continue
                    c = cost[i - 1][k]
                    x = min(f[i][j ^ (1 << k)], f[i - 1][j], f[i - 1][j ^ (1 << k)]) + c
                    f[i][j] = min(f[i][j], x)
        return f[m][-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Bitmask Dynamic Programming (Space Optimization)

We notice that the transition of $f[i][j]$ only depends on $f[i - 1][\cdot]$ and $f[i][\cdot]$, so we can use a rolling array to optimize the space complexity down to $O(2^n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        f = [inf] * (1 << n)
        f[0] = 0
        g = f[:]
        for i in range(1, m + 1):
            for j in range(1 << n):
                g[j] = inf
                for k in range(n):
                    if (j >> k & 1) == 0:
                        continue
                    c = cost[i - 1][k]
                    x = min(g[j ^ (1 << k)], f[j], f[j ^ (1 << k)]) + c
                    g[j] = min(g[j], x)
            f = g[:]
        return f[-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
