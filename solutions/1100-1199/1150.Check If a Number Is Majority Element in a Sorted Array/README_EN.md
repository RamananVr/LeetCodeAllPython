---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1150.Check%20If%20a%20Number%20Is%20Majority%20Element%20in%20a%20Sorted%20Array/README_EN.md
rating: 1249
source: Biweekly Contest 6 Q1
tags:
    - Array
    - Binary Search
---

<!-- problem:start -->

# [1150. Check If a Number Is Majority Element in a Sorted Array 🔒](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> sorted in non-decreasing order and an integer <code>target</code>, return <code>true</code> <em>if</em> <code>target</code> <em>is a <strong>majority</strong> element, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>majority</strong> element in an array <code>nums</code> is an element that appears more than <code>nums.length / 2</code> times in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,4,5,5,5,5,5,6,6], target = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 &gt; 9/2 is true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,100,101,101], target = 101
<strong>Output:</strong> false
<strong>Explanation:</strong> The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 &gt; 4/2 is false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is sorted in non-decreasing order.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search

We notice that the elements in the array $nums$ are non-decreasing, that is, the elements in the array $nums$ are monotonically increasing. Therefore, we can use the method of binary search to find the index $left$ of the first element in the array $nums$ that is greater than or equal to $target$, and the index $right$ of the first element in the array $nums$ that is greater than $target$. If $right - left > \frac{n}{2}$, it means that the number of occurrences of the element $target$ in the array $nums$ exceeds half of the length of the array, so return $true$, otherwise return $false$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return right - left > len(nums) // 2
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Binary Search (Optimized)

In Solution 1, we used binary search twice to find the index $left$ of the first element in the array $nums$ that is greater than or equal to $target$, and the index $right$ of the first element in the array $nums$ that is greater than $target$. However, we can use binary search once to find the index $left$ of the first element in the array $nums$ that is greater than or equal to $target$, and then judge whether $nums[left + \frac{n}{2}]$ is equal to $target$. If they are equal, it means that the number of occurrences of the element $target$ in the array $nums$ exceeds half of the length of the array, so return $true$, otherwise return $false$.

The time complexity is $O(\log n)$, and the space complexity is $O(1)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = bisect_left(nums, target)
        right = left + len(nums) // 2
        return right < len(nums) and nums[right] == target
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
