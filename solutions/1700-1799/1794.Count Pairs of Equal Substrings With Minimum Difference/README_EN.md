---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1794.Count%20Pairs%20of%20Equal%20Substrings%20With%20Minimum%20Difference/README_EN.md
tags:
    - Greedy
    - Hash Table
    - String
---

<!-- problem:start -->

# [1794. Count Pairs of Equal Substrings With Minimum Difference 🔒](https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference)

## Description

<!-- description:start -->

<p>You are given two strings <code>firstString</code> and <code>secondString</code> that are <strong>0-indexed</strong> and consist only of lowercase English letters. Count the number of index quadruples <code>(i,j,a,b)</code> that satisfy the following conditions:</p>

<ul>
	<li><code>0 &lt;= i &lt;= j &lt; firstString.length</code></li>
	<li><code>0 &lt;= a &lt;= b &lt; secondString.length</code></li>
	<li>The substring of <code>firstString</code> that starts at the <code>i<sup>th</sup></code> character and ends at the <code>j<sup>th</sup></code> character (inclusive) is <strong>equal</strong> to the substring of <code>secondString</code> that starts at the <code>a<sup>th</sup></code> character and ends at the <code>b<sup>th</sup></code> character (inclusive).</li>
	<li><code>j - a</code> is the <strong>minimum</strong> possible value among all quadruples that satisfy the previous conditions.</li>
</ul>

<p>Return <em>the <strong>number</strong> of such quadruples</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> firstString = &quot;abcd&quot;, secondString = &quot;bccda&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The quadruple (0,0,4,4) is the only one that satisfies all the conditions and minimizes j - a.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> firstString = &quot;ab&quot;, secondString = &quot;cd&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no quadruples satisfying all the conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= firstString.length, secondString.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li>Both strings consist only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Hash Table

The problem actually asks us to find a smallest index $i$ and a largest index $j$ such that $firstString[i]$ equals $secondString[j]$, and the value of $i - j$ is the smallest among all index pairs that meet the conditions.

Therefore, we first use a hash table $last$ to record the index of the last occurrence of each character in $secondString$. Then we traverse $firstString$. For each character $c$, if $c$ has appeared in $secondString$, we calculate $i - last[c]$. If the value of $i - last[c]$ is less than the current minimum value, we update the minimum value and set the answer to 1. If the value of $i - last[c]$ equals the current minimum value, we increment the answer by 1.

The time complexity is $O(m + n)$, and the space complexity is $O(C)$. Here, $m$ and $n$ are the lengths of $firstString$ and $secondString$ respectively, and $C$ is the size of the character set. In this problem, $C = 26$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countQuadruples(self, firstString: str, secondString: str) -> int:
        last = {c: i for i, c in enumerate(secondString)}
        ans, mi = 0, inf
        for i, c in enumerate(firstString):
            if c in last:
                t = i - last[c]
                if mi > t:
                    mi = t
                    ans = 1
                elif mi == t:
                    ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
