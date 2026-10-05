---
comments: true
difficulty: Hard
rating: 2105
source: Biweekly Contest 74 Q4
tags:
    - String
    - Dynamic Programming
    - Prefix Sum
---

<!-- problem:start -->

# [2209. Minimum White Tiles After Covering With Carpets](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed binary</strong> string <code>floor</code>, which represents the colors of tiles on a floor:</p>

<ul>
	<li><code>floor[i] = &#39;0&#39;</code> denotes that the <code>i<sup>th</sup></code> tile of the floor is colored <strong>black</strong>.</li>
	<li>On the other hand, <code>floor[i] = &#39;1&#39;</code> denotes that the <code>i<sup>th</sup></code> tile of the floor is colored <strong>white</strong>.</li>
</ul>

<p>You are also given <code>numCarpets</code> and <code>carpetLen</code>. You have <code>numCarpets</code> <strong>black</strong> carpets, each of length <code>carpetLen</code> tiles. Cover the tiles with the given carpets such that the number of <strong>white</strong> tiles still visible is <strong>minimum</strong>. Carpets may overlap one another.</p>

<p>Return <em>the <strong>minimum</strong> number of white tiles still visible.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2200-2299/2209.Minimum%20White%20Tiles%20After%20Covering%20With%20Carpets/images/ex1-1.png" style="width: 400px; height: 73px;" />
<pre>
<strong>Input:</strong> floor = &quot;10110101&quot;, numCarpets = 2, carpetLen = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2200-2299/2209.Minimum%20White%20Tiles%20After%20Covering%20With%20Carpets/images/ex2.png" style="width: 353px; height: 123px;" />
<pre>
<strong>Input:</strong> floor = &quot;11111&quot;, numCarpets = 2, carpetLen = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> 
The figure above shows one way of covering the tiles with the carpets such that no white tiles are visible.
Note that the carpets are able to overlap one another.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= carpetLen &lt;= floor.length &lt;= 1000</code></li>
	<li><code>floor[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>1 &lt;= numCarpets &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

<!-- thinking:start -->

> **Thinking**
>
> We have $m$ carpets of length $L$ and want as few uncovered white tiles as possible. Enumerating placements is exponential; $n, m \le 10^3$ forbids that. Decisions can be made left to right.
>
> Let $\textit{dfs}(i, j)$ be the fewest uncovered white tiles from index $i$ with $j$ carpets left. A black tile is skipped. With no carpet left, the remainder is the prefix-sum difference $s[n]-s[i]$. On a white tile we either leave it ($1 + \textit{dfs}(i+1, j)$) or cover it ($\textit{dfs}(i+L, j-1)$).
>
> There are $O(nm)$ states and constant work each; memoization yields $\textit{dfs}(0, m)$.

<!-- thinking:end -->

We design a function $\textit{dfs}(i, j)$ to represent the minimum number of white tiles that are not covered starting from index $i$ using $j$ carpets. The answer is $\textit{dfs}(0, \textit{numCarpets})$.

For index $i$, we discuss the following cases:

- If $i \ge n$, it means all tiles have been covered, return $0$;
- If $\textit{floor}[i] = 0$, then we do not need to use a carpet, just skip it, i.e., $\textit{dfs}(i, j) = \textit{dfs}(i + 1, j)$;
- If $j = 0$, then we can directly use the prefix sum array $s$ to calculate the number of remaining uncovered white tiles, i.e., $\textit{dfs}(i, j) = s[n] - s[i]$;
- If $\textit{floor}[i] = 1$, then we can choose to use a carpet or not, and take the minimum of the two, i.e., $\textit{dfs}(i, j) = \min(\textit{dfs}(i + 1, j), \textit{dfs}(i + \textit{carpetLen}, j - 1))$.

We use memoization search to solve this problem.

The time complexity is $O(n \times m)$, and the space complexity is $O(n \times m)$. Here, $n$ and $m$ are the length of the string $\textit{floor}$ and the value of $\textit{numCarpets}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= n:
                return 0
            if floor[i] == "0":
                return dfs(i + 1, j)
            if j == 0:
                return s[-1] - s[i]
            return min(1 + dfs(i + 1, j), dfs(i + carpetLen, j - 1))

        n = len(floor)
        s = [0] * (n + 1)
        for i, c in enumerate(floor):
            s[i + 1] = s[i] + int(c == "1")
        ans = dfs(0, numCarpets)
        dfs.cache_clear()
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> We have $m$ carpets of length $L$ and want as few visible white tiles as possible. Enumerating every placement is exponential, and both $n$ and $m$ can be $1000$.
>
> A black tile always jumps to the next index. A floor of black tiles is a chain from $0$ to $n$ of length $n$. Python raises RecursionError when $n=1000$.
>
> Skipping a black tile, leaving a white tile, or laying a carpet all read a later index. Laying a carpet also spends one carpet.
>
> Fill from the right. $f[i][j]$ is the fewest visible white tiles from index $i$ with $j$ carpets left, and $f[n][\cdot]=0$. A black tile copies $f[i+1][j]$. With no carpet left the answer is the remaining white count $s[n]-s[i]$. A white tile takes the minimum of leaving it, $1+f[i+1][j]$, and covering it, $f[i+L][j-1]$.

<!-- thinking:end -->

Let $s[i]$ be the number of white tiles in the first $i$ positions of $\textit{floor}$. Let $f[i][j]$ be the fewest white tiles left visible from index $i$ with $j$ carpets remaining. The answer is $f[0][\textit{numCarpets}]$. Set $f[n][j] = 0$, which means every tile has already been passed.

Fill $i$ from $n - 1$ down to $0$ and $j$ from $0$ through $m$:

- If $\textit{floor}[i] = 0$, the tile is black and costs no carpet, so $f[i][j] = f[i + 1][j]$.
- If $j = 0$, no carpet remains, so $f[i][j] = s[n] - s[i]$.
- Otherwise the tile is white. Leaving it visible costs $1 + f[i + 1][j]$. Laying a carpet of length $L$ jumps to index $i + L$ and leaves $j - 1$ carpets. That branch is $f[i + L][j - 1]$ when $i + L \le n$, and $0$ when the jump passes the end of the floor. $f[i][j]$ is the smaller of the two.

The time complexity is $O(n \times m)$, and the space complexity is $O(n \times m)$. Here $n$ and $m$ are the length of $\textit{floor}$ and the value of $\textit{numCarpets}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        s = [0] * (n + 1)
        for i, c in enumerate(floor):
            s[i + 1] = s[i] + int(c == "1")
        f = [[0] * (numCarpets + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(numCarpets + 1):
                if floor[i] == "0":
                    f[i][j] = f[i + 1][j]
                elif j == 0:
                    f[i][j] = s[n] - s[i]
                else:
                    cover = f[i + carpetLen][j - 1] if i + carpetLen <= n else 0
                    f[i][j] = min(1 + f[i + 1][j], cover)
        return f[0][numCarpets]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
