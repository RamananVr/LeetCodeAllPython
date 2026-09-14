---
comments: true
difficulty: Medium
rating: 1658
source: Biweekly Contest 116 Q3
tags:
    - Array
    - Dynamic Programming
    - Knapsack
    - 0-1 Knapsack
---

<!-- problem:start -->

# [2915. Length of the Longest Subsequence That Sums to Target](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code>, and an integer <code>target</code>.</p>

<p>Return <em>the <strong>length of the longest subsequence</strong> of</em> <code>nums</code> <em>that sums up to</em> <code>target</code>. <em>If no such subsequence exists, return</em> <code>-1</code>.</p>

<p>A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5], target = 9
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 subsequences with a sum equal to 9: [4,5], [1,3,5], and [2,3,4]. The longest subsequences are [1,3,5], and [2,3,4]. Hence, the answer is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,1,3,2,1,5], target = 7
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 5 subsequences with a sum equal to 7: [4,3], [4,1,2], [4,2,1], [1,1,5], and [1,3,2,1]. The longest subsequence is [1,3,2,1]. Hence, the answer is 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,5,4,5], target = 3
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be shown that nums has no subsequence that sums up to 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> The longest subsequence whose sum is exactly $target$ is a 0-1 knapsack ($n,target \le 1000$). Let $f[i][j]$ be the best length using the first $i$ numbers to make $j$, with unreachable states at $-\infty$.
>
> The recurrence takes the better of skipping $x$ and taking it. If $f[n][target]$ is non-positive, no solution exists.

<!-- thinking:end -->

We define $f[i][j]$ as the length of the longest subsequence that selects several numbers from the first $i$ numbers and the sum of these numbers is exactly $j$. Initially, $f[0][0]=0$, and all other positions are $-\infty$.

For $f[i][j]$, we consider the $i$th number $x$. If we do not select $x$, then $f[i][j]=f[i-1][j]$. If we select $x$, then $f[i][j]=f[i-1][j-x]+1$, where $j\ge x$. Therefore, we have the state transition equation:

$$
f[i][j]=\max\{f[i-1][j],f[i-1][j-x]+1\}
$$

The final answer is $f[n][target]$. If $f[n][target]\le0$, there is no subsequence with a sum of $target$, return $-1$.

The time complexity is $O(n\times target)$, and the space complexity is $O(n\times target)$. Here, $n$ is the length of the array, and $target$ is the target value.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [[-inf] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(nums, 1):
            for j in range(target + 1):
                f[i][j] = f[i - 1][j]
                if j >= x:
                    f[i][j] = max(f[i][j], f[i - 1][j - x] + 1)
        return -1 if f[n][target] <= 0 else f[n][target]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Optimized Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Method 1’s $f[i][j]$ depends only on the previous row, so the first index drops. Each number is used at most once, therefore the inner loop walks capacities downward. Space becomes $O(target)$ with the same answer.

<!-- thinking:end -->

$f[i][j]$ depends only on the previous row $f[i-1][\cdot]$, so the first dimension can be dropped. Each number is used at most once, so $j$ is updated from large to small. The space complexity becomes $O(target)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        f = [0] + [-inf] * target
        for x in nums:
            for j in range(target, x - 1, -1):
                f[j] = max(f[j], f[j - x] + 1)
        return -1 if f[-1] <= 0 else f[-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
