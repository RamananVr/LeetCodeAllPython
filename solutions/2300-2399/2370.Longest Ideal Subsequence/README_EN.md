---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2300-2399/2370.Longest%20Ideal%20Subsequence/README_EN.md
rating: 1834
source: Weekly Contest 305 Q4
tags:
    - Hash Table
    - String
    - Dynamic Programming
---

<!-- problem:start -->

# [2370. Longest Ideal Subsequence](https://leetcode.com/problems/longest-ideal-subsequence)

## Description

<!-- description:start -->

<p>You are given a string <code>s</code> consisting of lowercase letters and an integer <code>k</code>. We call a string <code>t</code> <strong>ideal</strong> if the following conditions are satisfied:</p>

<ul>
	<li><code>t</code> is a <strong>subsequence</strong> of the string <code>s</code>.</li>
	<li>The absolute difference in the alphabet order of every two <strong>adjacent</strong> letters in <code>t</code> is less than or equal to <code>k</code>.</li>
</ul>

<p>Return <em>the length of the <strong>longest</strong> ideal string</em>.</p>

<p>A <strong>subsequence</strong> is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.</p>

<p><strong>Note</strong> that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of <code>&#39;a&#39;</code> and <code>&#39;z&#39;</code> is <code>25</code>, not <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;acfgbd&quot;, k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest ideal string is &quot;acbd&quot;. The length of this string is 4, so 4 is returned.
Note that &quot;acfgbd&quot; is not ideal because &#39;c&#39; and &#39;f&#39; have a difference of 3 in alphabet order.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcd&quot;, k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest ideal string is &quot;abcd&quot;. The length of this string is 4, so 4 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= 25</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        ans = 1
        dp = [1] * n
        d = {s[0]: 0}
        for i in range(1, n):
            a = ord(s[i])
            for b in ascii_lowercase:
                if abs(a - ord(b)) > k:
                    continue
                if b in d:
                    dp[i] = max(dp[i], dp[d[b]] + 1)
            d[s[i]] = i
        return max(dp)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
