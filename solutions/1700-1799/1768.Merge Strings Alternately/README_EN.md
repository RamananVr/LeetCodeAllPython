---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1700-1799/1768.Merge%20Strings%20Alternately/README_EN.md
rating: 1166
source: Weekly Contest 229 Q1
tags:
    - Two Pointers
    - String
---

<!-- problem:start -->

# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately)

## Description

<!-- description:start -->

<p>You are given two strings <code>word1</code> and <code>word2</code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>

<p>Return <em>the merged string.</em></p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>

<strong>Input:</strong> word1 = &quot;abc&quot;, word2 = &quot;pqr&quot;

<strong>Output:</strong> &quot;apbqcr&quot;

<strong>Explanation:</strong>&nbsp;The merged string will be merged as so:

word1:  a   b   c

word2:    p   q   r

merged: a p b q c r

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>

<strong>Input:</strong> word1 = &quot;ab&quot;, word2 = &quot;pqrs&quot;

<strong>Output:</strong> &quot;apbqrs&quot;

<strong>Explanation:</strong>&nbsp;Notice that as word2 is longer, &quot;rs&quot; is appended to the end.

word1:  a   b 

word2:    p   q   r   s

merged: a p b q   r   s

</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>

<strong>Input:</strong> word1 = &quot;abcd&quot;, word2 = &quot;pq&quot;

<strong>Output:</strong> &quot;apbqcd&quot;

<strong>Explanation:</strong>&nbsp;Notice that as word1 is longer, &quot;cd&quot; is appended to the end.

word1:  a   b   c   d

word2:    p   q 

merged: a p b q c   d

</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>1 &lt;= word1.length, word2.length &lt;= 100</code></li>

    <li><code>word1</code> and <code>word2</code> consist of lowercase English letters.</li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Direct Simulation

We traverse the two strings `word1` and `word2`, take out the characters one by one, and append them to the result string. The Python code can be simplified into one line.

The time complexity is $O(m + n)$, where $m$ and $n$ are the lengths of the two strings respectively. Ignoring the space consumption of the answer, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
