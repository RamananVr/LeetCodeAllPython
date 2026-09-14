---
comments: true
difficulty: Hard
rating: 2723
source: Weekly Contest 431 Q4
tags:
    - Array
    - Binary Search
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [3414. Maximum Score of Non-overlapping Intervals](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals)

## Description

<!-- description:start -->

<p>You are given a 2D integer array <code>intervals</code>, where <code>intervals[i] = [l<sub>i</sub>, r<sub>i</sub>, weight<sub>i</sub>]</code>. Interval <code>i</code> starts at position <code>l<sub>i</sub></code> and ends at <code>r<sub>i</sub></code>, and has a weight of <code>weight<sub>i</sub></code>. You can choose <em>up to</em> 4 <strong>non-overlapping</strong> intervals. The <strong>score</strong> of the chosen intervals is defined as the total sum of their weights.</p>

<p>Return the <span data-keyword="lexicographically-smaller-array">lexicographically smallest</span> array of at most 4 indices from <code>intervals</code> with <strong>maximum</strong> score, representing your choice of non-overlapping intervals.</p>

<p>Two intervals are said to be <strong>non-overlapping</strong> if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,3]</span></p>

<p><strong>Explanation:</strong></p>

<p>You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3,5,6]</span></p>

<p><strong>Explanation:</strong></p>

<p>You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intevals.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 3</code></li>
	<li><code>intervals[i] = [l<sub>i</sub>, r<sub>i</sub>, weight<sub>i</sub>]</code></li>
	<li><code>1 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= weight<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Binary Search + Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> We pick at most four non-overlapping weighted intervals to maximize the total weight, breaking ties by the lexicographically smallest index tuple. $n\le 5\times 10^4$ forbids subset search.
>
> This is weighted interval scheduling with a cap of four. After sorting by left endpoint, the next non-overlapping interval is a binary search.
>
> State $(i,k)$ starts at interval $i$ with $k$ picks remaining. We either skip $i$ or take it and jump to $\textit{nxt}[i]$, comparing both weight and the index list so the lexicographically smallest optimum is kept.

<!-- thinking:end -->

Copy the intervals and record each original index, then sort by left endpoint. For each interval $i$, binary-search the first position $\textit{nxt}[i]$ whose left endpoint is strictly greater than $i$'s right endpoint (shared endpoints count as overlap).

Let $f[i][k]$ be the maximum weight obtainable from interval $i$ onward with at most $k$ picks, and let $g[i][k]$ store the corresponding lexicographically smallest index list. Transition from the back: skipping $i$ inherits $f[i+1][k]$; taking $i$ inserts its original index into $g[\textit{nxt}[i]][k-1]$ and adds the current weight. Keep the larger weight, or the lexicographically smaller index list on a tie. The answer is $g[0][4]$.

The time complexity is $O(n \times \log n)$ and the space complexity is $O(n)$. At most $4$ intervals are chosen, so inserting and comparing index lists is constant time.

<!-- tabs:start -->

#### Python3

```python

```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
