---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3880.Minimum%20Absolute%20Difference%20Between%20Two%20Values/README_EN.md
rating: 1257
source: Biweekly Contest 179 Q1
tags:
    - Array
    - Enumeration
---

<!-- problem:start -->

# [3880. Minimum Absolute Difference Between Two Values](https://leetcode.com/problems/minimum-absolute-difference-between-two-values)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> consisting only of 0, 1, and 2.</p>

<p>A pair of indices <code>(i, j)</code> is called <strong>valid</strong> if <code>nums[i] == 1</code> and <code>nums[j] == 2</code>.</p>

<p>Return the <strong>minimum</strong> absolute difference between <code>i</code> and <code>j</code> among all valid pairs. If no valid pair exists, return -1.</p>

<p>The absolute difference between indices <code>i</code> and <code>j</code> is defined as <code>abs(i - j)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,0,2,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The valid pairs are:</p>

<ul>
	<li>(0, 3) which has absolute difference of <code>abs(0 - 3) = 3</code>.</li>
	<li>(5, 3) which has absolute difference of <code>abs(5 - 3) = 2</code>.</li>
</ul>

<p>Thus, the answer is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no valid pairs in the array, thus the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Single Pass

We use an array $\textit{last}$ of length $3$ to record the last occurrence index of digits $0$, $1$, and $2$. Initially, $\textit{last} = [-(n+1), -(n+1), -(n+1)]$. We iterate through the array $\textit{nums}$. For the current number $x$, if $x$ is not equal to $0$, we update the answer $\textit{ans} = \min(\textit{ans}, i - \textit{last}[3 - x])$, where $i$ is the index of the current number $x$. Then we update $\textit{last}[x] = i$.

After the iteration, if $\textit{ans}$ is greater than the length of the array $\textit{nums}$, it means no valid index pair exists, so we return -1; otherwise, we return $\textit{ans}$.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        ans = n + 1
        last = [-inf] * 3
        for i, x in enumerate(nums):
            if x:
                ans = min(ans, i - last[3 - x])
                last[x] = i
        return -1 if ans > n else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
