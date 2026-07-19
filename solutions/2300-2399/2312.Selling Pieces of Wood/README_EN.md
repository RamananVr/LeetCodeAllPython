---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2300-2399/2312.Selling%20Pieces%20of%20Wood/README_EN.md
rating: 2363
source: Weekly Contest 298 Q4
tags:
    - Memoization
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [2312. Selling Pieces of Wood](https://leetcode.com/problems/selling-pieces-of-wood)

## Description

<!-- description:start -->

<p>You are given two integers <code>m</code> and <code>n</code> that represent the height and width of a rectangular piece of wood. You are also given a 2D integer array <code>prices</code>, where <code>prices[i] = [h<sub>i</sub>, w<sub>i</sub>, price<sub>i</sub>]</code> indicates you can sell a rectangular piece of wood of height <code>h<sub>i</sub></code> and width <code>w<sub>i</sub></code> for <code>price<sub>i</sub></code> dollars.</p>

<p>To cut a piece of wood, you must make a vertical or horizontal cut across the <strong>entire</strong> height or width of the piece to split it into two smaller pieces. After cutting a piece of wood into some number of smaller pieces, you can sell pieces according to <code>prices</code>. You may sell multiple pieces of the same shape, and you do not have to sell all the shapes. The grain of the wood makes a difference, so you <strong>cannot</strong> rotate a piece to swap its height and width.</p>

<p>Return <em>the <strong>maximum</strong> money you can earn after cutting an </em><code>m x n</code><em> piece of wood</em>.</p>

<p>Note that you can cut the piece of wood as many times as you want.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2300-2399/2312.Selling%20Pieces%20of%20Wood/images/ex1.png" style="width: 239px; height: 150px;" />
<pre>
<strong>Input:</strong> m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]
<strong>Output:</strong> 19
<strong>Explanation:</strong> The diagram above shows a possible scenario. It consists of:
- 2 pieces of wood shaped 2 x 2, selling for a price of 2 * 7 = 14.
- 1 piece of wood shaped 2 x 1, selling for a price of 1 * 3 = 3.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 14 + 3 + 2 = 19 money earned.
It can be shown that 19 is the maximum amount of money that can be earned.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2300-2399/2312.Selling%20Pieces%20of%20Wood/images/ex2new.png" style="width: 250px; height: 175px;" />
<pre>
<strong>Input:</strong> m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]
<strong>Output:</strong> 32
<strong>Explanation:</strong> The diagram above shows a possible scenario. It consists of:
- 3 pieces of wood shaped 3 x 2, selling for a price of 3 * 10 = 30.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 30 + 2 = 32 money earned.
It can be shown that 32 is the maximum amount of money that can be earned.
Notice that we cannot rotate the 1 x 4 piece of wood to obtain a 4 x 1 piece of wood.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>1 &lt;= prices.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>prices[i].length == 3</code></li>
	<li><code>1 &lt;= h<sub>i</sub> &lt;= m</code></li>
	<li><code>1 &lt;= w<sub>i</sub> &lt;= n</code></li>
	<li><code>1 &lt;= price<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>All the shapes of wood <code>(h<sub>i</sub>, w<sub>i</sub>)</code> are pairwise <strong>distinct</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

First, we define a 2D array $d$, where $d[i][j]$ represents the price of a wood block with height $i$ and width $j$.

Then, we design a function $dfs(h, w)$ to denote the maximum amount of money obtained by cutting a wood block with height $h$ and width $w$. The answer will be $dfs(m, n)$.

The process of function $dfs(h, w)$ is as follows:

- If $(h, w)$ has been calculated before, return the answer directly.
- Otherwise, initialize the answer as $d[h][w]$, then enumerate the cutting positions, calculate the maximum amount of money obtained by cutting the wood block into two pieces, and take the maximum value.

The time complexity is $O(m \times n \times (m + n) + p)$, and the space complexity is $O(m \times n)$. Here, $p$ represents the length of the price array, while $m$ and $n$ represent the height and width of the wood blocks, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        @cache
        def dfs(h: int, w: int) -> int:
            ans = d[h].get(w, 0)
            for i in range(1, h // 2 + 1):
                ans = max(ans, dfs(i, w) + dfs(h - i, w))
            for i in range(1, w // 2 + 1):
                ans = max(ans, dfs(h, i) + dfs(h, w - i))
            return ans

        d = defaultdict(dict)
        for h, w, p in prices:
            d[h][w] = p
        return dfs(m, n)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We can transform the memoization search in Solution 1 into dynamic programming.

Similar to Solution 1, we define a 2D array $d$, where $d[i][j]$ represents the price of a wood block with height $i$ and width $j$. Initially, we iterate through the price array $prices$ and store the price $p$ of each wood block $(h, w, p)$ in $d[h][w]$, while the rest of the prices are set to $0$.

Then, we define another 2D array $f$, where $f[i][j]$ represents the maximum amount of money obtained by cutting a wood block with height $i$ and width $j$. The answer will be $f[m][n]$.

Considering how $f[i][j]$ transitions, initially $f[i][j] = d[i][j]$. We enumerate the cutting positions, calculate the maximum amount of money obtained by cutting the wood block into two pieces, and take the maximum value.

The time complexity is $O(m \times n \times (m + n) + p)$, and the space complexity is $O(m \times n)$. Here, $p$ represents the length of the price array, while $m$ and $n$ represent the height and width of the wood blocks, respectively.

Similar problems:

- [1444. Number of Ways of Cutting a Pizza](https://github.com/doocs/leetcode/blob/main/solution/1400-1499/1444.Number%20of%20Ways%20of%20Cutting%20a%20Pizza/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        d = defaultdict(dict)
        for h, w, p in prices:
            d[h][w] = p
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = d[i].get(j, 0)
                for k in range(1, i):
                    f[i][j] = max(f[i][j], f[k][j] + f[i - k][j])
                for k in range(1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[i][j - k])
        return f[m][n]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
