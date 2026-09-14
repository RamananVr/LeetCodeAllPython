---
comments: true
difficulty: Medium
rating: 1855
source: Weekly Contest 201 Q3
tags:
    - Greedy
    - Array
    - Hash Table
    - Prefix Sum
---

<!-- problem:start -->

# [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target)

## Description

<!-- description:start -->

<p>Given an array <code>nums</code> and an integer <code>target</code>, return <em>the maximum number of <strong>non-empty</strong> <strong>non-overlapping</strong> subarrays such that the sum of values in each subarray is equal to</em> <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1], target = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 non-overlapping subarrays [<strong>1,1</strong>,1,<strong>1,1</strong>] with sum equals to target(2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,3,5,1,4,2,-9], target = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= target &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Prefix Sum + Hash Table

<!-- thinking:start -->

> **Thinking**
>
> Select as many non-overlapping subarrays of sum $target$ as possible. $n\le 10^5$ rules out interval DP. When two candidates overlap, keeping the one that ends further left never hurts later choices.
>
> Scan with a prefix-sum set, take the earliest subarray that hits $target$, then restart after it. The greedy always finishes a piece as soon as possible and leaves more room to the right.

<!-- thinking:end -->

We traverse the array $nums$, using the method of prefix sum + hash table, to find subarrays with a sum of $target$. If found, we increment the answer by one, then we set the prefix sum to $0$ and continue to traverse the array $nums$ until the entire array is traversed.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ans = 0
        i, n = 0, len(nums)
        while i < n:
            s = 0
            vis = {0}
            while i < n:
                s += nums[i]
                if s - target in vis:
                    ans += 1
                    break
                i += 1
                vis.add(s)
            i += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
