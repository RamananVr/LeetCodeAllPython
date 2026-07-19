---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2863.Maximum%20Length%20of%20Semi-Decreasing%20Subarrays/README_EN.md
tags:
    - Stack
    - Array
    - Sorting
    - Monotonic Stack
---

<!-- problem:start -->

# [2863. Maximum Length of Semi-Decreasing Subarrays 🔒](https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>Return <em>the length of the <strong>longest semi-decreasing</strong> subarray of </em><code>nums</code><em>, and </em><code>0</code><em> if there are no such subarrays.</em></p>

<ul>
	<li>A <b>subarray</b> is a contiguous non-empty sequence of elements within an array.</li>
	<li>A non-empty array is <strong>semi-decreasing</strong> if its first element is <strong>strictly greater</strong> than its last element.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,6,5,4,3,2,1,6,10,11]
<strong>Output:</strong> 8
<strong>Explanation:</strong> Take the subarray [7,6,5,4,3,2,1,6].
The first element is 7 and the last one is 6 so the condition is met.
Hence, the answer would be the length of the subarray or 8.
It can be shown that there aren&#39;t any subarrays with the given condition with a length greater than 8.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [57,55,50,60,61,58,63,59,64,60,63]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Take the subarray [61,58,63,59,64,60].
The first element is 61 and the last one is 60 so the condition is met.
Hence, the answer would be the length of the subarray or 6.
It can be shown that there aren&#39;t any subarrays with the given condition with a length greater than 6.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there are no semi-decreasing subarrays in the given array, the answer is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Sorting

The problem is essentially finding the maximum length of the inverse pairs. We can use a hash table $d$ to record the index $i$ corresponding to each number $x$ in the array.

Next, we traverse the keys of the hash table in descending order of the numbers. We maintain a number $k$ to keep track of the smallest index that has appeared so far. For the current number $x$, we can get a maximum inverse pair length of $d[x][|d[x]|-1]-k + 1$, where $|d[x]|$ represents the length of the array $d[x]$, i.e., the number of times the number $x$ appears in the original array. We update the answer accordingly. Then, we update $k$ to $d[x][0]$, which is the index where the number $x$ first appears in the original array. We continue to traverse the keys of the hash table until all keys are traversed.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        ans, k = 0, inf
        for x in sorted(d, reverse=True):
            ans = max(ans, d[x][-1] - k + 1)
            k = min(k, d[x][0])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
