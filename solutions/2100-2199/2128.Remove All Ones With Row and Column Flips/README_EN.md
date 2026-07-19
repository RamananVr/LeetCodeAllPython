---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2100-2199/2128.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips/README_EN.md
tags:
    - Bit Manipulation
    - Array
    - Math
    - Matrix
---

<!-- problem:start -->

# [2128. Remove All Ones With Row and Column Flips 🔒](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> binary matrix <code>grid</code>.</p>

<p>In one operation, you can choose <strong>any</strong> row or column and flip each value in that row or column (i.e., changing all <code>0</code>&#39;s to <code>1</code>&#39;s, and all <code>1</code>&#39;s to <code>0</code>&#39;s).</p>

<p>Return <code>true</code><em> if it is possible to remove all </em><code>1</code><em>&#39;s from </em><code>grid</code> using <strong>any</strong> number of operations or <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2128.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips/images/image-20220103191300-1.png" style="width: 756px; height: 225px;" />
<pre>
<strong>Input:</strong> grid = [[0,1,0],[1,0,1],[0,1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> One possible way to remove all 1&#39;s from grid is to:
- Flip the middle row
- Flip the middle column
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2128.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips/images/image-20220103181204-7.png" style="width: 237px; height: 225px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,0],[0,0,0],[0,0,0]]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to remove all 1&#39;s from grid.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2128.Remove%20All%20Ones%20With%20Row%20and%20Column%20Flips/images/image-20220103181224-8.png" style="width: 114px; height: 100px;" />
<pre>
<strong>Input:</strong> grid = [[0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are no 1&#39;s in grid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We observe that if two rows in the matrix satisfy one of the following conditions, they can be made equal by flipping certain columns:

1. The corresponding elements of the two rows are equal, i.e., if one row is $1,0,0,1$, the other row is also $1,0,0,1$;
1. The corresponding elements of the two rows are opposite, i.e., if one row is $1,0,0,1$, the other row is $0,1,1,0$.

We call two rows that satisfy one of the above conditions "equivalent rows." The answer to the problem is the maximum number of equivalent rows in the matrix.

Therefore, we can traverse each row of the matrix and convert each row into an "equivalent row" that starts with $0$. Specifically:

- If the first element of the current row is $0$, keep the row unchanged;
- If the first element of the current row is $1$, flip every element in the row, i.e., $0$ becomes $1$, $1$ becomes $0$. In other words, we flip rows starting with $1$ into "equivalent rows" starting with $0$.

In this way, we only need to use a hash table to count each converted row. If the hash table contains only one element at the end, it means we can remove all $1$s from the matrix by flipping rows or columns.

The time complexity is $O(mn)$ and the space complexity is $O(m)$, where $m$ and $n$ are the number of rows and columns in the matrix, respectively.

Related problem:

- [1072. Flip Columns For Maximum Number of Equal Rows](https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1072.Flip%20Columns%20For%20Maximum%20Number%20of%20Equal%20Rows/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        s = set()
        for row in grid:
            t = tuple(row) if row[0] == grid[0][0] else tuple(x ^ 1 for x in row)
            s.add(t)
        return len(s) == 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
