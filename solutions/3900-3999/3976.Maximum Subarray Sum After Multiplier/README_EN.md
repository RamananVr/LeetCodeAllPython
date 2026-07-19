---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3900-3999/3976.Maximum%20Subarray%20Sum%20After%20Multiplier/README_EN.md
rating: 1981
source: Weekly Contest 508 Q3
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [3976. Maximum Subarray Sum After Multiplier](https://leetcode.com/problems/maximum-subarray-sum-after-multiplier)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and a positive integer <code>k</code>.</p>

<p>You must choose <strong>exactly</strong> one <span data-keyword="subarray-nonempty">subarray</span> of <code>nums</code> and perform <strong>exactly</strong> one of the following operations:</p>

<ol>
	<li>Multiply each number in the chosen subarray by <code>k</code>.</li>
	<li>Divide each number in the chosen subarray by <code>k</code>.
	<ul>
		<li>When dividing a positive number by <code>k</code>, use the <strong>floor</strong> value of the division result.</li>
		<li>When dividing a negative number by <code>k</code>, use the <strong>ceiling</strong> value of the division result.</li>
	</ul>
	</li>
</ol>

<p>Return the <strong>maximum</strong> possible sum of a <strong>non-empty</strong> subarray in the resulting array.</p>

<p>Note that the subarray chosen for the operation and the subarray chosen for the sum may be <strong>different</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,-2,3,4,-5], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Multiply each number in the subarray <code>[3, 4]</code> by 2.</li>
	<li>This results in <code>nums = [1, -2, 6, 8, -5]</code>.</li>
	<li>The subarray with the largest sum is <code>[6, 8]</code>, so the output is <code>6 + 8 = 14</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-5,-4,-3], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Divide each number in the subarray <code>[-3]</code> by 2.</li>
	<li>This results in <code>nums = [-5, -4, -1]</code>.</li>
	<li>The subarray with the largest sum is <code>[-1]</code>, so the output is -1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i][j]$ as the maximum subarray sum ending at $nums[i]$ with current state $j$. There are $4$ states for $j$:

- State $0$: the current subarray has not undergone any operation yet;
- State $1$: the current subarray is being multiplied by $k$;
- State $2$: the current subarray is being divided by $k$;
- State $3$: the operation on the current subarray has been completed.

Initially, $f[0][0] = 0$, and all other $f[i][j] = -\infty$.

Next, we consider the state transitions. For the $i$-th number $nums[i]$, we can choose not to perform any operation, multiply by $k$, divide by $k$, or continue after the operation has been completed:

- If we perform no operation, then $f[i][0] = \max(f[i-1][0], 0) + nums[i]$;
- If we multiply by $k$, then $f[i][1] = \max(f[i-1][0], f[i-1][1], 0) + nums[i] \times k$;
- If we divide by $k$, then $f[i][2] = \max(f[i-1][0], f[i-1][2], 0) + \lfloor \frac{nums[i]}{k} \rfloor$;
- If the operation has been completed, then $f[i][3] = \max(f[i-1][1], f[i-1][2], f[i-1][3]) + nums[i]$.

We take the maximum among all states as the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [[-inf] * 4 for _ in range(n + 1)]
        f[0][0] = 0
        ans = -inf
        for i, x in enumerate(nums, 1):
            f[i][0] = max(f[i - 1][0], 0) + x
            f[i][1] = max(f[i - 1][0], f[i - 1][1], 0) + x * k
            f[i][2] = max(f[i - 1][0], f[i - 1][2], 0) + int(x / k)
            f[i][3] = max(f[i - 1][1], f[i - 1][2], f[i - 1][3]) + x
            ans = max(ans, max(f[i]))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
