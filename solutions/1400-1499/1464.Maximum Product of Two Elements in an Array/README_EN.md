---
comments: true
difficulty: Easy
rating: 1121
source: Weekly Contest 191 Q1
tags:
    - Array
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1464. Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array)

## Description

<!-- description:start -->

<p>You are given an array of integers <code>nums</code>.</p>

<p>Choose two <strong>different</strong> indices <code>i</code> and <code>j</code> of that array.</p>

<p>Return the <strong>maximum</strong> value of <code>(nums[i] - 1) * (nums[j] - 1)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5,2]
<strong>Output:</strong> 12 
<strong>Explanation:</strong> If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,4,5]
<strong>Output:</strong> 16
<strong>Explanation:</strong> Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,7]
<strong>Output:</strong> 12
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> $n\le 500$. Enumerate every unordered pair and keep the maximum of $(a-1)(b-1)$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        for i, a in enumerate(nums):
            for b in nums[i + 1 :]:
                ans = max(ans, (a - 1) * (b - 1))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Method 1 is quadratic. The product grows with the two values, so sort and take the last two.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3

<!-- thinking:start -->

> **Thinking**
>
> Method 2 still sorts. One pass that keeps the largest and second-largest values is enough.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = 0
        for v in nums:
            if v > a:
                a, b = v, a
            elif v > b:
                b = v
        return (a - 1) * (b - 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
