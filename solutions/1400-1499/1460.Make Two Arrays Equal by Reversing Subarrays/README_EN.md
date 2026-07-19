---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1460.Make%20Two%20Arrays%20Equal%20by%20Reversing%20Subarrays/README_EN.md
rating: 1151
source: Biweekly Contest 27 Q1
tags:
    - Array
    - Hash Table
    - Sorting
---

<!-- problem:start -->

# [1460. Make Two Arrays Equal by Reversing Subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays)

## Description

<!-- description:start -->

<p>You are given two integer arrays of equal length <code>target</code> and <code>arr</code>. In one step, you can select any <strong>non-empty subarray</strong> of <code>arr</code> and reverse it. You are allowed to make any number of steps.</p>

<p>Return <code>true</code> <em>if you can make </em><code>arr</code><em> equal to </em><code>target</code><em>&nbsp;or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = [1,2,3,4], arr = [2,4,1,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = [7], arr = [7]
<strong>Output:</strong> true
<strong>Explanation:</strong> arr is equal to target without any reverses.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = [3,7,9], arr = [3,7,11]
<strong>Output:</strong> false
<strong>Explanation:</strong> arr does not have value 9 and it can never be converted to target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>target.length == arr.length</code></li>
	<li><code>1 &lt;= target.length &lt;= 1000</code></li>
	<li><code>1 &lt;= target[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting

If two arrays are equal after sorting, then they can be made equal by reversing sub-arrays.

Therefore, we only need to sort the two arrays and then check if the sorted arrays are equal.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $arr$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Counting

We note that the range of the array elements given in the problem is $1 \sim 1000$. Therefore, we can use two arrays `cnt1` and `cnt2` of length $1001$ to record the number of times each element appears in the arrays `target` and `arr` respectively. Finally, we just need to check if the two arrays are equal.

We can also use only one array `cnt`. We traverse the arrays `target` and `arr`. For `target[i]`, we increment `cnt[target[i]]`, and for `arr[i]`, we decrement `cnt[arr[i]]`. In the end, we check if all elements in the array `cnt` are $0$.

The time complexity is $O(n + M)$, and the space complexity is $O(M)$. Here, $n$ is the length of the array `arr`, and $M$ is the range of the array elements. In this problem, $M = 1001$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
