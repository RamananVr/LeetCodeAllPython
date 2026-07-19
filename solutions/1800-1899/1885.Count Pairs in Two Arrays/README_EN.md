---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1800-1899/1885.Count%20Pairs%20in%20Two%20Arrays/README_EN.md
tags:
    - Array
    - Two Pointers
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [1885. Count Pairs in Two Arrays 🔒](https://leetcode.com/problems/count-pairs-in-two-arrays)

## Description

<!-- description:start -->

<p>Given two integer arrays <code>nums1</code> and <code>nums2</code> of length <code>n</code>, count the pairs of indices <code>(i, j)</code> such that <code>i &lt; j</code> and <code>nums1[i] + nums1[j] &gt; nums2[i] + nums2[j]</code>.</p>

<p>Return <em>the <strong>number of pairs</strong> satisfying the condition.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,1,2,1], nums2 = [1,2,1,2]
<strong>Output:</strong> 1
<strong>Explanation</strong>: The pairs satisfying the condition are:
- (0, 2) where 2 + 2 &gt; 1 + 1.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,10,6,2], nums2 = [1,4,1,5]
<strong>Output:</strong> 5
<strong>Explanation</strong>: The pairs satisfying the condition are:
- (0, 1) where 1 + 10 &gt; 1 + 4.
- (0, 2) where 1 + 6 &gt; 1 + 1.
- (1, 2) where 10 + 6 &gt; 4 + 1.
- (1, 3) where 10 + 2 &gt; 4 + 5.
- (2, 3) where 6 + 2 &gt; 1 + 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorting + Two Pointers

We can transform the inequality in the problem to $\textit{nums1}[i] - \textit{nums2}[i] + \textit{nums1}[j] - \textit{nums2}[j] > 0$, which simplifies to $\textit{nums}[i] + \textit{nums}[j] > 0$, where $\textit{nums}[i] = \textit{nums1}[i] - \textit{nums2}[i]$.

For the array $\textit{nums}$, we need to find all pairs $(i, j)$ that satisfy $\textit{nums}[i] + \textit{nums}[j] > 0$.

We can sort the array $\textit{nums}$ and then use the two-pointer method. Initialize the left pointer $l = 0$ and the right pointer $r = n - 1$. Each time, we check if $\textit{nums}[l] + \textit{nums}[r]$ is less than or equal to $0$. If it is, we move the left pointer to the right in a loop until $\textit{nums}[l] + \textit{nums}[r] > 0$. At this point, all pairs with the left pointer at $l$, $l + 1$, $l + 2$, $\cdots$, $r - 1$ and the right pointer at $r$ satisfy the condition, and there are $r - l$ such pairs. We add these pairs to the answer. Then, move the right pointer to the left and continue the above process until $l \ge r$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        nums = [a - b for a, b in zip(nums1, nums2)]
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            while l < r and nums[l] + nums[r] <= 0:
                l += 1
            ans += r - l
            r -= 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
