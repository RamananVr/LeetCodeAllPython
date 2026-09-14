---
comments: true
difficulty: Medium
rating: 1797
source: Weekly Contest 139 Q2
tags:
    - Array
    - Hash Table
    - Matrix
---

<!-- problem:start -->

# [1072. Flip Columns For Maximum Number of Equal Rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> binary matrix <code>matrix</code>.</p>

<p>You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from <code>0</code> to <code>1</code> or vice versa).</p>

<p>Return <em>the maximum number of rows that have all values equal after some number of flips</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[0,1],[1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> After flipping no values, 1 row has all values equal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[0,1],[1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> After flipping values in the first column, both rows have equal values.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[0,0,0],[0,0,1],[1,1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> After flipping values in the first two columns, the last two rows have equal values.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>matrix[i][j]</code> is either&nbsp;<code>0</code> or <code>1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> After some column flips, identical rows become all zeros or all ones. Two rows can become equal iff they are equal or bitwise complements. $m,n\le 300$ rules out enumerating $2^n$ flip masks.
>
> Normalize each row so the first bit is $0$ (flip the whole row when it starts with $1$). Complements then share a key.
>
> A counter of those tuples; the maximum frequency is the answer.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            cnt[t] += 1
        return max(cnt.values())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
