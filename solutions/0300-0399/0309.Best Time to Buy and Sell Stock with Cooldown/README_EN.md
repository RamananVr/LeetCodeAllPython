---
comments: true
difficulty: Medium
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown)

## Description

<!-- description:start -->

<p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:</p>

<ul>
	<li>After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).</li>
</ul>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,0,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> transactions = [buy, sell, cooldown, buy, sell]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 5000</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

<!-- thinking:start -->

> **Thinking**
>
> We may trade many times, but a sell forces a one-day cooldown. A raw decision tree over day, holding, and cooldown revisits the same states.
>
> Compress to $(i,j)$: starting at day $i$, whether we hold. Skip the day; if holding, sell and jump to $i+2$; if free, buy and start holding. Memoization evaluates each state once; the extra day after a sell is the cooldown.

<!-- thinking:end -->

We design a function $dfs(i, j)$, which represents the maximum profit that can be obtained starting from the $i$th day with state $j$. The values of $j$ are $0$ and $1$, respectively representing currently not holding a stock and holding a stock. The answer is $dfs(0, 0)$.

The execution logic of the function $dfs(i, j)$ is as follows:

If $i \geq n$, it means that there are no more stocks to trade, so return $0$;

Otherwise, we can choose not to trade, then $dfs(i, j) = dfs(i + 1, j)$. We can also trade stocks. If $j > 0$, it means that we currently hold a stock and can sell it, then $dfs(i, j) = prices[i] + dfs(i + 2, 0)$. If $j = 0$, it means that we currently do not hold a stock and can buy, then $dfs(i, j) = -prices[i] + dfs(i + 1, 1)$. Take the maximum value as the return value of the function $dfs(i, j)$.

The answer is $dfs(0, 0)$.

To avoid repeated calculations, we use the method of memoization search, and use an array $f$ to record the return value of $dfs(i, j)$. If $f[i][j]$ is not $-1$, it means that it has been calculated, and we can directly return $f[i][j]$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $prices$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= len(prices):
                return 0
            ans = dfs(i + 1, j)
            if j:
                ans = max(ans, prices[i] + dfs(i + 2, 0))
            else:
                ans = max(ans, -prices[i] + dfs(i + 1, 1))
            return ans

        return dfs(0, 0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 fills a suffix table from the end. The same choices can be written forward: $f[i][0/1]$ is the best profit after day $i$, free or holding. Free comes from staying free or selling today; holding comes from staying put or buying after cooldown, i.e. from $f[i-2][0]$.
>
> Fill left to right; the answer is free on the last day. Time stays $O(n)$.

<!-- thinking:end -->

We can also use dynamic programming to solve this problem.

We define $f[i][j]$ to represent the maximum profit that can be obtained on the $i$th day with state $j$. The values of $j$ are $0$ and $1$, respectively representing currently not holding a stock and holding a stock. Initially, $f[0][0] = 0$, $f[0][1] = -prices[0]$.

When $i \geq 1$, if we currently do not hold a stock, then $f[i][0]$ can be obtained by transitioning from $f[i - 1][0]$ and $f[i - 1][1] + prices[i]$, i.e., $f[i][0] = \max(f[i - 1][0], f[i - 1][1] + prices[i])$. If we currently hold a stock, then $f[i][1]$ can be obtained by transitioning from $f[i - 1][1]$ and $f[i - 2][0] - prices[i]$, i.e., $f[i][1] = \max(f[i - 1][1], f[i - 2][0] - prices[i])$. The final answer is $f[n - 1][0]$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $prices$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n)]
        f[0][1] = -prices[0]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][1] + prices[i])
            f[i][1] = max(f[i - 1][1], f[i - 2][0] - prices[i])
        return f[n - 1][0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Dynamic Programming (Space Optimization)

<!-- thinking:start -->

> **Thinking**
>
> Method 2 only reads $i-1$ and $i-2$, so the full table is unnecessary. Three rolling variables (free two days ago, free yesterday, holding yesterday) implement the same transfers in $O(1)$ space.

<!-- thinking:end -->

The transition only needs the previous two days, so three variables are enough and the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f, f0, f1 = 0, 0, -prices[0]
        for x in prices[1:]:
            f, f0, f1 = f0, max(f0, f1 + x), max(f1, f - x)
        return f0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 4: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> We may trade many times, but a sell forces a one-day cooldown. $n \le 5000$, so a raw decision tree is far too large.
>
> The state is the day and whether we hold. Skipping always calls the next day before it returns, so the chain has length $n$ and overflows the stack.
>
> Later days are known if we walk backward. Let $f[i][j]$ be the best profit from day $i$ with holding flag $j$, and fill $i$ from $n-1$ down to $0$. Selling lands on $i+2$, which is the cooldown.

<!-- thinking:end -->

Let $f[i][j]$ be the maximum profit starting from day $i$ in state $j$. The values of $j$ are $0$ and $1$, meaning we do not hold a stock and we hold a stock. The answer is $f[0][0]$. Days past the end contribute $0$, so $f[n][j] = f[n + 1][j] = 0$.

Fill $i$ from $n - 1$ down to $0$. Doing nothing keeps $f[i + 1][j]$. If $j > 0$, we hold a stock and may sell it, earning $prices[i] + f[i + 2][0]$. The extra day is the cooldown. If $j = 0$, we may buy, earning $-prices[i] + f[i + 1][1]$. Take the larger value:

$$
f[i][j] = \max(f[i + 1][j],\ prices[i] + f[i + 2][0])
$$

when $j > 0$, and

$$
f[i][j] = \max(f[i + 1][j],\ -prices[i] + f[i + 1][1])
$$

when $j = 0$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $prices$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for j in range(2):
                ans = f[i + 1][j]
                if j:
                    ans = max(ans, prices[i] + f[i + 2][0])
                else:
                    ans = max(ans, -prices[i] + f[i + 1][1])
                f[i][j] = ans
        return f[0][0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
