---
comments: true
difficulty: Medium
tags:
    - Array
    - Hash Table
    - Prefix Sum
    - Sliding Window
---

<!-- problem:start -->

# [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum)

## Description

<!-- description:start -->

<p>Given a binary array <code>nums</code> and an integer <code>goal</code>, return <em>the number of non-empty <strong>subarrays</strong> with a sum</em> <code>goal</code>.</p>

<p>A <strong>subarray</strong> is a contiguous part of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,0,1], goal = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> The 4 subarrays are bolded and underlined below:
[<u><strong>1,0,1</strong></u>,0,1]
[<u><strong>1,0,1,0</strong></u>,1]
[1,<u><strong>0,1,0,1</strong></u>]
[1,0,<u><strong>1,0,1</strong></u>]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0,0,0], goal = 0
<strong>Output:</strong> 15
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>0 &lt;= goal &lt;= nums.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Count subarrays of a $0/1$ array whose sum is $\textit{goal}$. $n$ is large, so enumerating intervals is too slow. When the prefix sum is $s$, the number of earlier prefixes equal to $s-\textit{goal}$ is the number of good subarrays ending here. A counter of prefix frequencies, starting at $cnt[0]=1$, answers each step in $O(1)$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = Counter({0: 1})
        ans = s = 0
        for v in nums:
            s += v
            ans += cnt[s - goal]
            cnt[s] += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Method 1 uses linear extra space. Because the array is non-negative, the window sum is monotone in the left end. Two left pointers keep the first index whose sum exceeds $\textit{goal}$ and the first whose sum is at least $\textit{goal}$; their difference is the number of windows with sum exactly $\textit{goal}$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        i1 = i2 = s1 = s2 = j = ans = 0
        n = len(nums)
        while j < n:
            s1 += nums[j]
            s2 += nums[j]
            while i1 <= j and s1 > goal:
                s1 -= nums[i1]
                i1 += 1
            while i2 <= j and s2 >= goal:
                s2 -= nums[i2]
                i2 += 1
            ans += i2 - i1
            j += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
