---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1898.Maximum%20Number%20of%20Removable%20Characters/README_EN.md
rating: 1912
source: Weekly Contest 245 Q2
tags:
    - Array
    - Two Pointers
    - String
    - Binary Search
---

<!-- problem:start -->

# [1898. Maximum Number of Removable Characters](https://leetcode.com/problems/maximum-number-of-removable-characters)

## Description

<!-- description:start -->

<p>You are given two strings <code>s</code> and <code>p</code> where <code>p</code> is a <strong>subsequence </strong>of <code>s</code>. You are also given a <strong>distinct 0-indexed </strong>integer array <code>removable</code> containing a subset of indices of <code>s</code> (<code>s</code> is also <strong>0-indexed</strong>).</p>

<p>You want to choose an integer <code>k</code> (<code>0 &lt;= k &lt;= removable.length</code>) such that, after removing <code>k</code> characters from <code>s</code> using the <strong>first</strong> <code>k</code> indices in <code>removable</code>, <code>p</code> is still a <strong>subsequence</strong> of <code>s</code>. More formally, you will mark the character at <code>s[removable[i]]</code> for each <code>0 &lt;= i &lt; k</code>, then remove all marked characters and check if <code>p</code> is still a subsequence.</p>

<p>Return <em>the <strong>maximum</strong> </em><code>k</code><em> you can choose such that </em><code>p</code><em> is still a <strong>subsequence</strong> of </em><code>s</code><em> after the removals</em>.</p>

<p>A <strong>subsequence</strong> of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcacb&quot;, p = &quot;ab&quot;, removable = [3,1,0]
<strong>Output:</strong> 2
<strong>Explanation</strong>: After removing the characters at indices 3 and 1, &quot;a<s><strong>b</strong></s>c<s><strong>a</strong></s>cb&quot; becomes &quot;accb&quot;.
&quot;ab&quot; is a subsequence of &quot;<strong><u>a</u></strong>cc<strong><u>b</u></strong>&quot;.
If we remove the characters at indices 3, 1, and 0, &quot;<s><strong>ab</strong></s>c<s><strong>a</strong></s>cb&quot; becomes &quot;ccb&quot;, and &quot;ab&quot; is no longer a subsequence.
Hence, the maximum k is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcbddddd&quot;, p = &quot;abcd&quot;, removable = [3,2,1,4,5,6]
<strong>Output:</strong> 1
<strong>Explanation</strong>: After removing the character at index 3, &quot;abc<s><strong>b</strong></s>ddddd&quot; becomes &quot;abcddddd&quot;.
&quot;abcd&quot; is a subsequence of &quot;<u><strong>abcd</strong></u>dddd&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcab&quot;, p = &quot;abc&quot;, removable = [0,1,2,3,4]
<strong>Output:</strong> 0
<strong>Explanation</strong>: If you remove the first index in the array removable, &quot;abc&quot; is no longer a subsequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= p.length &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= removable.length &lt; s.length</code></li>
	<li><code>0 &lt;= removable[i] &lt; s.length</code></li>
	<li><code>p</code> is a <strong>subsequence</strong> of <code>s</code>.</li>
	<li><code>s</code> and <code>p</code> both consist of lowercase English letters.</li>
	<li>The elements in <code>removable</code> are <strong>distinct</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search

We notice that if removing the characters at the first $k$ indices in $\textit{removable}$ still makes $p$ a subsequence of $s$, then removing the characters at $k \lt k' \leq \textit{removable.length}$ indices will also satisfy the condition. This monotonicity allows us to use binary search to find the maximum $k$.

We define the left boundary of the binary search as $l = 0$ and the right boundary as $r = \textit{removable.length}$. Then we perform binary search. In each search, we take the middle value $mid = \left\lfloor \frac{l + r + 1}{2} \right\rfloor$ and check if removing the characters at the first $mid$ indices in $\textit{removable}$ still makes $p$ a subsequence of $s$. If it does, we update the left boundary $l = mid$; otherwise, we update the right boundary $r = mid - 1$.

After the binary search ends, we return the left boundary $l$.

The time complexity is $O(k \times \log k)$, and the space complexity is $O(n)$. Here, $n$ is the length of the string $s$, and $k$ is the length of $\textit{removable}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(k: int) -> bool:
            rem = [False] * len(s)
            for i in removable[:k]:
                rem[i] = True
            i = j = 0
            while i < len(s) and j < len(p):
                if not rem[i] and p[j] == s[i]:
                    j += 1
                i += 1
            return j == len(p)

        l, r = 0, len(removable)
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
