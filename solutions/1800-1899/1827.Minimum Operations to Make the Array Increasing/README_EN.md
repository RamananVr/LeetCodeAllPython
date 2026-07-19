---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1827.Minimum%20Operations%20to%20Make%20the%20Array%20Increasing/README_EN.md
rating: 1314
source: Biweekly Contest 50 Q1
tags:
    - Greedy
    - Array
---

<!-- problem:start -->

# [1827. Minimum Operations to Make the Array Increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> (<strong>0-indexed</strong>). In one operation, you can choose an element of the array and increment it by <code>1</code>.</p>

<ul>

    <li>For example, if <code>nums = [1,2,3]</code>, you can choose to increment <code>nums[1]</code> to make <code>nums = [1,<u><b>3</b></u>,3]</code>.</li>

</ul>

<p>Return <em>the <strong>minimum</strong> number of operations needed to make</em> <code>nums</code> <em><strong>strictly</strong> <strong>increasing</strong>.</em></p>

<p>An array <code>nums</code> is <strong>strictly increasing</strong> if <code>nums[i] &lt; nums[i+1]</code> for all <code>0 &lt;= i &lt; nums.length - 1</code>. An array of length <code>1</code> is trivially strictly increasing.</p>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>

<strong>Input:</strong> nums = [1,1,1]

<strong>Output:</strong> 3

<strong>Explanation:</strong> You can do the following operations:

1) Increment nums[2], so nums becomes [1,1,<u><strong>2</strong></u>].

2) Increment nums[1], so nums becomes [1,<u><strong>2</strong></u>,2].

3) Increment nums[2], so nums becomes [1,2,<u><strong>3</strong></u>].

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>

<strong>Input:</strong> nums = [1,5,2,4,1]

<strong>Output:</strong> 14

</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>

<strong>Input:</strong> nums = [8]

<strong>Output:</strong> 0

</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>1 &lt;= nums.length &lt;= 5000</code></li>

    <li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Single Pass

We use a variable $mx$ to record the maximum value of the current strictly increasing array, initially $mx = 0$.

Traverse the array `nums` from left to right. For the current element $v$, if $v \lt mx + 1$, we need to increase it to $mx + 1$ to ensure the array is strictly increasing. Therefore, the number of operations we need to perform this time is $max(0, mx + 1 - v)$, which is added to the answer, and then we update $mx=max(mx + 1, v)$. Continue to traverse the next element until the entire array is traversed.

The time complexity is $O(n)$, where $n$ is the length of the array `nums`. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = mx = 0
        for v in nums:
            ans += max(0, mx + 1 - v)
            mx = max(mx + 1, v)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
