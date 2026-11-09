---
comments: true
difficulty: Easy
rating: 1245
source: Biweekly Contest 3 Q1
tags:
    - Array
    - Two Pointers
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [1099. Two Sum Less Than K 🔒](https://leetcode.com/problems/two-sum-less-than-k)

## Description

<!-- description:start -->

<p>Given an array <code>nums</code> of integers and&nbsp;integer <code>k</code>, return the maximum <code>sum</code> such that there exists <code>i &lt; j</code> with <code>nums[i] + nums[j] = sum</code> and <code>sum &lt; k</code>. If no <code>i</code>, <code>j</code> exist satisfying this equation, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [34,23,1,24,75,33,54,8], k = 60
<strong>Output:</strong> 58
<strong>Explanation: </strong>We can use 34 and 24 to sum 58 which is less than 60.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,20,30], k = 15
<strong>Output:</strong> -1
<strong>Explanation: </strong>In this case it is not possible to get a pair sum less that 15.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 2000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Binary Search

<!-- thinking:start -->

> **Thinking**
>
> The largest pair sum strictly below $k$ is quadratic if every pair is tested. After sorting, each $x$ needs the largest right value below $k-x$, which is a binary search.
>
> For index $i$, `bisect_left` on $(i,n)$ finds $k-x$; the previous index, if still greater than $i$, updates the answer.
>
> The answer stays $-1$ when no pair qualifies.

<!-- thinking:end -->

We can first sort the array $\textit{nums}$, and initialize the answer as $-1$.

Next, we enumerate each element $\textit{nums}[i]$ in the array, and find the maximum $\textit{nums}[j]$ in the array that satisfies $\textit{nums}[j] + \textit{nums}[i] < k$. Here, we can use binary search to speed up the search process. If we find such a $\textit{nums}[j]$, then we can update the answer, i.e., $\textit{ans} = \max(\textit{ans}, \textit{nums}[i] + \textit{nums}[j])$.

After the enumeration ends, return the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = -1
        for i, x in enumerate(nums):
            j = bisect_left(nums, k - x, lo=i + 1) - 1
            if i < j:
                ans = max(ans, x + nums[j])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Sorting + Two Pointers

<!-- thinking:start -->

> **Thinking**
>
> One binary search per $x$ is $O(n \log n)$. Two pointers use the same monotonicity: a small sum moves the left end right; a sum of at least $k$ moves the right end left.
>
> A single pass covers the Pareto front of distinct-index pairs with a smaller constant.

<!-- thinking:end -->

Similar to Solution 1, we can first sort the array $\textit{nums}$, and initialize the answer as $-1$.

Next, we use two pointers $i$ and $j$ to point to the left and right ends of the array, respectively. Each time we judge whether $s = \textit{nums}[i] + \textit{nums}[j]$ is less than $k$. If it is less than $k$, then we can update the answer, i.e., $\textit{ans} = \max(\textit{ans}, s)$, and move $i$ one step to the right, otherwise move $j$ one step to the left.

After the enumeration ends, return the answer.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = -1
        while i < j:
            if (s := nums[i] + nums[j]) < k:
                ans = max(ans, s)
                i += 1
            else:
                j -= 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
