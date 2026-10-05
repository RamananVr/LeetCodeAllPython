---
comments: true
difficulty: Medium
tags:
    - Array
    - Bucket Sort
    - Radix Sort
    - Sorting
    - Pigeonhole Principle
---

<!-- problem:start -->

# [164. Maximum Gap](https://leetcode.com/problems/maximum-gap)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return <em>the maximum difference between two successive elements in its sorted form</em>. If the array contains less than two elements, return <code>0</code>.</p>

<p>You must write an algorithm that runs in linear time and uses linear extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,6,9,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The array contains less than 2 elements, therefore return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Bucket Sort

<!-- thinking:start -->

> **Thinking**
>
> Maximum gap after sorting, in linear time. Comparison sorts are $O(n\log n)$; $n\le 10^5$. The max adjacent gap is at least $(\textit{max}-\textit{min})/(n-1)$. Bucket by that width: gaps inside a bucket are smaller than this lower bound, so the answer is between consecutive non-empty buckets (next min minus previous max). Each bucket stores only min and max.

<!-- thinking:end -->

Suppose $nums$ has $n$ elements. After sorting them into $nums_0 \le \cdots \le nums_{n-1}$, the maximum adjacent gap $maxGap$ satisfies

$$
nums_{n-1} - nums_0 = \sum_{i=1}^{n-1}(nums_i - nums_{i-1}) \le maxGap \times (n-1).
$$

Hence $maxGap \ge \dfrac{nums_{n-1} - nums_0}{n-1}$.

Use that lower bound as the bucket width, and at least $1$ when every value is equal. Values that fall in the same bucket differ by less than $maxGap$, so a gap of size $maxGap$ always crosses two buckets. Each bucket keeps only its minimum and its maximum, initialized to $+\infty$ and $-\infty$ to mark an empty bucket.

Place every value $v$ into bucket $\lfloor(v - \min) / \textit{bucketSize}\rfloor$. Smaller indices then hold smaller values. Scan the buckets from left to right. The minimum of the current non-empty bucket and the maximum of the previous non-empty bucket are adjacent in sorted order; their difference updates the answer. There is no gap before the first non-empty bucket.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        mi, mx = min(nums), max(nums)
        bucket_size = max(1, (mx - mi) // (n - 1))
        bucket_count = (mx - mi) // bucket_size + 1
        buckets = [[inf, -inf] for _ in range(bucket_count)]
        for v in nums:
            i = (v - mi) // bucket_size
            buckets[i][0] = min(buckets[i][0], v)
            buckets[i][1] = max(buckets[i][1], v)
        ans = 0
        prev = inf
        for curmin, curmax in buckets:
            if curmin > curmax:
                continue
            ans = max(ans, curmin - prev)
            prev = curmax
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
