---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3830.Longest%20Alternating%20Subarray%20After%20Removing%20At%20Most%20One%20Element/README_EN.md
rating: 2162
source: Weekly Contest 487 Q4
tags:
    - Array
    - Dynamic Programming
    - Enumeration
---

<!-- problem:start -->

# [3830. Longest Alternating Subarray After Removing At Most One Element](https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>A <span data-keyword="subarray">subarray</span> <code>nums[l..r]</code> is <strong>alternating</strong> if one of the following holds:</p>

<ul>
	<li><code>nums[l] &lt; nums[l + 1] &gt; nums[l + 2] &lt; nums[l + 3] &gt; ...</code></li>
	<li><code>nums[l] &gt; nums[l + 1] &lt; nums[l + 2] &gt; nums[l + 3] &lt; ...</code></li>
</ul>

<p>In other words, if we compare adjacent elements in the subarray, then the comparisons alternate between <strong>strictly</strong> greater and <strong>strictly</strong> smaller.</p>

<p>You can remove <strong>at most one</strong> element from <code>nums</code>. Then, you select an alternating subarray from <code>nums</code>.</p>

<p>Return an integer denoting the <strong>maximum</strong> <strong>length</strong> of the alternating subarray you can select.</p>

<p>A subarray of length 1 is considered alternating.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose not to remove elements.</li>
	<li>Select the entire array <code>[<u><strong>2, 1, 3, 2</strong></u>]</code>, which is alternating because <code>2 &gt; 1 &lt; 3 &gt; 2</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,1,2,3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose to remove <code>nums[3]</code> i.e., <code>[3, 2, 1, <u><strong>2</strong></u>, 3, 2, 1]</code>. The array becomes <code>[3, 2, 1, 3, 2, 1]</code>.</li>
	<li>Select the subarray <code>[3, <strong><u>2, 1, 3, 2</u></strong>, 1]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [100000,100000]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Choose not to remove elements.</li>
	<li>Select the subarray <code>[100000, <u><strong>100000</strong></u>]</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix-Suffix Decomposition + Enumeration

We use two arrays $l_1$ and $l_2$ to represent the length of the longest alternating subarray ending at position $i$ with the last comparison being "<" and ">", respectively. Similarly, we use $r_1$ and $r_2$ to represent the length of the longest alternating subarray starting at position $i$ with the first comparison being "<" and ">", respectively.

We can compute $l_1$ and $l_2$ through a single left-to-right traversal, and then compute $r_1$ and $r_2$ through a single right-to-left traversal.

Next, we initialize the answer as $\max(\max(l_1), \max(l_2))$, which represents the length of the longest alternating subarray without removing any elements.

Then, we enumerate the position $i$ of the element to be removed. If after removing position $i$, positions $i-1$ and $i+1$ can still form an alternating relationship, we can add $l_1[i-1]$ and $r_1[i+1]$ (or $l_2[i-1]$ and $r_2[i+1]$) together to update the answer.

The time complexity is $O(n)$ and the space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        l1 = [1] * n
        l2 = [1] * n
        r1 = [1] * n
        r2 = [1] * n
        ans = 0
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                l1[i] = l2[i - 1] + 1
            elif nums[i - 1] > nums[i]:
                l2[i] = l1[i - 1] + 1
            ans = max(ans, l1[i], l2[i])
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                r1[i] = r2[i + 1] + 1
            elif nums[i + 1] < nums[i]:
                r2[i] = r1[i + 1] + 1
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i + 1]:
                ans = max(ans, l2[i - 1] + r2[i + 1])
            elif nums[i - 1] > nums[i + 1]:
                ans = max(ans, l1[i - 1] + r1[i + 1])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
