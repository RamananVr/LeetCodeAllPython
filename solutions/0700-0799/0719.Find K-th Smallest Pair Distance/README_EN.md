---
comments: true
difficulty: Hard
tags:
    - Array
    - Two Pointers
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [719. Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance)

## Description

<!-- description:start -->

<p>The <strong>distance of a pair</strong> of integers <code>a</code> and <code>b</code> is defined as the absolute difference between <code>a</code> and <code>b</code>.</p>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest <strong>distance among all the pairs</strong></em> <code>nums[i]</code> <em>and</em> <code>nums[j]</code> <em>where</em> <code>0 &lt;= i &lt; j &lt; nums.length</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,1], k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> Here are all the pairs:
(1,3) -&gt; 2
(1,1) -&gt; 0
(3,1) -&gt; 2
Then the 1<sup>st</sup> smallest distance pair is (1,1), and its distance is 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1], k = 2
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,6,1], k = 3
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= n * (n - 1) / 2</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> We want the $k$-th smallest pairwise distance. $n\le 10^4$ forbids listing all $O(n^2)$ pairs. Distances lie in $[0,\max-\min]$ and the count of pairs $\le d$ is monotone in $d$.
>
> Binary-search $d$ and count pairs with distance $\le d$. After sorting, each right value $b$ has a leftmost partner $b-d$; a lower-bound search counts them in $O(n\log n)$.
>
> The smallest $d$ whose count is at least $k$ is the answer, searched in $[0, nums[-1]-nums[0]]$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(dist):
            cnt = 0
            for i, b in enumerate(nums):
                a = b - dist
                j = bisect_left(nums, a, 0, i)
                cnt += i - j
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
