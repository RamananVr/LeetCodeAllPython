---
comments: true
difficulty: Medium
tags:
    - String
---

<!-- problem:start -->

# [6. Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion)

## Description

<!-- description:start -->

<p>The string <code>&quot;PAYPALISHIRING&quot;</code> is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)</p>

<pre>
P   A   H   N
A P L S I I G
Y   I   R
</pre>

<p>And then read line by line: <code>&quot;PAHNAPLSIIGYIR&quot;</code></p>

<p>Write the code that will take a string and make this conversion given a number of rows:</p>

<pre>
string convert(string s, int numRows);
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 3
<strong>Output:</strong> &quot;PAHNAPLSIIGYIR&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;PAYPALISHIRING&quot;, numRows = 4
<strong>Output:</strong> &quot;PINALSIGYAHRPI&quot;
<strong>Explanation:</strong>
P     I    N
A   L S  I G
Y A   H R
P     I
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A&quot;, numRows = 1
<strong>Output:</strong> &quot;A&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), <code>&#39;,&#39;</code> and <code>&#39;.&#39;</code>.</li>
	<li><code>1 &lt;= numRows &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

<!-- thinking:start -->

> **Thinking**
>
> Drawing the 2D grid and reading by row is correct, but most cells are empty. $n \le 10^3$ would pass, yet the unused “column” dimension is wasted.
>
> Only the row of each character, and order within a row, affect the answer. The row index goes $0,1,\ldots,\textit{numRows}-1$ and then back, reversing at the top or bottom.
>
> So we keep $\textit{numRows}$ lists and flip a direction $k$ at the boundaries. $k$ starts at $-1$, so the first row immediately turns it downward. When $\textit{numRows}=1$, top and bottom are the same row; we must return $s$ as is, or the direction would bounce in place.

<!-- thinking:end -->

We use a 2D array $g$ to simulate the process of arranging the string in a zigzag pattern, where $g[i][j]$ represents the character at row $i$ and column $j$. Initially, $i = 0$. We also define a direction variable $k$, initially $k = -1$, which means moving upwards.

We traverse the string $s$ from left to right. For each character $c$, we append it to $g[i]$. If $i = 0$ or $i = \textit{numRows} - 1$, it means the current character is at a turning point in the zigzag pattern, so we reverse the value of $k$, i.e., $k = -k$. Then, we update $i$ to $i + k$, which means moving up or down one row. Continue traversing the next character until the end of the string $s$. Finally, we return the concatenation of all rows in $g$ as the result.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of the string $s$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        g = [[] for _ in range(numRows)]
        i, k = 0, -1
        for c in s:
            g[i].append(c)
            if i == 0 or i == numRows - 1:
                k = -k
            i += k
        return ''.join(chain(*g))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
