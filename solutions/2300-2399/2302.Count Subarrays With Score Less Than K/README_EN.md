---
comments: true
difficulty: Hard
rating: 1808
source: Biweekly Contest 80 Q4
tags:
    - Array
    - Binary Search
    - Prefix Sum
    - Sliding Window
---

<!-- problem:start -->

# [2302. Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k)

## Description

<!-- description:start -->

<p>The <strong>score</strong> of an array is defined as the <strong>product</strong> of its sum and its length.</p>

<ul>
	<li>For example, the score of <code>[1, 2, 3, 4, 5]</code> is <code>(1 + 2 + 3 + 4 + 5) * 5 = 75</code>.</li>
</ul>

<p>Given a positive integer array <code>nums</code> and an integer <code>k</code>, return <em>the <strong>number of non-empty subarrays</strong> of</em> <code>nums</code> <em>whose score is <strong>strictly less</strong> than</em> <code>k</code>.</p>

<p>A <strong>subarray</strong> is a contiguous sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,4,3,5], k = 10
<strong>Output:</strong> 6
<strong>Explanation:</strong>
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1], k = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong>
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>15</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sum + Binary Search

<!-- thinking:start -->

> **Thinking**
>
> A subarray’s score is its sum times its length. Enumerating all subarrays is $O(n^2)$ and fails for $n \le 10^5$. All values are positive, so for a fixed right end a longer window has a larger score, and valid left ends form a prefix.
>
> Prefix sums answer any range sum in constant time. Binary-search the largest length $l$ with $(s[i]-s[i-l])\times l < k$. That right end contributes $l$ subarrays.

<!-- thinking:end -->

First, we calculate the prefix sum array $s$ of the array $\textit{nums}$, where $s[i]$ represents the sum of the first $i$ elements of $\textit{nums}$.

Next, we enumerate each element of $\textit{nums}$ as the last element of a subarray. For each element, we can use binary search to find the maximum length $l$ such that $s[i] - s[i - l] \times l < k$. The number of subarrays ending at this element is $l$, and summing up all $l$ gives the final answer.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        ans = 0
        for i in range(1, len(s)):
            l, r = 0, i
            while l < r:
                mid = (l + r + 1) >> 1
                if (s[i] - s[i - mid]) * mid < k:
                    l = mid
                else:
                    r = mid - 1
            ans += l
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Two Pointers

<!-- thinking:start -->

> **Thinking**
>
> Method 1 stores a prefix array and pays a logarithmic cost per right end. Positivity makes the score decrease as the left end moves right, so the left pointer only advances. Maintain the window sum and count valid subarrays in one linear scan.

<!-- thinking:end -->

We can use the two-pointer technique to maintain a sliding window such that the sum of elements in the window is less than $k$. The number of subarrays ending at the current element is equal to the length of the window. Summing up all the window lengths gives the final answer.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = s = j = 0
        for i, x in enumerate(nums):
            s += x
            while s * (i - j + 1) >= k:
                s -= nums[j]
                j += 1
            ans += i - j + 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
