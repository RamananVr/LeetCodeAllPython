---
comments: true
difficulty: Hard
rating: 2133
source: Weekly Contest 187 Q4
tags:
    - Array
    - Binary Search
    - Matrix
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows)

## Description

<!-- description:start -->

<p>You are given an <code>m x n</code> matrix <code>mat</code> that has its rows sorted in non-decreasing order and an integer <code>k</code>.</p>

<p>You are allowed to choose <strong>exactly one element</strong> from each row to form an array.</p>

<p>Return <em>the </em><code>k<sup>th</sup></code><em> smallest array sum among all possible arrays</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,3,11],[2,4,6]], k = 5
<strong>Output:</strong> 7
<strong>Explanation:</strong> Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,3,11],[2,4,6]], k = 9
<strong>Output:</strong> 17
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
<strong>Output:</strong> 9
<strong>Explanation:</strong> Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.  
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat.length[i]</code></li>
	<li><code>1 &lt;= m, n &lt;= 40</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 5000</code></li>
	<li><code>1 &lt;= k &lt;= min(200, n<sup>m</sup>)</code></li>
	<li><code>mat[i]</code> is a non-decreasing array.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> One value per row yields $n^m$ sums, but $k\le 200$. We only need the $k$ smallest partial sums. Rows are sorted, so combining with the next row uses at most its first $k$ entries.
>
> Let $pre$ be the $k$ smallest sums so far. Cartesian-add the current row, sort, and keep $k$ values. After the last row, $pre[k-1]$ is the answer.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        pre = [0]
        for cur in mat:
            pre = sorted(a + b for a in pre for b in cur[:k])[:k]
        return pre[-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
