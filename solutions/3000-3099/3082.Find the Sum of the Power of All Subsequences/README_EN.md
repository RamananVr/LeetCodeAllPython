---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3000-3099/3082.Find%20the%20Sum%20of%20the%20Power%20of%20All%20Subsequences/README_EN.md
rating: 2241
source: Biweekly Contest 126 Q4
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [3082. Find the Sum of the Power of All Subsequences](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> and a <strong>positive</strong> integer <code>k</code>.</p>

<p>The <strong>power</strong> of an array of integers is defined as the number of <span data-keyword="subsequence-array">subsequences</span> with their sum <strong>equal</strong> to <code>k</code>.</p>

<p>Return <em>the <strong>sum</strong> of <strong>power</strong> of all subsequences of</em> <code>nums</code><em>.</em></p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [1,2,3], k = 3 </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 6 </span></p>

<p><strong>Explanation:</strong></p>

<p>There are <code>5</code> subsequences of nums with non-zero power:</p>

<ul>
	<li>The subsequence <code>[<u><strong>1</strong></u>,<u><strong>2</strong></u>,<u><strong>3</strong></u>]</code> has <code>2</code> subsequences with <code>sum == 3</code>: <code>[1,2,<u>3</u>]</code> and <code>[<u>1</u>,<u>2</u>,3]</code>.</li>
	<li>The subsequence <code>[<u><strong>1</strong></u>,2,<u><strong>3</strong></u>]</code> has <code>1</code> subsequence with <code>sum == 3</code>: <code>[1,2,<u>3</u>]</code>.</li>
	<li>The subsequence <code>[1,<u><strong>2</strong></u>,<u><strong>3</strong></u>]</code> has <code>1</code> subsequence with <code>sum == 3</code>: <code>[1,2,<u>3</u>]</code>.</li>
	<li>The subsequence <code>[<u><strong>1</strong></u>,<u><strong>2</strong></u>,3]</code> has <code>1</code> subsequence with <code>sum == 3</code>: <code>[<u>1</u>,<u>2</u>,3]</code>.</li>
	<li>The subsequence <code>[1,2,<u><strong>3</strong></u>]</code> has <code>1</code> subsequence with <code>sum == 3</code>: <code>[1,2,<u>3</u>]</code>.</li>
</ul>

<p>Hence the answer is <code>2 + 1 + 1 + 1 + 1 = 6</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [2,3,3], k = 5 </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 4 </span></p>

<p><strong>Explanation:</strong></p>

<p>There are <code>3</code> subsequences of nums with non-zero power:</p>

<ul>
	<li>The subsequence <code>[<u><strong>2</strong></u>,<u><strong>3</strong></u>,<u><strong>3</strong></u>]</code> has 2 subsequences with <code>sum == 5</code>: <code>[<u>2</u>,3,<u>3</u>]</code> and <code>[<u>2</u>,<u>3</u>,3]</code>.</li>
	<li>The subsequence <code>[<u><strong>2</strong></u>,3,<u><strong>3</strong></u>]</code> has 1 subsequence with <code>sum == 5</code>: <code>[<u>2</u>,3,<u>3</u>]</code>.</li>
	<li>The subsequence <code>[<u><strong>2</strong></u>,<u><strong>3</strong></u>,3]</code> has 1 subsequence with <code>sum == 5</code>: <code>[<u>2</u>,<u>3</u>,3]</code>.</li>
</ul>

<p>Hence the answer is <code>2 + 1 + 1 = 4</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> nums = [1,2,3], k = 7 </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 0 </span></p>

<p><strong>Explanation:&nbsp;</strong>There exists no subsequence with sum <code>7</code>. Hence all subsequences of nums have <code>power = 0</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

The problem requires us to find all subsequences $\textit{S}$ in the given array $\textit{nums}$, and then calculate the number of ways for each subsequence $\textit{T}$ such that the sum of $\textit{T}$ equals $\textit{k}$.

We define $f[i][j]$ to represent the number of ways to form subsequences with the first $i$ numbers such that the sum of each subsequence equals $j$. Initially, $f[0][0] = 1$, and all other positions are $0$.

For the $i$-th number $x$, there are three cases:

1. Not in the subsequence $\textit{S}$, in which case $f[i][j] = f[i-1][j]$;
2. In the subsequence $\textit{S}$, but not in the subsequence $\textit{T}$, in which case $f[i][j] = f[i-1][j]$;
3. In the subsequence $\textit{S}$, and in the subsequence $\textit{T}$, in which case $f[i][j] = f[i-1][j-x]$.

In summary, the state transition equation is:

$$
f[i][j] = f[i-1][j] \times 2 + f[i-1][j-x]
$$

The final answer is $f[n][k]$.

The time complexity is $O(n \times k)$, and the space complexity is $O(n \times k)$. Here, $n$ is the length of the array $\textit{nums}$, and $k$ is the given positive integer.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        f = [[0] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums, 1):
            for j in range(k + 1):
                f[i][j] = f[i - 1][j] * 2 % mod
                if j >= x:
                    f[i][j] = (f[i][j] + f[i - 1][j - x]) % mod
        return f[n][k]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming (Optimization)

In the state transition equation from Solution 1, the value of $f[i][j]$ only depends on $f[i-1][j]$ and $f[i-1][j-x]$. Therefore, we can optimize the first dimension of the space, reducing the space complexity to $O(k)$.

Time complexity is $O(n \times k)$, and space complexity is $O(k)$. Here, $n$ is the length of the array $\textit{nums}$, and $k$ is the given positive integer.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        f = [1] + [0] * k
        for x in nums:
            for j in range(k, -1, -1):
                f[j] = (f[j] * 2 + (0 if j < x else f[j - x])) % mod
        return f[k]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
