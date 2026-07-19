---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0907.Sum%20of%20Subarray%20Minimums/README_EN.md
tags:
    - Stack
    - Array
    - Dynamic Programming
    - Monotonic Stack
---

<!-- problem:start -->

# [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums)

## Description

<!-- description:start -->

<p>Given an array of integers arr, find the sum of <code>min(b)</code>, where <code>b</code> ranges over every (contiguous) subarray of <code>arr</code>. Since the answer may be large, return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,2,4]
<strong>Output:</strong> 17
<strong>Explanation:</strong> 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [11,81,94,43,3]
<strong>Output:</strong> 444
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 3 * 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack

The problem asks for the sum of the minimum values of each subarray, which is equivalent to finding the number of subarrays for which each element $arr[i]$ is the minimum, then multiplying by $arr[i]$, and finally summing these up.

Therefore, the focus of the problem is to find the number of subarrays for which $arr[i]$ is the minimum. For $arr[i]$, we find the first position $left[i]$ to its left that is less than $arr[i]$, and the first position $right[i]$ to its right that is less than or equal to $arr[i]$. The number of subarrays for which $arr[i]$ is the minimum is $(i - left[i]) \times (right[i] - i)$.

Note, why do we find the first position $right[i]$ to the right that is less than or equal to $arr[i]$, rather than less than $arr[i]$? This is because if we find the first position $right[i]$ to the right that is less than $arr[i]$, it will lead to duplicate calculations.

Let's take an example to illustrate. For the following array:

The element at index $3$ is $2$, the first element to its left that is less than $2$ is at index $0$. If we find the first element to its right that is less than $2$, we get index $7$. That is, the subarray interval is $(0, 7)$. Note that this is an open interval.

```
0 4 3 2 5 3 2 1
*     ^       *
```

In the same way, we can find the subarray interval for the element at index $6$, and find that its subarray interval is also $(0, 7)$. That is, the subarray intervals for the elements at index $3$ and index $6$ are the same. This leads to duplicate calculations.

```
0 4 3 2 5 3 2 1
*           ^ *
```

If we find the first element to its right that is less than or equal to its value, there will be no duplication, because the subarray interval for the element at index $3$ becomes $(0, 6)$, and the subarray interval for the element at index $6$ is $(0, 7)$, which are not the same.

Back to this problem, we just need to traverse the array, for each element $arr[i]$, use a monotonic stack to find the first position $left[i]$ to its left that is less than $arr[i]$, and the first position $right[i]$ to its right that is less than or equal to $arr[i]$. The number of subarrays for which $arr[i]$ is the minimum is $(i - left[i]) \times (right[i] - i)$, then multiply by $arr[i]$, and finally sum these up.

Be aware of data overflow and modulo operations.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $arr$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stk = []
        for i, v in enumerate(arr):
            while stk and arr[stk[-1]] >= v:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        mod = 10**9 + 7
        return sum((i - left[i]) * (right[i] - i) * v for i, v in enumerate(arr)) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
