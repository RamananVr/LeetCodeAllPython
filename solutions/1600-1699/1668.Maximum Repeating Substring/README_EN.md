---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1600-1699/1668.Maximum%20Repeating%20Substring/README_EN.md
rating: 1395
source: Biweekly Contest 40 Q1
tags:
    - String
    - Dynamic Programming
    - String Matching
---

<!-- problem:start -->

# [1668. Maximum Repeating Substring](https://leetcode.com/problems/maximum-repeating-substring)

## Description

<!-- description:start -->

<p>For a string <code>sequence</code>, a string <code>word</code> is <strong><code>k</code>-repeating</strong> if <code>word</code> concatenated <code>k</code> times is a substring of <code>sequence</code>. The <code>word</code>&#39;s <strong>maximum <code>k</code>-repeating value</strong> is the highest value <code>k</code> where <code>word</code> is <code>k</code>-repeating in <code>sequence</code>. If <code>word</code> is not a substring of <code>sequence</code>, <code>word</code>&#39;s maximum <code>k</code>-repeating value is <code>0</code>.</p>

<p>Given strings <code>sequence</code> and <code>word</code>, return <em>the <strong>maximum <code>k</code>-repeating value</strong> of <code>word</code> in <code>sequence</code></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> sequence = &quot;ababc&quot;, word = &quot;ab&quot;
<strong>Output:</strong> 2
<strong>Explanation: </strong>&quot;abab&quot; is a substring in &quot;<u>abab</u>c&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> sequence = &quot;ababc&quot;, word = &quot;ba&quot;
<strong>Output:</strong> 1
<strong>Explanation: </strong>&quot;ba&quot; is a substring in &quot;a<u>ba</u>bc&quot;. &quot;baba&quot; is not a substring in &quot;ababc&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> sequence = &quot;ababc&quot;, word = &quot;ac&quot;
<strong>Output:</strong> 0
<strong>Explanation: </strong>&quot;ac&quot; is not a substring in &quot;ababc&quot;. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sequence.length &lt;= 100</code></li>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>sequence</code> and <code>word</code>&nbsp;contains only lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for k in range(len(sequence) // len(word), -1, -1):
            if word * k in sequence:
                return k
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
