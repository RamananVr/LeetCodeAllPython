---
comments: true
difficulty: Easy
rating: 1152
source: Weekly Contest 269 Q1
tags:
    - Array
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [2089. Find Target Indices After Sorting Array](https://leetcode.com/problems/find-target-indices-after-sorting-array)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and a target element <code>target</code>.</p>

<p>A <strong>target index</strong> is an index <code>i</code> such that <code>nums[i] == target</code>.</p>

<p>Return <em>a list of the target indices of</em> <code>nums</code> after<em> sorting </em><code>nums</code><em> in <strong>non-decreasing</strong> order</em>. If there are no target indices, return <em>an <strong>empty</strong> list</em>. The returned list must be sorted in <strong>increasing</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 2
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> After sorting, nums is [1,<u><strong>2</strong></u>,<u><strong>2</strong></u>,3,5].
The indices where nums[i] == 2 are 1 and 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 3
<strong>Output:</strong> [3]
<strong>Explanation:</strong> After sorting, nums is [1,2,2,<u><strong>3</strong></u>,5].
The index where nums[i] == 3 is 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,5,2,3], target = 5
<strong>Output:</strong> [4]
<strong>Explanation:</strong> After sorting, nums is [1,2,2,3,<u><strong>5</strong></u>].
The index where nums[i] == 5 is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> With $n \le 100$, sort and collect indices equal to $\textit{target}$; they already appear in increasing order.
>
> A linear count of smaller/equal values could build the same range; the code simply sorts.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i, v in enumerate(nums) if v == target]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Counting

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 sorts the whole array to recover indices, so the time stays $O(n \log n)$. Those indices depend only on where $\textit{target}$ would sit after sorting, not on the order among the other values.
>
> The number of values strictly less than $\textit{target}$ is the start of that contiguous range, and the number of values equal to $\textit{target}$ is its length. Both counts come from one pass over the original array, which removes the comparison sort.

<!-- thinking:end -->

After sorting into non-decreasing order, every value equal to $\textit{target}$ occupies one contiguous index range. The start of the range equals the number of elements strictly less than $\textit{target}$, and the length equals the number of elements equal to $\textit{target}$.

Scan $\textit{nums}$ once and store the two counts in $\textit{less}$ and $\textit{equal}$. The answer is every integer in $[\textit{less}, \textit{less} + \textit{equal})$. The range is empty when $\textit{equal} = 0$.

The time complexity is $O(n)$, and the space complexity is $O(1)$, where $n$ is the length of $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = equal = 0
        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                equal += 1
        return list(range(less, less + equal))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
