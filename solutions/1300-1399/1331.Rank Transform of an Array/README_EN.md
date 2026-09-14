---
comments: true
difficulty: Easy
rating: 1355
source: Biweekly Contest 18 Q1
tags:
    - Array
    - Hash Table
    - Sorting
---

<!-- problem:start -->

# [1331. Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array)

## Description

<!-- description:start -->

<p>Given an array of integers&nbsp;<code>arr</code>, replace each element with its rank.</p>

<p>The rank represents how large the element is. The rank has the following rules:</p>

<ul>
	<li>Rank is an integer starting from 1.</li>
	<li>The larger the element, the larger the rank. If two elements are equal, their rank must be the same.</li>
	<li>Rank should be as small as possible.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [40,10,20,30]
<strong>Output:</strong> [4,1,2,3]
<strong>Explanation</strong>: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [100,100,100]
<strong>Output:</strong> [1,1,1]
<strong>Explanation</strong>: Same elements share the same rank.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [37,12,28,9,100,56,80,5,12]
<strong>Output:</strong> [5,3,4,2,8,6,7,1,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Discretization

<!-- thinking:start -->

> **Thinking**
>
> Replace each value by its $1$-based rank, sharing a rank on ties. Pairwise comparison is quadratic for $n \le 10^5$. Rank depends only on the position in the sorted unique list $t$; $\mathrm{bisect\_right}$ on $t$ yields that rank for every $x$.

<!-- thinking:end -->

First, we copy an array $t$, then sort and deduplicate it to obtain an array of length $m$ that is strictly monotonically increasing.

Next, we traverse the original array $arr$. For each element $x$ in the array, we use binary search to find the position of $x$ in $t$. The position plus one is the rank of $x$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $arr$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        t = sorted(set(arr))
        return [bisect_right(t, x) for x in arr]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Sorting + Hash Map

<!-- thinking:start -->

> **Thinking**
>
> A binary search per element repeats the same work. After sorting the unique values, a hash map from value to rank answers every lookup in expected constant time.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
