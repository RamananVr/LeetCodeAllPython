---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0238.Product%20of%20Array%20Except%20Self/README_EN.md
tags:
    - Array
    - Prefix Sum
---

<!-- problem:start -->

# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The input is generated such that <code>answer[i]</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Can you solve the problem in <code>O(1)</code>&nbsp;extra&nbsp;space complexity? (The output array <strong>does not</strong> count as extra space for space complexity analysis.)</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two Passes

We define two variables $\textit{left}$ and $\textit{right}$ to represent the product of all elements to the left and right of the current element, respectively. Initially, $\textit{left} = 1$ and $\textit{right} = 1$. We define an answer array $\textit{ans}$ of length $n$.

First, we traverse the array from left to right. For the $i$-th element, we update $\textit{ans}[i]$ with $\textit{left}$, then multiply $\textit{left}$ by $\textit{nums}[i]$.

Next, we traverse the array from right to left. For the $i$-th element, we update $\textit{ans}[i]$ to $\textit{ans}[i] \times \textit{right}$, then multiply $\textit{right}$ by $\textit{nums}[i]$.

After the traversal, we return the answer array $\textit{ans}$.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$. Ignoring the space consumption of the answer array, the space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        left = right = 1
        for i, x in enumerate(nums):
            ans[i] = left
            left *= x
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
