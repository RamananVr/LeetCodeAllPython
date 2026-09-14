---
comments: true
difficulty: Medium
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv)

## Description

<!-- description:start -->

<p>Given an array of <strong>distinct</strong> integers <code>nums</code> and a target integer <code>target</code>, return <em>the number of possible combinations that add up to</em>&nbsp;<code>target</code>.</p>

<p>The test cases are generated so that the answer can fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3], target = 4
<strong>Output:</strong> 7
<strong>Explanation:</strong>
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9], target = 3
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li>All the elements of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

<!-- thinking:start -->

> **Thinking**
>
> Count ordered ways to sum to $target$. An outer loop over items (combinations) misses permutations. Enumerate the sum first, then the last addend.
>
> $f[i]$ is the number of permutations summing to $i$, $f[0]=1$. For each $i$ and each $x\le i$, add $f[i-x]$. Same shape as 322, counting instead of minimizing coins.

<!-- thinking:end -->

We define $f[i]$ as the number of combinations that sum up to $i$. Initially, $f[0] = 1$, and the rest $f[i] = 0$. The final answer is $f[target]$.

For $f[i]$, we can enumerate each element $x$ in the array. If $i \ge x$, then $f[i] = f[i] + f[i - x]$.

Finally, return $f[target]$.

The time complexity is $O(n \times target)$, and the space complexity is $O(target)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        f = [1] + [0] * target
        for i in range(1, target + 1):
            for x in nums:
                if i >= x:
                    f[i] += f[i - x]
        return f[target]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
