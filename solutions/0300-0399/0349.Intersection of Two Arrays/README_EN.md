---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0300-0399/0349.Intersection%20of%20Two%20Arrays/README_EN.md
tags:
    - Array
    - Hash Table
    - Two Pointers
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays)

## Description

<!-- description:start -->

<p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their <span data-keyword="array-intersection">intersection</span></em>. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [9,4]
<strong>Explanation:</strong> [4,9] is also accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table or Array

First, we use a hash table or an array $s$ of length $1001$ to record the elements that appear in the array $nums1$. Then, we iterate through each element in the array $nums2$. If an element $x$ is in $s$, we add $x$ to the answer and remove $x$ from $s$.

After the iteration is finished, we return the answer array.

The time complexity is $O(n+m)$, and the space complexity is $O(n)$. Here, $n$ and $m$ are the lengths of the arrays $nums1$ and $nums2$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
