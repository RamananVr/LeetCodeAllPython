---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2300-2399/2386.Find%20the%20K-Sum%20of%20an%20Array/README_EN.md
rating: 2647
source: Weekly Contest 307 Q4
tags:
    - Array
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [2386. Find the K-Sum of an Array](https://leetcode.com/problems/find-the-k-sum-of-an-array)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and a <strong>positive</strong> integer <code>k</code>. You can choose any <strong>subsequence</strong> of the array and sum all of its elements together.</p>

<p>We define the <strong>K-Sum</strong> of the array as the <code>k<sup>th</sup></code> <strong>largest</strong> subsequence sum that can be obtained (<strong>not</strong> necessarily distinct).</p>

<p>Return <em>the K-Sum of the array</em>.</p>

<p>A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>

<p><strong>Note</strong> that the empty subsequence is considered to have a sum of <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,4,-2], k = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> All the possible subsequence sums that we can obtain are the following sorted in decreasing order:
6, 4, 4, 2, <u>2</u>, 0, 0, -2.
The 5-Sum of the array is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,-2,3,4,-10,12], k = 16
<strong>Output:</strong> 10
<strong>Explanation:</strong> The 16-Sum of the array is 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(2000, 2<sup>n</sup>)</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Priority Queue (Min-Heap)

First, we find the maximum subarray sum $mx$, which is the sum of all positive numbers.

It can be observed that the sum of other subarrays can be considered as the maximum subarray sum minus the sum of other parts of the subarray. Therefore, we can convert the problem into finding the $k$-th smallest subarray sum.

We only need to sort all numbers in ascending order by their absolute values, then build a min-heap to store the tuple $(s, i)$, where $s$ is the current sum and $i$ is the index of the next number to be selected in the subarray.

Each time, we extract the top of the heap and insert two new situations: one is to select the next number, and the other is to select the next number but not the current number.

Since the array is sorted in ascending order, this method can traverse all subarray sums in order without omission.

The time complexity is $O(n \times \log n + k \times \log k)$, where $n$ is the length of the array $\textit{nums}$. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        mx = 0
        for i, x in enumerate(nums):
            if x > 0:
                mx += x
            else:
                nums[i] = -x
        nums.sort()
        h = [(0, 0)]
        for _ in range(k - 1):
            s, i = heappop(h)
            if i < len(nums):
                heappush(h, (s + nums[i], i + 1))
                if i:
                    heappush(h, (s + nums[i] - nums[i - 1], i + 1))
        return mx - h[0][0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
