---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1300.Sum%20of%20Mutated%20Array%20Closest%20to%20Target/README_EN.md
rating: 1606
source: Biweekly Contest 16 Q2
tags:
    - Array
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [1300. Sum of Mutated Array Closest to Target](https://leetcode.com/problems/sum-of-mutated-array-closest-to-target)

## Description

<!-- description:start -->

<p>Given an integer array <code>arr</code> and a target value <code>target</code>, return the integer <code>value</code> such that when we change all the integers larger than <code>value</code> in the given array to be equal to <code>value</code>, the sum of the array gets as close as possible (in absolute difference) to <code>target</code>.</p>

<p>In case of a tie, return the minimum such integer.</p>

<p>Notice that the answer is not neccesarilly a number from <code>arr</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,9,3], target = 10
<strong>Output:</strong> 3
<strong>Explanation:</strong> When using 3 arr converts to [3, 3, 3] which sums 9 and that&#39;s the optimal answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,3,5], target = 10
<strong>Output:</strong> 5
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [60864,25176,27249,21296,20204], target = 56803
<strong>Output:</strong> 11361
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i], target &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Prefix Sum + Binary Search + Enumeration

We notice that the problem requires changing all values greater than `value` to `value` and then summing them up. Therefore, we can consider sorting the array `arr` first, and then calculating the prefix sum array $s$, where $s[i]$ represents the sum of the first $i$ elements of the array.

Next, we can enumerate all `value` values from smallest to largest. For each `value`, we can use binary search to find the index $i$ of the first element in the array that is greater than `value`. At this point, the number of elements in the array greater than `value` is $n - i$, so the number of elements in the array less than or equal to `value` is $i$. The sum of the elements in the array less than or equal to `value` is $s[i]$, and the sum of the elements in the array greater than `value` is $(n - i) \times value$. Therefore, the sum of all elements in the array is $s[i] + (n - i) \times \textit{value}$. If the absolute difference between $s[i] + (n - i) \times \textit{value}$ and `target` is less than the current minimum difference `diff`, update `diff` and `ans`.

After enumerating all `value` values, we can get the final answer `ans`.

Time complexity $O(n \times \log n)$, space complexity $O(n)$. Where $n$ is the length of the array `arr`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        s = list(accumulate(arr, initial=0))
        ans, diff = 0, inf
        for value in range(max(arr) + 1):
            i = bisect_right(arr, value)
            d = abs(s[i] + (len(arr) - i) * value - target)
            if diff > d:
                diff = d
                ans = value
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
