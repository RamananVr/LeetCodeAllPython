---
comments: true
difficulty: Medium
rating: 1694
source: Biweekly Contest 91 Q2
tags:
    - Dynamic Programming
---

<!-- problem:start -->

# [2466. Count Ways To Build Good Strings](https://leetcode.com/problems/count-ways-to-build-good-strings)

## Description

<!-- description:start -->

<p>Given the integers <code>zero</code>, <code>one</code>, <code>low</code>, and <code>high</code>, we can construct a string by starting with an empty string, and then at each step perform either of the following:</p>

<ul>
	<li>Append the character <code>&#39;0&#39;</code> <code>zero</code> times.</li>
	<li>Append the character <code>&#39;1&#39;</code> <code>one</code> times.</li>
</ul>

<p>This can be performed any number of times.</p>

<p>A <strong>good</strong> string is a string constructed by the above process having a <strong>length</strong> between <code>low</code> and <code>high</code> (<strong>inclusive</strong>).</p>

<p>Return <em>the number of <strong>different</strong> good strings that can be constructed satisfying these properties.</em> Since the answer can be large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> low = 3, high = 3, zero = 1, one = 1
<strong>Output:</strong> 8
<strong>Explanation:</strong> 
One possible valid good string is &quot;011&quot;. 
It can be constructed as follows: &quot;&quot; -&gt; &quot;0&quot; -&gt; &quot;01&quot; -&gt; &quot;011&quot;. 
All binary strings from &quot;000&quot; to &quot;111&quot; are good strings in this example.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> low = 2, high = 3, zero = 1, one = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> The good strings are &quot;00&quot;, &quot;11&quot;, &quot;000&quot;, &quot;110&quot;, and &quot;011&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= low&nbsp;&lt;= high&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= zero, one &lt;= low</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization Search

<!-- thinking:start -->

> **Thinking**
>
> Each step appends $zero$ zeros or $one$ ones; a string is good if its length lies in $[low,high]$. With $high\le 10^5$, $dfs(i)$ is the number of ways after length $i$: count $1$ if $i$ is already in range, then add $dfs(i+zero)$ and $dfs(i+one)$.

<!-- thinking:end -->

We design a function $dfs(i)$ to represent the number of good strings constructed starting from the $i$-th position. The answer is $dfs(0)$.

The computation process of the function $dfs(i)$ is as follows:

- If $i > high$, return $0$;
- If $low \leq i \leq high$, increment the answer by $1$, then after $i$, we can add either `zero` number of $0$s or `one` number of $1$s. Therefore, the answer is incremented by $dfs(i + zero) + dfs(i + one)$.

During the process, we need to take the modulus of the answer, and we can use memoization search to reduce redundant computations.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n = high$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dfs(i):
            if i > high:
                return 0
            ans = 0
            if low <= i <= high:
                ans += 1
            ans += dfs(i + zero) + dfs(i + one)
            return ans % mod

        mod = 10**9 + 7
        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic programming

<!-- thinking:start -->

> **Thinking**
>
> Method 1 fills a suffix table from length $high$. The same strings can be counted by the ways to reach each length: $f[0]=1$, add $f[i-zero]$ and $f[i-one]$, then sum $f$ on $[low,high]$.
>
> Fill left to right. Time stays $O(n)$.

<!-- thinking:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Each step appends $zero$ zeros or $one$ ones, and a string is good when its length lies in $[low,high]$. $high \le 10^5$, so a decision tree over appends repeats many lengths.
>
> The shorter step is taken first. Both steps are at least $1$, so that call always moves to a larger length, and the chain can have length $high$ and overflow the stack.
>
> Longer lengths are known if we walk downward. Let $f[i]$ be the number of good strings when the length is already $i$: count $1$ inside the range, then add $f[i+zero]$ and $f[i+one]$, treating anything past $high$ as $0$.

<!-- thinking:end -->

Let $f[i]$ be the number of good strings that can be built when the current length is already $i$. The answer is $f[0]$. Lengths past $high$ contribute $0$.

Fill $i$ from $high$ down to $0$. If $low \le i \le high$, the current string is already good, so start from $1$. Then add $f[i + zero]$ and $f[i + one]$; an index past $high$ contributes $0$. Reduce each value modulo $10^9 + 7$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n = high$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        f = [0] * (high + 1)
        for i in range(high, -1, -1):
            ans = int(low <= i <= high)
            if i + zero <= high:
                ans += f[i + zero]
            if i + one <= high:
                ans += f[i + one]
            f[i] = ans % mod
        return f[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
