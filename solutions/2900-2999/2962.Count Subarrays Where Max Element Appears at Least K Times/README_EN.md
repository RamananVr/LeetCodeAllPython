---
comments: true
difficulty: Medium
rating: 1700
source: Weekly Contest 375 Q3
tags:
    - Array
    - Sliding Window
---

<!-- problem:start -->

# [2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and a <strong>positive</strong> integer <code>k</code>.</p>

<p>Return <em>the number of subarrays where the <strong>maximum</strong> element of </em><code>nums</code><em> appears <strong>at least</strong> </em><code>k</code><em> times in that subarray.</em></p>

<p>A <strong>subarray</strong> is a contiguous sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,3,3], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4,2,1], k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> No subarray contains the element 4 at least 3 times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers

<!-- thinking:start -->

> **Thinking**
>
> A subarray must contain the global maximum at least $k$ times. $n \le 10^5$ forbids enumeration. For a fixed left end, the earliest right end that gathers $k$ copies of $mx$ is monotone, and every later right end stays valid.
>
> Two pointers maintain $cnt$. After each left step, advance $j$ as needed, add $n-j+1$, then drop the leaving $mx$.

<!-- thinking:end -->

Let's denote the maximum value in the array as $mx$.

We use two pointers $i$ and $j$ to maintain a sliding window, such that in the subarray between $[i, j)$, there are $k$ elements equal to $mx$. If we fix the left endpoint $i$, then all right endpoints greater than or equal to $j-1$ meet the condition, totaling $n - (j - 1)$.

Therefore, we enumerate the left endpoint $i$, use the pointer $j$ to maintain the right endpoint, use a variable $cnt$ to record the number of elements equal to $mx$ in the current window. When $cnt$ is greater than or equal to $k$, we have found a subarray that meets the condition, and we increase the answer by $n - (j - 1)$. Then we update $cnt$ and continue to enumerate the next left endpoint.

The time complexity is $O(n)$, where $n$ is the length of the array $nums$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        ans = cnt = j = 0
        for x in nums:
            while j < n and cnt < k:
                cnt += nums[j] == mx
                j += 1
            if cnt < k:
                break
            ans += n - j + 1
            cnt -= x == mx
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
