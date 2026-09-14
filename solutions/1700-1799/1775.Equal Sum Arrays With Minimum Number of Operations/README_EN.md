---
comments: true
difficulty: Medium
rating: 1850
source: Weekly Contest 230 Q3
tags:
    - Greedy
    - Array
    - Hash Table
    - Counting
---

<!-- problem:start -->

# [1775. Equal Sum Arrays With Minimum Number of Operations](https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations)

## Description

<!-- description:start -->

<p>You are given two arrays of integers <code>nums1</code> and <code><font face="monospace">nums2</font></code>, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.</p>

<p>In one operation, you can change any integer&#39;s value in <strong>any </strong>of the arrays to <strong>any</strong> value between 1 and 6, inclusive.</p>

<p>Return the <strong>minimum</strong> number of operations required to make the sum of values in <code>nums1</code> equal to the sum of values in <code>nums2</code>. Return -1​​​​​ if it is not possible to make the sum of the two arrays <strong>equal</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [<u><strong>6</strong></u>,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,<strong><u>1</u></strong>], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,<strong><u>2</u></strong>,4,5,1], nums2 = [6,1,2,2,2,2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,1,1,1,1,1,1], nums2 = [6]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [6,6], nums2 = [1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [<strong><u>2</u></strong>,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,<strong><u>2</u></strong>], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [<strong><u>4</u></strong>].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 6</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Values may only change inside $[1,6]$. We want equal sums with the fewest changes. $n\le 10^5$, so greedily spend the change that shrinks the gap most.
>
> Assume $s_1<s_2$. Each small-array entry can grow to $6$ and each large-array entry can shrink to $1$. Sort those deltas descending and subtract from the gap until it is nonpositive.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            return self.minOperations(nums2, nums1)
        arr = [6 - v for v in nums1] + [v - 1 for v in nums2]
        d = s2 - s1
        for i, v in enumerate(sorted(arr, reverse=True), 1):
            d -= v
            if d <= 0:
                return i
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Deltas lie in $0..5$, so sorting is unnecessary. A size-$6$ bucket from $5$ down to $1$ spends the gap in linear time.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            return self.minOperations(nums2, nums1)
        cnt = Counter([6 - v for v in nums1] + [v - 1 for v in nums2])
        d = s2 - s1
        ans = 0
        for i in range(5, 0, -1):
            while cnt[i] and d > 0:
                d -= i
                cnt[i] -= 1
                ans += 1
        return ans if d <= 0 else -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
