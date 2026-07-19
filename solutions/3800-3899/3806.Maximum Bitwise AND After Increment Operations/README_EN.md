---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3806.Maximum%20Bitwise%20AND%20After%20Increment%20Operations/README_EN.md
rating: 2259
source: Weekly Contest 484 Q4
tags:
    - Greedy
    - Bit Manipulation
    - Array
    - Sorting
---

<!-- problem:start -->

# [3806. Maximum Bitwise AND After Increment Operations](https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and two integers <code>k</code> and <code>m</code>.</p>

<p>You may perform <strong>at most</strong> <code>k</code> operations. In one operation, you may choose any index <code>i</code> and <strong>increase</strong> <code>nums[i]</code> by 1.</p>

<p>Return an integer denoting the <strong>maximum</strong> possible <strong>bitwise AND</strong> of any <strong><span data-keyword="subset">subset</span></strong> of size <code>m</code> after performing up to <code>k</code> operations optimally.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,2], k = 8, m = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>We need a subset of size <code>m = 2</code>. Choose indices <code>[0, 2]</code>.</li>
	<li>Increase <code>nums[0] = 3</code> to 6 using 3 operations, and increase <code>nums[2] = 2</code> to 6 using 4 operations.</li>
	<li>The total number of operations used is 7, which is not greater than <code>k = 8</code>.</li>
	<li>The two chosen values become <code>[6, 6]</code>, and their bitwise AND is <code>6</code>, which is the maximum possible.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,8,4], k = 7, m = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>We need a subset of size <code>m = 3</code>. Choose indices <code>[0, 1, 3]</code>.</li>
	<li>Increase <code>nums[0] = 1</code> to 4 using 3 operations, increase <code>nums[1] = 2</code> to 4 using 2 operations, and keep <code>nums[3] = 4</code>.</li>
	<li>The total number of operations used is 5, which is not greater than <code>k = 7</code>.</li>
	<li>The three chosen values become <code>[4, 4, 4]</code>, and their bitwise AND is 4, which is the maximum possible.​​​​​​​</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1], k = 3, m = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>We need a subset of size <code>m = 2</code>. Choose indices <code>[0, 1]</code>.</li>
	<li>Increase both values from 1 to 2 using 1 operation each.</li>
	<li>The total number of operations used is 2, which is not greater than <code>k = 3</code>.</li>
	<li>The two chosen values become <code>[2, 2]</code>, and their bitwise AND is 2, which is the maximum possible.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= m &lt;= n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy Bit Construction + Bit Manipulation

We enumerate each bit from the highest bit, attempting to include that bit in the final bitwise AND result. For the currently attempted bitwise AND result $\textit{target}$, we calculate the minimum number of operations required to increase each element in the array to at least $\textit{target}$.

Specifically, we find the position $j - 1$ where $\textit{target}$ has the first bit set to $1$ from high to low, while the current element has the corresponding bit set to $0$. Then we only need to increase the current element to the value of $\textit{target}$ in the lower $j$ bits. The required number of operations is $(\textit{target} \& 2^{j} - 1) - (\textit{nums}[i] \& 2^{j} - 1)$. We store the required number of operations for all elements in the array $\textit{cost}$, sort it, and take the sum of the first $m$ elements. If it does not exceed $k$, it means we can include this bit in the final bitwise AND result.

The time complexity is $O(n \times \log n \times \log M)$ and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$ and $M$ is the maximum value in the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        mx = (max(nums) + k).bit_length()
        ans = 0
        cost = [0] * len(nums)
        for bit in range(mx - 1, -1, -1):
            target = ans | (1 << bit)
            for i, x in enumerate(nums):
                j = (target & ~x).bit_length()
                mask = (1 << j) - 1
                cost[i] = (target & mask) - (x & mask)
            cost.sort()
            if sum(cost[:m]) <= k:
                ans = target
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
