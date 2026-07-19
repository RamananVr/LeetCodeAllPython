---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3566.Partition%20Array%20into%20Two%20Equal%20Product%20Subsets/README_EN.md
rating: 1459
source: Weekly Contest 452 Q1
tags:
    - Bit Manipulation
    - Recursion
    - Array
    - Enumeration
---

<!-- problem:start -->

# [3566. Partition Array into Two Equal Product Subsets](https://leetcode.com/problems/partition-array-into-two-equal-product-subsets)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> containing <strong>distinct</strong> positive integers and an integer <code>target</code>.</p>

<p>Determine if you can partition <code>nums</code> into two <strong>non-empty</strong> <strong>disjoint</strong> <strong>subsets</strong>, with each element belonging to <strong>exactly one</strong> subset, such that the product of the elements in each subset is equal to <code>target</code>.</p>

<p>Return <code>true</code> if such a partition exists and <code>false</code> otherwise.</p>
A <strong>subset</strong> of an array is a selection of elements of the array.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,6,8,4], target = 24</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong> The subsets <code>[3, 8]</code> and <code>[1, 6, 4]</code> each have a product of 24. Hence, the output is true.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,5,3,7], target = 15</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong> There is no way to partition <code>nums</code> into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 12</code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>15</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li>All elements of <code>nums</code> are <strong>distinct</strong>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Enumeration

We can use binary enumeration to check all possible subset partitions. For each subset partition, we can calculate the product of the two subsets and check whether both are equal to the target value.

Specifically, we can use an integer $i$ to represent the state of the subset partition, where the binary bits of $i$ indicate whether each element belongs to the first subset. For each possible $i$, we calculate the product of the two subsets and check whether both are equal to the target value.

The time complexity is $O(2^n \times n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        for i in range(1 << n):
            x = y = 1
            for j in range(n):
                if i >> j & 1:
                    x *= nums[j]
                else:
                    y *= nums[j]
            if x == target and y == target:
                return True
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
