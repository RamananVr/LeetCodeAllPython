---
comments: true
difficulty: Medium
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [3717. Minimum Operations to Make the Array Beautiful 🔒](https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>An array is called <strong>beautiful</strong> if for every index <code>i &gt; 0</code>, the value at <code>nums[i]</code> is <strong>divisible</strong> by <code>nums[i - 1]</code>.</p>

<p>In one operation, you may <strong>increment</strong> any element <code>nums[i]</code> (with <code>i &gt; 0</code>) by <code>1</code>.</p>

<p>Return the <strong>minimum number of operations</strong> required to make the array beautiful.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,7,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Applying the operation twice on <code>nums[1]</code> makes the array beautiful: <code>[3,9,9]</code></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The given array is already beautiful.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The array has only one element, so it&#39;s already beautiful.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50​​​</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Later entries may only increase and must become multiples of the previous one. With $n\le 100$ and $nums[i]\le 50$, the raised values stay in a small range. DP stores the value written at the previous index and its cost; from each such value we try multiples of it that are at least $x$ and within a constant cap.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = {nums[0]: 0}
        for x in nums[1:]:
            g = {}
            for pre, s in f.items():
                cur = (x + pre - 1) // pre * pre
                while cur <= 100:
                    if cur not in g or g[cur] > s + cur - x:
                        g[cur] = s + cur - x
                    cur += pre
            f = g
        return min(f.values())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
