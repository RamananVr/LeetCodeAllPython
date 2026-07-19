---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1478.Allocate%20Mailboxes/README_EN.md
rating: 2190
source: Biweekly Contest 28 Q4
tags:
    - Array
    - Math
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [1478. Allocate Mailboxes](https://leetcode.com/problems/allocate-mailboxes)

## Description

<!-- description:start -->

<p>Given the array <code>houses</code> where <code>houses[i]</code> is the location of the <code>i<sup>th</sup></code> house along a street and an integer <code>k</code>, allocate <code>k</code> mailboxes in the street.</p>

<p>Return <em>the <strong>minimum</strong> total distance between each house and its nearest mailbox</em>.</p>

<p>The test cases are generated so that the answer fits in a 32-bit integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1478.Allocate%20Mailboxes/images/sample_11_1816.png" style="width: 454px; height: 154px;" />
<pre>
<strong>Input:</strong> houses = [1,4,8,10,20], k = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1400-1499/1478.Allocate%20Mailboxes/images/sample_2_1816.png" style="width: 433px; height: 154px;" />
<pre>
<strong>Input:</strong> houses = [2,3,5,12,18], k = 2
<strong>Output:</strong> 9
<strong>Explanation:</strong> Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= houses.length &lt;= 100</code></li>
	<li><code>1 &lt;= houses[i] &lt;= 10<sup>4</sup></code></li>
	<li>All the integers of <code>houses</code> are <strong>unique</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ to represent the minimum total distance between the houses and their nearest mailbox, when placing $j$ mailboxes among the first $i+1$ houses. Initially, $f[i][j] = \infty$, and the final answer will be $f[n-1][k]$.

We can iterate over the last house $p$ controlled by the $j-1$-th mailbox, i.e., $0 \leq p \leq i-1$. The $j$-th mailbox will control the houses in the range $[p+1, \dots, i]$. Let $g[i][j]$ denote the minimum total distance when placing a mailbox for the houses in the range $[i, \dots, j]$. The state transition equation is:

$$
f[i][j] = \min_{0 \leq p \leq i-1} \{f[p][j-1] + g[p+1][i]\}
$$

where $g[i][j]$ is computed as follows:

$$
g[i][j] = g[i + 1][j - 1] + \textit{houses}[j] - \textit{houses}[i]
$$

The time complexity is $O(n^2 \times k)$, and the space complexity is $O(n^2)$, where $n$ is the number of houses.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        g = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = g[i + 1][j - 1] + houses[j] - houses[i]
        f = [[inf] * (k + 1) for _ in range(n)]
        for i in range(n):
            f[i][1] = g[0][i]
            for j in range(2, min(k + 1, i + 2)):
                for p in range(i):
                    f[i][j] = min(f[i][j], f[p][j - 1] + g[p + 1][i])
        return f[-1][k]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
