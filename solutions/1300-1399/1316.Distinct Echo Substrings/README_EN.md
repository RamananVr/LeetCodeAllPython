---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1316.Distinct%20Echo%20Substrings/README_EN.md
rating: 1836
source: Biweekly Contest 17 Q4
tags:
    - Trie
    - String
    - Hash Function
    - Rolling Hash
---

<!-- problem:start -->

# [1316. Distinct Echo Substrings](https://leetcode.com/problems/distinct-echo-substrings)

## Description

<!-- description:start -->

<p>Return the number of <strong>distinct</strong> non-empty substrings of <code>text</code>&nbsp;that can be written as the concatenation of some string with itself (i.e. it can be written as <code>a + a</code>&nbsp;where <code>a</code> is some string).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;abcabcabc&quot;
<strong>Output:</strong> 3
<b>Explanation: </b>The 3 substrings are &quot;abcabc&quot;, &quot;bcabca&quot; and &quot;cabcab&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;leetcodeleetcode&quot;
<strong>Output:</strong> 2
<b>Explanation: </b>The 2 substrings are &quot;ee&quot; and &quot;leetcodeleetcode&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 2000</code></li>
	<li><code>text</code>&nbsp;has only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        def get(l, r):
            return (h[r] - h[l - 1] * p[r - l + 1]) % mod

        n = len(text)
        base = 131
        mod = int(1e9) + 7
        h = [0] * (n + 10)
        p = [1] * (n + 10)
        for i, c in enumerate(text):
            t = ord(c) - ord('a') + 1
            h[i + 1] = (h[i] * base) % mod + t
            p[i + 1] = (p[i] * base) % mod
        vis = set()
        for i in range(n - 1):
            for j in range(i + 1, n, 2):
                k = (i + j) >> 1
                a = get(i + 1, k + 1)
                b = get(k + 2, j + 1)
                if a == b:
                    vis.add(a)
        return len(vis)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
