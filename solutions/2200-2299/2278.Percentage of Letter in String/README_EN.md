---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2200-2299/2278.Percentage%20of%20Letter%20in%20String/README_EN.md
rating: 1161
source: Weekly Contest 294 Q1
tags:
    - String
---

<!-- problem:start -->

# [2278. Percentage of Letter in String](https://leetcode.com/problems/percentage-of-letter-in-string)

## Description

<!-- description:start -->

<p>Given a string <code>s</code> and a character <code>letter</code>, return<em> the <strong>percentage</strong> of characters in </em><code>s</code><em> that equal </em><code>letter</code><em> <strong>rounded down</strong> to the nearest whole percent.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;foobar&quot;, letter = &quot;o&quot;
<strong>Output:</strong> 33
<strong>Explanation:</strong>
The percentage of characters in s that equal the letter &#39;o&#39; is 2 / 6 * 100% = 33% when rounded down, so we return 33.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;jjjj&quot;, letter = &quot;k&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The percentage of characters in s that equal the letter &#39;k&#39; is 0%, so we return 0.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>letter</code> is a lowercase English letter.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

We can traverse the string $\textit{s}$ and count the number of characters that are equal to $\textit{letter}$. Then, we calculate the percentage using the formula $\textit{count} \times 100 \, / \, \textit{len}(\textit{s})$.

Time complexity is $O(n)$, where $n$ is the length of the string $\textit{s}$. Space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
