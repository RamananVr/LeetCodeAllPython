---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0983.Minimum%20Cost%20For%20Tickets/README_EN.md
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [983. Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets)

## Description

<!-- description:start -->

<p>You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array <code>days</code>. Each day is an integer from <code>1</code> to <code>365</code>.</p>

<p>Train tickets are sold in <strong>three different ways</strong>:</p>

<ul>
	<li>a <strong>1-day</strong> pass is sold for <code>costs[0]</code> dollars,</li>
	<li>a <strong>7-day</strong> pass is sold for <code>costs[1]</code> dollars, and</li>
	<li>a <strong>30-day</strong> pass is sold for <code>costs[2]</code> dollars.</li>
</ul>

<p>The passes allow that many days of consecutive travel.</p>

<ul>
	<li>For example, if we get a <strong>7-day</strong> pass on day <code>2</code>, then we can travel for <code>7</code> days: <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, <code>6</code>, <code>7</code>, and <code>8</code>.</li>
</ul>

<p>Return <em>the minimum number of dollars you need to travel every day in the given list of days</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> days = [1,4,6,7,8,20], costs = [2,7,15]
<strong>Output:</strong> 11
<strong>Explanation:</strong> For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
<strong>Output:</strong> 17
<strong>Explanation:</strong> For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= days.length &lt;= 365</code></li>
	<li><code>1 &lt;= days[i] &lt;= 365</code></li>
	<li><code>days</code> is in strictly increasing order.</li>
	<li><code>costs.length == 3</code></li>
	<li><code>1 &lt;= costs[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search + Binary Search

We define a function $\textit{dfs(i)}$, which represents the minimum cost required from the $i$-th trip to the last trip. Thus, the answer is $\textit{dfs(0)}$.

The execution process of the function $\textit{dfs(i)}$ is as follows:

- If $i \geq n$, it means all trips have ended, return $0$;
- Otherwise, we need to consider three types of purchases: buying a 1-day pass, buying a 7-day pass, and buying a 30-day pass. We calculate the cost for these three purchasing methods separately and use binary search to find the index $j$ of the next trip, then recursively call $\textit{dfs(j)}$, and finally return the minimum cost among these three purchasing methods.

To avoid repeated calculations, we use memoization search to save the results that have already been calculated.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ represents the number of trips.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            ans = inf
            for c, v in zip(costs, valid):
                j = bisect_left(days, days[i] + v)
                ans = min(ans, c + dfs(j))
            return ans

        n = len(days)
        valid = [1, 7, 30]
        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

Let's denote the last day in the $\textit{days}$ array as $m$. We can define an array $f$ of length $m + 1$, where $f[i]$ represents the minimum cost from day $1$ to day $i$.

We can calculate the value of $f[i]$ in increasing order of the dates in the $\textit{days}$ array, starting from day $1$. If day $i$ is a travel day, we can consider three purchasing options: buying a 1-day pass, buying a 7-day pass, and buying a 30-day pass. We calculate the cost for these three purchasing methods separately and take the minimum cost among these three as the value of $f[i]$. If day $i$ is not a travel day, then $f[i] = f[i - 1]$.

The final answer is $f[m]$.

The time complexity is $O(m)$, and the space complexity is $O(m)$. Here, $m$ represents the last day of travel.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        m = days[-1]
        f = [0] * (m + 1)
        valid = [1, 7, 30]
        j = 0
        for i in range(1, m + 1):
            if i == days[j]:
                f[i] = inf
                for c, v in zip(costs, valid):
                    f[i] = min(f[i], f[max(0, i - v)] + c)
                j += 1
            else:
                f[i] = f[i - 1]
        return f[m]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
