---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2700-2799/2781.Length%20of%20the%20Longest%20Valid%20Substring/README_EN.md
rating: 2203
source: Weekly Contest 354 Q4
tags:
    - Array
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [2781. Length of the Longest Valid Substring](https://leetcode.com/problems/length-of-the-longest-valid-substring)

## Description

<!-- description:start -->

<p>You are given a string <code>word</code> and an array of strings <code>forbidden</code>.</p>

<p>A string is called <strong>valid</strong> if none of its substrings are present in <code>forbidden</code>.</p>

<p>Return <em>the length of the <strong>longest valid substring</strong> of the string </em><code>word</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string, possibly empty.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;cbaaaabc&quot;, forbidden = [&quot;aaa&quot;,&quot;cb&quot;]
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 11 valid substrings in word: &quot;c&quot;, &quot;b&quot;, &quot;a&quot;, &quot;ba&quot;, &quot;aa&quot;, &quot;bc&quot;, &quot;baa&quot;, &quot;aab&quot;, &quot;ab&quot;, &quot;abc&quot; and &quot;aabc&quot;. The length of the longest valid substring is 4. 
It can be shown that all other substrings contain either &quot;aaa&quot; or &quot;cb&quot; as a substring. </pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;leetcode&quot;, forbidden = [&quot;de&quot;,&quot;le&quot;,&quot;e&quot;]
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 11 valid substrings in word: &quot;l&quot;, &quot;t&quot;, &quot;c&quot;, &quot;o&quot;, &quot;d&quot;, &quot;tc&quot;, &quot;co&quot;, &quot;od&quot;, &quot;tco&quot;, &quot;cod&quot;, and &quot;tcod&quot;. The length of the longest valid substring is 4.
It can be shown that all other substrings contain either &quot;de&quot;, &quot;le&quot;, or &quot;e&quot; as a substring. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= forbidden.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= forbidden[i].length &lt;= 10</code></li>
	<li><code>forbidden[i]</code> consists only of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        s = set(forbidden)
        ans = i = 0
        for j in range(len(word)):
            for k in range(j, max(j - 10, i - 1), -1):
                if word[k : j + 1] in s:
                    i = k + 1
                    break
            ans = max(ans, j - i + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
