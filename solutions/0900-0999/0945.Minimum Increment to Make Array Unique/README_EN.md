---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0900-0999/0945.Minimum%20Increment%20to%20Make%20Array%20Unique/README_EN.md
tags:
    - Greedy
    - Array
    - Counting
    - Sorting
---

<!-- problem:start -->

# [945. Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>. In one move, you can pick an index <code>i</code> where <code>0 &lt;= i &lt; nums.length</code> and increment <code>nums[i]</code> by <code>1</code>.</p>

<p>Return <em>the minimum number of moves to make every value in </em><code>nums</code><em> <strong>unique</strong></em>.</p>

<p>The test cases are generated so that the answer fits in a 32-bit integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> After 1 move, the array could be [1, 2, 3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,2,1,7]
<strong>Output:</strong> 6
<strong>Explanation:</strong> After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Greedy

First, we sort the array $\textit{nums}$, and use a variable $\textit{y}$ to record the current maximum value, initially $\textit{y} = -1$.

Then, we iterate through the array $\textit{nums}$. For each element $x$, we update $y$ to $\max(y + 1, x)$, and accumulate the operation count $y - x$ into the result.

After completing the iteration, we return the result.

The time complexity is $O(n \log n)$, and the space complexity is $O(\log n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans, y = 0, -1
        for x in nums:
            y = max(y + 1, x)
            ans += y - x
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- source:start -->

### Solution 2: Counting + Greedy

According to the problem description, the maximum value of the result array $m = \max(\textit{nums}) + \textit{len}(\textit{nums})$. We can use a counting array $\textit{cnt}$ to record the occurrence count of each element.

Then, we iterate from $0$ to $m - 1$. For each element $i$, if its occurrence count $\textit{cnt}[i]$ is greater than $1$, then we add $\textit{cnt}[i] - 1$ elements to $i + 1$, and accumulate the operation count into the result.

After completing the iteration, we return the result.

The time complexity is $O(m)$, and the space complexity is $O(m)$. Here, $m$ is the length of the array $\textit{nums}$ plus the maximum value in the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        m = max(nums) + len(nums)
        cnt = Counter(nums)
        ans = 0
        for i in range(m - 1):
            if (diff := cnt[i] - 1) > 0:
                cnt[i + 1] += diff
                ans += diff
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
