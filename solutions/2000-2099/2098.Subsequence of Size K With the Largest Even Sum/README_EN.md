---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2098.Subsequence%20of%20Size%20K%20With%20the%20Largest%20Even%20Sum/README_EN.md
tags:
    - Greedy
    - Array
    - Sorting
---

<!-- problem:start -->

# [2098. Subsequence of Size K With the Largest Even Sum 🔒](https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. Find the <strong>largest even sum</strong> of any subsequence of <code>nums</code> that has a length of <code>k</code>.</p>

<p>Return <em>this sum, or </em><code>-1</code><em> if such a sum does not exist</em>.</p>

<p>A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,1,5,3,1], k = 3
<strong>Output:</strong> 12
<strong>Explanation:</strong>
The subsequence with the largest possible even sum is [4,5,3]. It has a sum of 4 + 5 + 3 = 12.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,6,2], k = 3
<strong>Output:</strong> 12
<strong>Explanation:</strong>
The subsequence with the largest possible even sum is [4,6,2]. It has a sum of 4 + 6 + 2 = 12.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5], k = 1
<strong>Output:</strong> -1
<strong>Explanation:</strong>
No subsequence of nums with length 1 has an even sum.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Sorting

We notice that the problem involves selecting a subsequence, so we can consider sorting the array first.

Next, we greedily select the largest $k$ numbers. If the sum of these numbers is even, we directly return this sum $ans$.

Otherwise, we have two greedy strategies:

1. Among the largest $k$ numbers, find the smallest even number $mi1$, and then among the remaining $n - k$ numbers, find the largest odd number $mx1$. Replace $mi1$ with $mx1$. If such a replacement exists, then the sum after replacement $ans - mi1 + mx1$ is guaranteed to be even;
2. Among the largest $k$ numbers, find the smallest odd number $mi2$, and then among the remaining $n - k$ numbers, find the largest even number $mx2$. Replace $mi2$ with $mx2$. If such a replacement exists, then the sum after replacement $ans - mi2 + mx2$ is guaranteed to be even.

We take the largest even sum as the answer. If no even sum exists, return $-1$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(\log n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = sum(nums[-k:])
        if ans % 2 == 0:
            return ans
        n = len(nums)
        mx1 = mx2 = -inf
        for x in nums[: n - k]:
            if x & 1:
                mx1 = x
            else:
                mx2 = x
        mi1 = mi2 = inf
        for x in nums[-k:][::-1]:
            if x & 1:
                mi2 = x
            else:
                mi1 = x
        ans = max(ans - mi1 + mx1, ans - mi2 + mx2, -1)
        return -1 if ans < 0 else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
