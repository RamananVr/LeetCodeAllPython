---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0400-0499/0485.Max%20Consecutive%20Ones/README_EN.md
tags:
    - Array
---

<!-- problem:start -->

# [485. Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones)

## Description

<!-- description:start -->

<p>Given a binary array <code>nums</code>, return <em>the maximum number of consecutive </em><code>1</code><em>&#39;s in the array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,0,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1,0,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Single Pass

We can iterate through the array, using a variable $\textit{cnt}$ to record the current number of consecutive 1s, and another variable $\textit{ans}$ to record the maximum number of consecutive 1s.

When we encounter a 1, we increment $\textit{cnt}$ by one, and then update $\textit{ans}$ to be the maximum of $\textit{cnt}$ and $\textit{ans}$ itself, i.e., $\textit{ans} = \max(\textit{ans}, \textit{cnt})$. Otherwise, we reset $\textit{cnt}$ to 0.

After the iteration ends, we return the value of $\textit{ans}$.

The time complexity is $O(n)$, where $n$ is the length of the array. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cnt = 0
        for x in nums:
            if x:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
