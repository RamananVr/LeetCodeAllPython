---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1900-1999/1918.Kth%20Smallest%20Subarray%20Sum/README_EN.md
tags:
    - Array
    - Binary Search
    - Sliding Window
---

<!-- problem:start -->

# [1918. Kth Smallest Subarray Sum 🔒](https://leetcode.com/problems/kth-smallest-subarray-sum)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>, return <em>the </em><code>k<sup>th</sup></code> <em><strong>smallest subarray sum</strong>.</em></p>

<p>A <strong>subarray</strong> is defined as a <strong>non-empty</strong> contiguous sequence of elements in an array. A <strong>subarray sum</strong> is the sum of all elements in the subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,3], k = 4
<strong>Output:</strong> 3
<strong>Explanation: </strong>The subarrays of [2,1,3] are:
- [2] with sum 2
- [1] with sum 1
- [3] with sum 3
- [2,1] with sum 3
- [1,3] with sum 4
- [2,1,3] with sum 6 
Ordering the sums from smallest to largest gives 1, 2, 3, <u>3</u>, 4, 6. The 4th smallest is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,5,5], k = 7
<strong>Output:</strong> 10
<strong>Explanation: </strong>The subarrays of [3,3,5,5] are:
- [3] with sum 3
- [3] with sum 3
- [5] with sum 5
- [5] with sum 5
- [3,3] with sum 6
- [3,5] with sum 8
- [5,5] with sum 10
- [3,3,5], with sum 11
- [3,5,5] with sum 13
- [3,3,5,5] with sum 16
Ordering the sums from smallest to largest gives 3, 3, 5, 5, 6, 8, <u>10</u>, 11, 13, 16. The 7th smallest is 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= n * (n + 1) / 2</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Binary Search + Two Pointers

We observe that all elements in the array are positive integers. The larger the subarray sum $s$, the more subarrays there are with sums less than or equal to $s$. This monotonicity allows us to use binary search to solve the problem.

We perform binary search on the subarray sum, initializing the left and right boundaries as the minimum value in the array $\textit{nums}$ and the sum of all elements in the array, respectively. Each time, we calculate the number of subarrays with sums less than or equal to the current middle value. If the count is greater than or equal to $k$, it means the current middle value $s$ might be the $k$-th smallest subarray sum, so we shrink the right boundary. Otherwise, we increase the left boundary. After the binary search ends, the left boundary will be the $k$-th smallest subarray sum.

The problem reduces to calculating the number of subarrays in an array with sums less than or equal to $s$, which we can compute using a function $f(s)$.

The function $f(s)$ is calculated as follows:

- Initialize two pointers $j$ and $i$, representing the left and right boundaries of the current window, with $j = i = 0$. Also, initialize the sum of elements in the window $t = 0$.
- Use a variable $\textit{cnt}$ to record the number of subarrays with sums less than or equal to $s$, initially $\textit{cnt} = 0$.
- Traverse the array $\textit{nums}$. For each element $\textit{nums}[i]$, add it to the window, i.e., $t = t + \textit{nums}[i]$. If $t > s$, move the left boundary of the window to the right until $t \leq s$, i.e., repeatedly execute $t -= \textit{nums}[j]$ and $j = j + 1$. Then update $\textit{cnt}$ as $\textit{cnt} = \textit{cnt} + i - j + 1$. Continue to the next element until the entire array is traversed.

Finally, return $cnt$ as the result of the function $f(s)$.

Time complexity is $O(n \times \log S)$, where $n$ is the length of the array $\textit{nums}$, and $S$ is the sum of all elements in the array $\textit{nums}$. Space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def f(s):
            t = j = 0
            cnt = 0
            for i, x in enumerate(nums):
                t += x
                while t > s:
                    t -= nums[j]
                    j += 1
                cnt += i - j + 1
            return cnt >= k

        l, r = min(nums), sum(nums)
        return l + bisect_left(range(l, r + 1), True, key=f)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
