---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2680.Maximum%20OR/README_EN.md
rating: 1912
source: Biweekly Contest 104 Q3
tags:
    - Greedy
    - Bit Manipulation
    - Array
    - Prefix Sum
---

<!-- problem:start -->

# [2680. Maximum OR](https://leetcode.com/problems/maximum-or)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>. In an operation, you can choose an element and multiply it by <code>2</code>.</p>

<p>Return <em>the maximum possible value of </em><code>nums[0] | nums[1] | ... | nums[n - 1]</code> <em>that can be obtained after applying the operation on nums at most </em><code>k</code><em> times</em>.</p>

<p>Note that <code>a | b</code> denotes the <strong>bitwise or</strong> between two integers <code>a</code> and <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [12,9], k = 1
<strong>Output:</strong> 30
<strong>Explanation:</strong> If we apply the operation to index 1, our new array nums will be equal to [12,18]. Thus, we return the bitwise or of 12 and 18, which is 30.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [8,1,2], k = 2
<strong>Output:</strong> 35
<strong>Explanation:</strong> If we apply the operation twice on index 0, we yield a new array of [32,1,2]. Thus, we return 32|1|2 = 35.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 15</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Preprocessing

We notice that in order to maximize the answer, we should apply $k$ times of bitwise OR to the same number.

First, we preprocess the suffix OR value array $suf$ of the array $nums$, where $suf[i]$ represents the bitwise OR value of $nums[i], nums[i + 1], \cdots, nums[n - 1]$.

Next, we traverse the array $nums$ from left to right, and maintain the current prefix OR value $pre$. For the current position $i$, we perform $k$ times of bitwise left shift on $nums[i]$, i.e., $nums[i] \times 2^k$, and perform bitwise OR operation with $pre$ to obtain the intermediate result. Then, we perform bitwise OR operation with $suf[i + 1]$ to obtain the maximum OR value with $nums[i]$ as the last number. By enumerating all possible positions $i$, we can obtain the final answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] | nums[i]
        ans = pre = 0
        for i, x in enumerate(nums):
            ans = max(ans, pre | (x << k) | suf[i + 1])
            pre |= x
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
