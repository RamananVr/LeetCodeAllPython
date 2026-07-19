---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3572.Maximize%20Y%E2%80%91Sum%20by%20Picking%20a%20Triplet%20of%20Distinct%20X%E2%80%91Values/README_EN.md
rating: 1319
source: Biweekly Contest 158 Q1
tags:
    - Greedy
    - Array
    - Hash Table
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3572. Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values](https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues)

## Description

<!-- description:start -->

<p>You are given two integer arrays <code>x</code> and <code>y</code>, each of length <code>n</code>. You must choose three <strong>distinct</strong> indices <code>i</code>, <code>j</code>, and <code>k</code> such that:</p>

<ul>
	<li><code>x[i] != x[j]</code></li>
	<li><code>x[j] != x[k]</code></li>
	<li><code>x[k] != x[i]</code></li>
</ul>

<p>Your goal is to <strong>maximize</strong> the value of <code>y[i] + y[j] + y[k]</code> under these conditions. Return the <strong>maximum</strong> possible sum that can be obtained by choosing such a triplet of indices.</p>

<p>If no such triplet exists, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">x = [1,2,1,3,2], y = [5,3,4,6,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose <code>i = 0</code> (<code>x[i] = 1</code>, <code>y[i] = 5</code>), <code>j = 1</code> (<code>x[j] = 2</code>, <code>y[j] = 3</code>), <code>k = 3</code> (<code>x[k] = 3</code>, <code>y[k] = 6</code>).</li>
	<li>All three values chosen from <code>x</code> are distinct. <code>5 + 3 + 6 = 14</code> is the maximum we can obtain. Hence, the output is 14.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">x = [1,2,1,2], y = [4,5,6,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There are only two distinct values in <code>x</code>. Hence, the output is -1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == x.length == y.length</code></li>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= x[i], y[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Greedy + Hash Table

We pair the elements of arrays $x$ and $y$ into a 2D array $\textit{arr}$, and then sort $\textit{arr}$ in descending order by the value of $y$. Next, we use a hash table to record the $x$ values that have already been selected, and iterate through $\textit{arr}$, each time selecting an $x$ value and its corresponding $y$ value that has not been chosen yet, until we have selected three distinct $x$ values.

If we manage to select three different $x$ values during the iteration, we return the sum of their corresponding $y$ values; if we finish iterating without selecting three distinct $x$ values, we return -1.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of arrays $\textit{x}$ and $\textit{y}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        arr = [(a, b) for a, b in zip(x, y)]
        arr.sort(key=lambda x: -x[1])
        vis = set()
        ans = 0
        for a, b in arr:
            if a in vis:
                continue
            vis.add(a)
            ans += b
            if len(vis) == 3:
                return ans
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
