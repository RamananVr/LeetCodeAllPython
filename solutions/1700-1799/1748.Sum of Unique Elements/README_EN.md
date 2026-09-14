---
comments: true
difficulty: Easy
rating: 1228
source: Biweekly Contest 45 Q1
tags:
    - Array
    - Hash Table
    - Counting
---

<!-- problem:start -->

# [1748. Sum of Unique Elements](https://leetcode.com/problems/sum-of-unique-elements)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>. The unique elements of an array are the elements that appear <strong>exactly once</strong> in the array.</p>

<p>Return <em>the <strong>sum</strong> of all the unique elements of </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The unique elements are [1,3], and the sum is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no unique elements, and the sum is 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 15
<strong>Explanation:</strong> The unique elements are [1,2,3,4,5], and the sum is 15.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Sum values that occur exactly once. Both the length and the values are at most $100$, so count frequencies and add keys whose count is $1$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return sum(x for x, v in cnt.items() if v == 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- thinking:start -->

> **Thinking**
>
> Solution 1 counts fully then sums. With a tiny domain we can do it in one pass: add on the first sighting, subtract on the second, and ignore later ones.

<!-- thinking:end -->

<!-- solution:end -->

<!-- problem:end -->
