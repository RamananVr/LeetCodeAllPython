---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3900-3999/3942.Minimum%20Operations%20to%20Sort%20a%20Permutation/README_EN.md
rating: 1854
source: Weekly Contest 503 Q3
tags:
    - Array
---

<!-- problem:start -->

# [3942. Minimum Operations to Sort a Permutation](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code>, where <code>nums</code> is a <span data-keyword="permutation-array">permutation</span> of the integers from 0 to <code>n - 1</code>.</p>

<p>You may perform <strong>only</strong> the following operations:</p>

<ul>
	<li><strong>Reverse</strong> the entire array.</li>
	<li><strong>Rotate Left by One</strong>: Move the first element to the end of the array, and rest elements to left by one position.</li>
</ul>

<p>Return an integer denoting the <strong>minimum</strong> number of operations required to sort the array in <strong>increasing</strong> order. If it is <strong>not possible</strong> to sort the array using only the given operations, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Rotate Left by one: <code>[2, 1, 0]</code></li>
	<li>Reverse the array: <code>[0, 1, 2]</code></li>
</ul>

<p>The array becomes sorted in 2 operations, which is minimal</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Reverse the array: <code>[2, 0, 1]</code></li>
	<li>Rotate Left by one: <code>[0, 1, 2]</code></li>
</ul>

<p>The array becomes sorted in 2 operations, which is minimal.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,0,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>It is impossible to reach <code>[2, 0, 1, 3]</code>. Thus, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n - 1</code></li>
	<li><code>nums</code> is a permutation of integers from 0 to <code>n - 1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Case Analysis

We first find the position of `0` in the array, denoted as $\textit{zero}$.

Next, we check whether the sequence is increasing when traversing right from `0`, and whether it is increasing when traversing left from `0`.

If it is increasing to the right from `0`, we can sort the array in either of the following two ways:

- Rotate directly: left-rotate the array by $\textit{zero}$ positions.
- Reverse, rotate, then reverse back: reverse the array, left-rotate it by $n - \textit{zero}$ positions, then reverse it again.

If it is increasing to the left from `0`, we can sort the array in either of the following two ways:

- Rotate, then reverse: left-rotate the array by $\textit{zero} + 1$ positions to move `0` to the end, then reverse the array.
- Reverse, then rotate: reverse the array, then left-rotate it by $n - \textit{zero} - 1$ positions to move `0` to the beginning.

We compute the number of operations for all four methods above and return the minimum. If sorting is impossible, return `-1`.

The time complexity is $O(n)$, where $n$ is the length of $\textit{nums}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        zero = nums.index(0)

        def check(step: int) -> bool:
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n

                if nums[prev] > nums[curr]:
                    return False

            return True

        ans = inf

        if check(1):
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)

        if check(-1):
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)

        return -1 if ans == inf else ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
