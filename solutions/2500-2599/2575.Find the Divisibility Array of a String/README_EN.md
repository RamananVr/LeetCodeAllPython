---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2575.Find%20the%20Divisibility%20Array%20of%20a%20String/README_EN.md
rating: 1541
source: Weekly Contest 334 Q2
tags:
    - Array
    - Math
    - String
---

<!-- problem:start -->

# [2575. Find the Divisibility Array of a String](https://leetcode.com/problems/find-the-divisibility-array-of-a-string)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> string <code>word</code> of length <code>n</code>&nbsp;consisting of digits, and a positive integer&nbsp;<code>m</code>.</p>

<p>The <strong>divisibility array</strong> <code>div</code> of <code>word</code> is an integer array of length <code>n</code> such that:</p>

<ul>
	<li><code>div[i] = 1</code> if the&nbsp;<strong>numeric value</strong>&nbsp;of&nbsp;<code>word[0,...,i]</code> is divisible by <code>m</code>, or</li>
	<li><code>div[i] = 0</code> otherwise.</li>
</ul>

<p>Return<em> the divisibility array of</em><em> </em><code>word</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;998244353&quot;, m = 3
<strong>Output:</strong> [1,1,0,0,0,1,1,0,0]
<strong>Explanation:</strong> There are only 4 prefixes that are divisible by 3: &quot;9&quot;, &quot;99&quot;, &quot;998244&quot;, and &quot;9982443&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;1010&quot;, m = 10
<strong>Output:</strong> [0,1,0,1]
<strong>Explanation:</strong> There are only 2 prefixes that are divisible by 10: &quot;10&quot;, and &quot;1010&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code><font face="monospace">word.length == n</font></code></li>
	<li><code><font face="monospace">word</font></code><font face="monospace"> consists of digits from <code>0</code>&nbsp;to <code>9</code></font></li>
	<li><code><font face="monospace">1 &lt;= m &lt;= 10<sup>9</sup></font></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Traversal + Modulo

We iterate over the string `word`, using a variable $x$ to record the modulo result of the current prefix with $m$. If $x$ is $0$, then the divisible array value at the current position is $1$, otherwise it is $0$.

The time complexity is $O(n)$, where $n$ is the length of the string `word`. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        x = 0
        for c in word:
            x = (x * 10 + int(c)) % m
            ans.append(1 if x == 0 else 0)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
