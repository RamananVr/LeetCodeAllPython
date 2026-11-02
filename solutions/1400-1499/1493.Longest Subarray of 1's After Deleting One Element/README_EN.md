---
comments: true
difficulty: Medium
rating: 1423
source: Biweekly Contest 29 Q3
tags:
    - Array
    - Dynamic Programming
    - Sliding Window
---

<!-- problem:start -->

# [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element)

## Description

<!-- description:start -->

<p>You are given a binary array <code>nums</code>, you should delete <strong>one</strong> element from it.</p>

<p>Return the size of the <strong>longest non-empty subarray</strong> containing only 1&#39;s in the resulting array. Return 0 if there is no such <strong>subarray</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,0,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1&#39;s.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,1,1,0,1,1,0,1]
<strong>Output:</strong> 5
<strong>Explanation:</strong> After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1&#39;s is [1,1,1,1,1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> You must delete one element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either 0 or 1.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration

<!-- thinking:start -->

> **Thinking**
>
> Exactly one element is deleted, so the answer is the ones immediately left of $i$ plus those immediately right. $n\le 10^5$. Precompute longest ones ending before $i$ and starting after $i$, then maximize over the deleted index.

<!-- thinking:end -->

We can enumerate each position $i$ to be deleted, then calculate the number of consecutive 1s on the left and right, and finally take the maximum value.

Specifically, we use two arrays $\textit{left}$ and $\textit{right}$ of length $n+1$, where $\textit{left}[i]$ represents the number of consecutive 1s ending with $\textit{nums}[i-1]$, and $\textit{right}[i]$ represents the number of consecutive 1s starting with $\textit{nums}[i]$.

The final answer is $\max_{0 \leq i < n} \{\textit{left}[i] + \textit{right}[i+1]\}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        for i, x in enumerate(nums, 1):
            if x:
                left[i] = left[i - 1] + 1
        for i in range(n - 1, -1, -1):
            if nums[i]:
                right[i] = right[i + 1] + 1
        return max(left[i] + right[i + 1] for i in range(n))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Two Pointers

<!-- thinking:start -->

> **Thinking**
>
> Method 1 stores two arrays. Equivalently, find the longest window with at most one $0$; after deleting that $0$ (or one $1$) the length is $i-j$. Expand the right end and shrink while the zero count exceeds $1$.

<!-- thinking:end -->

The problem is actually asking us to find the longest subarray that contains at most one $0$. The remaining length after deleting one element from this subarray is the answer.

Therefore, we can use two pointers $j$ and $i$ to point to the left and right boundaries of the subarray, initially $j = 0$, $i = 0$. In addition, we use a variable $\textit{cnt}$ to record the number of $0$s in the subarray.

Next, we move the right pointer $i$. If $\textit{nums}[i] = 0$, then $\textit{cnt}$ is incremented by $1$. When $\textit{cnt} > 1$, we need to move the left pointer $j$ until $\textit{cnt} \leq 1$. Then, we update the answer, i.e., $\textit{ans} = \max(\textit{ans}, i - j)$. Continue to move the right pointer $i$ until $i$ reaches the end of the array.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = j = 0
        for i, x in enumerate(nums):
            cnt += x ^ 1
            while cnt > 1:
                cnt -= nums[j] ^ 1
                j += 1
            ans = max(ans, i - j)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Two Pointers (Optimization)

<!-- thinking:start -->

> **Thinking**
>
> Method 2 may shrink the window when zeros exceed one. We only need the maximum length, so move the left end once whenever the count is too large and keep the window non-decreasing. The answer is $n-l-1$.

<!-- thinking:end -->

In Solution 2, we move the left pointer in a loop until $\textit{cnt} \leq 1$. Since the problem asks for the longest subarray, it means we don't need to reduce the length of the subarray. Therefore, if $\textit{cnt} \gt 1$, we only move the left pointer once, and the right pointer continues to move to the right. This ensures that the length of the subarray does not decrease.

Finally, the answer we return is $n - l - 1$, where $l$ is the position of the left pointer.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = l = 0
        for x in nums:
            cnt += x ^ 1
            if cnt > 1:
                cnt -= nums[l] ^ 1
                l += 1
        return len(nums) - l - 1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
