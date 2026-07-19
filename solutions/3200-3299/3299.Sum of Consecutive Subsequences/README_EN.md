---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3299.Sum%20of%20Consecutive%20Subsequences/README_EN.md
tags:
    - Array
    - Hash Table
    - Dynamic Programming
---

<!-- problem:start -->

# [3299. Sum of Consecutive Subsequences 🔒](https://leetcode.com/problems/sum-of-consecutive-subsequences)

## Description

<!-- description:start -->

<p>We call an array <code>arr</code> of length <code>n</code> <strong>consecutive</strong> if one of the following holds:</p>

<ul>
	<li><code>arr[i] - arr[i - 1] == 1</code> for <em>all</em> <code>1 &lt;= i &lt; n</code>.</li>
	<li><code>arr[i] - arr[i - 1] == -1</code> for <em>all</em> <code>1 &lt;= i &lt; n</code>.</li>
</ul>

<p>The <strong>value</strong> of an array is the sum of its elements.</p>

<p>For example, <code>[3, 4, 5]</code> is a consecutive array of value 12 and <code>[9, 8]</code> is another of value 17. While <code>[3, 4, 3]</code> and <code>[8, 6]</code> are not consecutive.</p>

<p>Given an array of integers <code>nums</code>, return the <em>sum</em> of the <strong>values</strong> of all <strong>consecutive </strong><em>non-empty</em> <span data-keyword="subsequence-array">subsequences</span>.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9 </sup>+ 7.</code></p>

<p><strong>Note</strong> that an array of length 1 is also considered consecutive.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The consecutive subsequences are: <code>[1]</code>, <code>[2]</code>, <code>[1, 2]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,4,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">31</span></p>

<p><strong>Explanation:</strong></p>

<p>The consecutive subsequences are: <code>[1]</code>, <code>[4]</code>, <code>[2]</code>, <code>[3]</code>, <code>[1, 2]</code>, <code>[2, 3]</code>, <code>[4, 3]</code>, <code>[1, 2, 3]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration of Contributions

Let us count how many times each element $\textit{nums}[i]$ appears in a continuous subsequence of length greater than 1. Then, multiplying this count by $\textit{nums}[i]$ gives the contribution of $\textit{nums}[i]$ in all continuous subsequences of length greater than 1. We sum these contributions, and adding the sum of all elements, we get the answer.

We can first compute the contribution of strictly increasing subsequences, then the contribution of strictly decreasing subsequences, and finally add the sum of all elements.

To implement this, we define a function $\textit{calc}(\textit{nums})$, where $\textit{nums}$ is an array. This function returns the sum of all continuous subsequences of length greater than 1 in $\textit{nums}$.

In the function, we can use two arrays, $\textit{left}$ and $\textit{right}$, to record the number of strictly increasing subsequences ending with $\textit{nums}[i] - 1$ on the left of each element $\textit{nums}[i]$, and the number of strictly increasing subsequences starting with $\textit{nums}[i] + 1$ on the right of each element $\textit{nums}[i]$. In this way, we can calculate the contribution of $\textit{nums}$ in all continuous subsequences of length greater than 1 in $O(n)$ time complexity.

In the main function, we first call $\textit{calc}(\textit{nums})$ to compute the contribution of strictly increasing subsequences, then reverse $\textit{nums}$ and call $\textit{calc}(\textit{nums})$ again to compute the contribution of strictly decreasing subsequences. Finally, adding the sum of all elements gives the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def getSum(self, nums: List[int]) -> int:
        def calc(nums: List[int]) -> int:
            n = len(nums)
            left = [0] * n
            right = [0] * n
            cnt = Counter()
            for i in range(1, n):
                cnt[nums[i - 1]] += 1 + cnt[nums[i - 1] - 1]
                left[i] = cnt[nums[i] - 1]
            cnt = Counter()
            for i in range(n - 2, -1, -1):
                cnt[nums[i + 1]] += 1 + cnt[nums[i + 1] + 1]
                right[i] = cnt[nums[i] + 1]
            return sum((l + r + l * r) * x for l, r, x in zip(left, right, nums)) % mod

        mod = 10**9 + 7
        x = calc(nums)
        nums.reverse()
        y = calc(nums)
        return (x + y + sum(nums)) % mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
