---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3737.Count%20Subarrays%20With%20Majority%20Element%20I/README_EN.md
rating: 1422
source: Biweekly Contest 169 Q2
tags:
    - Segment Tree
    - Array
    - Hash Table
    - Divide and Conquer
    - Counting
    - Prefix Sum
    - Merge Sort
---

<!-- problem:start -->

# [3737. Count Subarrays With Majority Element I](https://leetcode.com/problems/count-subarrays-with-majority-element-i)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and an integer <code>target</code>.</p>

<p>Return the number of <strong><span data-keyword="subarray-nonempty">subarrays</span></strong> of <code>nums</code> in which <code>target</code> is the <strong>majority element</strong>.</p>

<p>The <strong>majority element</strong> of a subarray is the element that appears <strong>strictly</strong> <strong>more than half</strong> of the times in that subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2,3], target = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>Valid subarrays with <code>target = 2</code> as the majority element:</p>

<ul>
	<li><code>nums[1..1] = [2]</code></li>
	<li><code>nums[2..2] = [2]</code></li>
	<li><code>nums[1..2] = [2,2]</code></li>
	<li><code>nums[0..2] = [1,2,2]</code></li>
	<li><code>nums[1..3] = [2,2,3]</code></li>
</ul>

<p>So there are 5 such subarrays.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1], target = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation: </strong></p>

<p><strong>​​​​​​​</strong>All 10 subarrays have 1 as the majority element.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3], target = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><code>target = 4</code> does not appear in <code>nums</code> at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>​​​​​​​9</sup></code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration

We can enumerate all subarrays and maintain a counter $\textit{cnt}$ to record the number of times $\textit{target}$ appears in the subarray, then determine whether $\textit{target}$ is the majority element of that subarray.

Specifically, we enumerate the starting position $i$ of the subarray in the range $[0, n-1]$, then enumerate the ending position $j$ in the range $[i, n-1]$. For each subarray $nums[i..j]$, we update the counter $\textit{cnt}$. If $\textit{cnt} \times 2 > j - i + 1$, it means $\textit{target}$ is the majority element of this subarray, and we increment the answer by $1$.

The time complexity is $O(n^2)$, and the space complexity is $O(1)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                cnt += int(nums[j] == target)
                if cnt * 2 > j - i + 1:
                    ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
