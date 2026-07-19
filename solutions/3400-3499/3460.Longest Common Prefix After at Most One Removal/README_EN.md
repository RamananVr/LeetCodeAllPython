---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3460.Longest%20Common%20Prefix%20After%20at%20Most%20One%20Removal/README_EN.md
tags:
    - Two Pointers
    - String
---

<!-- problem:start -->

# [3460. Longest Common Prefix After at Most One Removal 🔒](https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal)

## Description

<!-- description:start -->

<p>You are given two strings <code>s</code> and <code>t</code>.</p>

<p>Return the <strong>length</strong> of the <strong>longest common <span data-keyword="string-prefix">prefix</span></strong> between <code>s</code> and <code>t</code> after removing <strong>at most</strong> one character from <code>s</code>.</p>

<p><strong>Note:</strong> <code>s</code> can be left without any removal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;madxa&quot;, t = &quot;madam&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Removing <code>s[3]</code> from <code>s</code> results in <code>&quot;mada&quot;</code>, which has a longest common prefix of length 4 with <code>t</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leetcode&quot;, t = &quot;eetcode&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>Removing <code>s[0]</code> from <code>s</code> results in <code>&quot;eetcode&quot;</code>, which matches <code>t</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;one&quot;, t = &quot;one&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>No removal is needed.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;a&quot;, t = &quot;b&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><code>s</code> and <code>t</code> cannot have a common prefix.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= t.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> contain only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

We record the lengths of the strings $s$ and $t$ as $n$ and $m$, respectively. Then, we use two pointers $i$ and $j$ to point to the beginning of the strings $s$ and $t$, and use a boolean variable $\textit{rem}$ to record whether a character has been removed.

Next, we start traversing the strings $s$ and $t$. If $s[i]$ is not equal to $t[j]$, we check if a character has already been removed. If a character has been removed, we exit the loop; otherwise, we mark that a character has been removed and skip $s[i]$. Otherwise, we skip both $s[i]$ and $t[j]$. Continue traversing until $i \geq n$ or $j \geq m$.

Finally, return $j$.

The time complexity is $O(n+m)$, where $n$ and $m$ are the lengths of the strings $s$ and $t$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        i = j = 0
        rem = False
        while i < n and j < m:
            if s[i] != t[j]:
                if rem:
                    break
                rem = True
            else:
                j += 1
            i += 1
        return j
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
