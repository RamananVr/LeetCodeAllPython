---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0962.Maximum%20Width%20Ramp/README_EN.md
tags:
    - Stack
    - Array
    - Two Pointers
    - Monotonic Stack
---

<!-- problem:start -->

# [962. Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp)

## Description

<!-- description:start -->

<p>A <strong>ramp</strong> in an integer array <code>nums</code> is a pair <code>(i, j)</code> for which <code>i &lt; j</code> and <code>nums[i] &lt;= nums[j]</code>. The <strong>width</strong> of such a ramp is <code>j - i</code>.</p>

<p>Given an integer array <code>nums</code>, return <em>the maximum width of a <strong>ramp</strong> in </em><code>nums</code>. If there is no <strong>ramp</strong> in <code>nums</code>, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,0,8,2,1,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,8,1,0,1,9,4,0,4,1]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack

According to the problem, we can find that the subsequence formed by all possible $\textit{nums}[i]$ must be monotonically decreasing. Why is that? Let's prove it by contradiction.

Suppose there exist $i_1<i_2$ and $\textit{nums}[i_1]\leq\textit{nums}[i_2]$, then actually $\textit{nums}[i_2]$ cannot be a candidate value, because $\textit{nums}[i_1]$ is more to the left and would be a better value. Therefore, the subsequence formed by $\textit{nums}[i]$ must be monotonically decreasing, and $i$ must start from 0.

We use a monotonically decreasing stack $\textit{stk}$ (from bottom to top) to store all possible $\textit{nums}[i]$. Then we traverse $j$ starting from the right boundary. If we encounter $\textit{nums}[\textit{stk.top()}]\leq\textit{nums}[j]$, it means a ramp is formed at this point. We cyclically pop the top elements from the stack and update $\textit{ans}$.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ represents the length of $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = []
        for i, v in enumerate(nums):
            if not stk or nums[stk[-1]] > v:
                stk.append(i)
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            while stk and nums[stk[-1]] <= nums[i]:
                ans = max(ans, i - stk.pop())
            if not stk:
                break
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
