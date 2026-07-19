---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0611.Valid%20Triangle%20Number/README_EN.md
tags:
    - Greedy
    - Array
    - Two Pointers
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return <em>the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,3,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,3,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Binary Search

A valid triangle must satisfy: **the sum of any two sides is greater than the third side**. That is:

$$a + b \gt c \tag{1}$$

$$a + c \gt b \tag{2}$$

$$b + c \gt a \tag{3}$$

If we arrange the sides in ascending order, i.e., $a \leq b \leq c$, then obviously conditions (2) and (3) are satisfied. We only need to ensure that condition (1) is also satisfied to form a valid triangle.

We enumerate $i$ in the range $[0, n - 3]$, enumerate $j$ in the range $[i + 1, n - 2]$, and perform binary search in the range $[j + 1, n - 1]$ to find the first index $left$ that is greater than or equal to $nums[i] + nums[j]$. Then, the values of $k$ in the range $[j + 1, left - 1]$ satisfy the condition, and we add them to the result $\textit{ans}$.

The time complexity is $O(n^2\log n)$, and the space complexity is $O(\log n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = bisect_left(nums, nums[i] + nums[j], lo=j + 1) - 1
                ans += k - j
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
