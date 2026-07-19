---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3600-3699/3641.Longest%20Semi-Repeating%20Subarray/README_EN.md
tags:
    - Array
    - Hash Table
    - Sliding Window
---

<!-- problem:start -->

# [3641. Longest Semi-Repeating Subarray 🔒](https://leetcode.com/problems/longest-semi-repeating-subarray)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>A <strong>semi‑repeating</strong> subarray is a contiguous subarray in which at most <code>k</code> elements repeat (i.e., appear more than once).</p>

<p>Return the length of the longest <strong>semi‑repeating</strong> subarray in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,1,2,3,4], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repeating subarray is <code>[2, 3, 1, 2, 3, 4]</code>, which has two repeating elements (2 and 3).</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1,1], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repeating subarray is <code>[1, 1, 1, 1, 1]</code>, which has only one repeating element (1).</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1,1], k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repeating subarray is <code>[1]</code>, which has no repeating elements.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sliding Window

We use two pointers $l$ and $r$ to maintain a sliding window, where the right pointer continuously moves to the right, and we use a hash table $\textit{cnt}$ to record the number of occurrences of each element within the current window.

When the occurrence count of an element changes from $1$ to $2$, it indicates that there is a new repeating element, so we increment the repeating element counter $\textit{cur}$ by $1$. When the repeating element counter exceeds $k$, it means the current window does not satisfy the condition, and we need to move the left pointer until the repeating element counter is no greater than $k$. During the process of moving the left pointer, if the occurrence count of an element changes from $2$ to $1$, it indicates that there is one less repeating element, so we decrement the repeating element counter by $1$. Then, we update the answer, i.e., $\textit{ans} = \max(\textit{ans}, r - l + 1)$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestSubarray(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = cur = l = 0
        for r, x in enumerate(nums):
            cnt[x] += 1
            cur += cnt[x] == 2
            while cur > k:
                cnt[nums[l]] -= 1
                cur -= cnt[nums[l]] == 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
