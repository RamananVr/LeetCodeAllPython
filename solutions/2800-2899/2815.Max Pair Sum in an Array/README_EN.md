---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2815.Max%20Pair%20Sum%20in%20an%20Array/README_EN.md
rating: 1295
source: Weekly Contest 358 Q1
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [2815. Max Pair Sum in an Array](https://leetcode.com/problems/max-pair-sum-in-an-array)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>. You have to find the <strong>maximum</strong> sum of a pair of numbers from <code>nums</code> such that the <strong>largest digit </strong>in both numbers is equal.</p>

<p>For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.</p>

<p>Return the <strong>maximum</strong> sum or -1 if no such pair exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [112,131,411]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>Each numbers largest digit in order is [2,3,4].</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2536,1613,3366,162]</span></p>

<p><strong>Output:</strong> <span class="example-io">5902</span></p>

<p><strong>Explanation:</strong></p>

<p>All the numbers have 6 as their largest digit, so the answer is <span class="example-io">2536 + 3366 = 5902.</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [51,71,17,24,42]</span></p>

<p><strong>Output:</strong> <span class="example-io">88</span></p>

<p><strong>Explanation:</strong></p>

<p>Each number&#39;s largest digit in order is [5,7,7,4,4].</p>

<p>So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration

First, we initialize the answer variable $ans=-1$. Next, we directly enumerate all pairs $(nums[i], nums[j])$ where $i \lt j$, and calculate their sum $v=nums[i] + nums[j]$. If $v$ is greater than $ans$ and the largest digit of $nums[i]$ and $nums[j]$ are the same, then we update $ans$ with $v$.

The time complexity is $O(n^2 \times \log M)$, where $n$ is the length of the array and $M$ is the maximum value in the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        for i, x in enumerate(nums):
            for y in nums[i + 1 :]:
                v = x + y
                if ans < v and max(str(x)) == max(str(y)):
                    ans = v
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
