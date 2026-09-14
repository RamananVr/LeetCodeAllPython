---
comments: true
difficulty: Medium
tags:
    - Math
    - Dynamic Programming
---

<!-- problem:start -->

# [650. 2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard)

## Description

<!-- description:start -->

<p>There is only one character <code>&#39;A&#39;</code> on the screen of a notepad. You can perform one of two operations on this notepad for each step:</p>

<ul>
	<li>Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).</li>
	<li>Paste: You can paste the characters which are copied last time.</li>
</ul>

<p>Given an integer <code>n</code>, return <em>the minimum number of operations to get the character</em> <code>&#39;A&#39;</code> <em>exactly</em> <code>n</code> <em>times on the screen</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> Initially, we have one character &#39;A&#39;.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get &#39;AA&#39;.
In step 3, we use Paste operation to get &#39;AAA&#39;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

<!-- thinking:start -->

> **Thinking**
>
> Start from one `A` and reach $n$ by copy and paste. The search tree of sequences is wide.
>
> If the last step pastes a block of length $n/j$ into $j$ copies, $dfs(n)=\min(dfs(n/j)+j)$. Memoize over factors; $n=1$ costs $0$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 1:
                return 0
            i, ans = 2, n
            while i * i <= n:
                if n % i == 0:
                    ans = min(ans, dfs(n // i) + i)
                i += 1
            return ans

        return dfs(n)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Memoization is top-down. The same recurrences fill $dp[i]$ bottom-up over factors, without recursion.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minSteps(self, n: int) -> int:
        dp = list(range(n + 1))
        dp[1] = 0
        for i in range(2, n + 1):
            j = 2
            while j * j <= i:
                if i % j == 0:
                    dp[i] = min(dp[i], dp[i // j] + j)
                j += 1
        return dp[-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Math

<!-- thinking:start -->

> **Thinking**
>
> The optimum equals the sum of prime factors of $n$: factor $i$ is one copy plus $i-1$ pastes. Factorize $n$ and skip the DP table.

<!-- thinking:end -->

Factorize $n$; each prime factor $i$ costs $i$ operations.

<!-- solution:end -->

<!-- problem:end -->
