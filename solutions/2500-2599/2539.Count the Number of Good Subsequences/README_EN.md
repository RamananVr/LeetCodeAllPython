---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2539.Count%20the%20Number%20of%20Good%20Subsequences/README_EN.md
tags:
    - Hash Table
    - Math
    - String
    - Combinatorics
    - Counting
---

<!-- problem:start -->

# [2539. Count the Number of Good Subsequences 🔒](https://leetcode.com/problems/count-the-number-of-good-subsequences)

## Description

<!-- description:start -->

<p>A <strong>subsequence</strong> of a string is&nbsp;good if it is not empty and the frequency of each one of its characters is the same.</p>

<p>Given a string <code>s</code>, return <em>the number of good subsequences of</em> <code>s</code>. Since the answer may be too large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>A <strong>subsequence</strong> is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabb&quot;
<strong>Output:</strong> 11
<strong>Explanation:</strong> The total number of subsequences is <code>2<sup>4</sup>. </code>There are five subsequences which are not good: &quot;<strong><u>aab</u></strong>b&quot;, &quot;a<u><strong>abb</strong></u>&quot;, &quot;<strong><u>a</u></strong>a<u><strong>bb</strong></u>&quot;, &quot;<u><strong>aa</strong></u>b<strong><u>b</u></strong>&quot;, and the empty subsequence. Hence, the number of good subsequences is <code>2<sup>4</sup>-5 = 11</code>.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leet&quot;
<strong>Output:</strong> 12
<strong>Explanation:</strong> There are four subsequences which are not good: &quot;<strong><u>l</u><em>ee</em></strong>t&quot;, &quot;l<u><strong>eet</strong></u>&quot;, &quot;<strong><u>leet</u></strong>&quot;, and the empty subsequence. Hence, the number of good subsequences is <code>2<sup>4</sup>-4 = 12</code>.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;
<strong>Output:</strong> 15
<strong>Explanation:</strong> All of the non-empty subsequences are good subsequences. Hence, the number of good subsequences is <code>2<sup>4</sup>-1 = 15</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
N = 10001
MOD = 10**9 + 7
f = [1] * N
g = [1] * N
for i in range(1, N):
    f[i] = f[i - 1] * i % MOD
    g[i] = pow(f[i], MOD - 2, MOD)

def comb(n, k):
    return f[n] * g[k] * g[n - k] % MOD

class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        for i in range(1, max(cnt.values()) + 1):
            x = 1
            for v in cnt.values():
                if v >= i:
                    x = x * (comb(v, i) + 1) % MOD
            ans = (ans + x - 1) % MOD
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
