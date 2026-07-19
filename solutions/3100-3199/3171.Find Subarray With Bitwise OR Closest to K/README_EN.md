---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3171.Find%20Subarray%20With%20Bitwise%20OR%20Closest%20to%20K/README_EN.md
rating: 2162
source: Weekly Contest 400 Q4
tags:
    - Bit Manipulation
    - Segment Tree
    - Array
    - Binary Search
---

<!-- problem:start -->

# [3171. Find Subarray With Bitwise OR Closest to K](https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k)

## Description

<!-- description:start -->

<p>You are given an array <code>nums</code> and an integer <code>k</code>. You need to find a <span data-keyword="subarray-nonempty">subarray</span> of <code>nums</code> such that the <strong>absolute difference</strong> between <code>k</code> and the bitwise <code>OR</code> of the subarray elements is as<strong> small</strong> as possible. In other words, select a subarray <code>nums[l..r]</code> such that <code>|k - (nums[l] OR nums[l + 1] ... OR nums[r])|</code> is minimum.</p>

<p>Return the <strong>minimum</strong> possible value of the absolute difference.</p>

<p>A <strong>subarray</strong> is a contiguous <b>non-empty</b> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4,5], k = 3</span></p>

<p><strong>Output:</strong> 0</p>

<p><strong>Explanation:</strong></p>

<p>The subarray <code>nums[0..1]</code> has <code>OR</code> value 3, which gives the minimum absolute difference <code>|3 - 3| = 0</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,1,3], k = 2</span></p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>The subarray <code>nums[1..1]</code> has <code>OR</code> value 3, which gives the minimum absolute difference <code>|3 - 2| = 1</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1], k = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>There is a single subarray with <code>OR</code> value 1, which gives the minimum absolute difference <code>|10 - 1| = 9</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Pointers + Bitwise Operations

According to the problem description, we need to calculate the result of the bitwise OR operation of elements from index $l$ to $r$ in the array $\textit{nums}$, that is, $\textit{nums}[l] \lor \textit{nums}[l + 1] \lor \cdots \lor \textit{nums}[r]$, where $\lor$ represents the bitwise OR operation.

If we fix the right endpoint $r$, then the range of the left endpoint $l$ is $[0, r]$. Each time we move the right endpoint $r$, the result of the bitwise OR operation will only increase. We use a variable $s$ to record the current result of the bitwise OR operation. If $s$ is greater than $k$, we move the left endpoint $l$ to the right until $s$ is less than or equal to $k$. During the process of moving the left endpoint $l$, we need to maintain an array $cnt$ to record the number of $0$s on each binary digit in the current interval. When $cnt[h] = 0$, it means that all elements in the current interval have a $0$ on the $h^{th}$ bit, and we can set the $h^{th}$ bit of $s$ to $0$.

The time complexity is $O(n \times \log M)$, and the space complexity is $O(\log M)$. Here, $n$ and $M$ respectively represent the length of the array $\textit{nums}$ and the maximum value in the array $\textit{nums}$.

Similar Problems:

- [3097. Shortest Subarray With OR at Least K II](https://github.com/doocs/leetcode/blob/main/solution/3000-3099/3097.Shortest%20Subarray%20With%20OR%20at%20Least%20K%20II/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        m = max(nums).bit_length()
        cnt = [0] * m
        s = i = 0
        ans = inf
        for j, x in enumerate(nums):
            s |= x
            ans = min(ans, abs(s - k))
            for h in range(m):
                if x >> h & 1:
                    cnt[h] += 1
            while i < j and s > k:
                y = nums[i]
                for h in range(m):
                    if y >> h & 1:
                        cnt[h] -= 1
                        if cnt[h] == 0:
                            s ^= 1 << h
                i += 1
                ans = min(ans, abs(s - k))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Hash Table + Enumeration

According to the problem description, we need to calculate the result of the bitwise OR operation of elements from index $l$ to $r$ in the array $nums$, that is, $nums[l] \lor nums[l + 1] \lor \cdots \lor nums[r]$. Here, $\lor$ represents the bitwise OR operation.

If we fix the right endpoint $r$, then the range of the left endpoint $l$ is $[0, r]$. Since the sum of bitwise OR increases monotonically as $l$ decreases, and the value of $\textit{nums}[i]$ does not exceed $10^9$, the interval $[0, r]$ can have at most $30$ different values. Therefore, we can use a set to maintain all the values of $nums[l] \lor nums[l + 1] \lor \cdots \lor nums[r]$. When we traverse from $r$ to $r+1$, the values with $r+1$ as the right endpoint are the values obtained by performing the bitwise OR operation of each value in the set with $nums[r + 1]$, plus $nums[r + 1]$ itself. Therefore, we only need to enumerate each value in the set and perform the bitwise OR operation with $nums[r]$, to get all the values for $r$ as the right endpoint. Then, we take the absolute difference of each value with $k$, and the minimum of these differences is the answer.

The time complexity is $O(n \times \log M)$, and the space complexity is $O(\log M)$. Here, $n$ and $M$ respectively represent the length of the array $nums$ and the maximum value in the array $nums$.

Similar Problems:

- [1521. Find a Value of a Mysterious Function Closest to Target](https://github.com/doocs/leetcode/blob/main/solution/1500-1599/1521.Find%20a%20Value%20of%20a%20Mysterious%20Function%20Closest%20to%20Target/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        s = set()
        for x in nums:
            s = {x | y for y in s} | {x}
            ans = min(ans, min(abs(y - k) for y in s))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
