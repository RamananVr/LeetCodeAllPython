---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3300-3399/3326.Minimum%20Division%20Operations%20to%20Make%20Array%20Non%20Decreasing/README_EN.md
rating: 1864
source: Weekly Contest 420 Q3
tags:
    - Greedy
    - Array
    - Math
    - Number Theory
---

<!-- problem:start -->

# [3326. Minimum Division Operations to Make Array Non Decreasing](https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>Any <strong>positive</strong> divisor of a natural number <code>x</code> that is <strong>strictly less</strong> than <code>x</code> is called a <strong>proper divisor</strong> of <code>x</code>. For example, 2 is a <em>proper divisor</em> of 4, while 6 is not a <em>proper divisor</em> of 6.</p>

<p>You are allowed to perform an <strong>operation</strong> any number of times on <code>nums</code>, where in each <strong>operation</strong> you select any <em>one</em> element from <code>nums</code> and divide it by its <strong>greatest</strong> <strong>proper divisor</strong>.</p>

<p>Return the <strong>minimum</strong> number of <strong>operations</strong> required to make the array <strong>non-decreasing</strong>.</p>

<p>If it is <strong>not</strong> possible to make the array <em>non-decreasing</em> using any number of operations, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [25,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Using a single operation, 25 gets divided by 5 and <code>nums</code> becomes <code>[5, 7]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [7,7,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Greedy

According to the problem description,

If an integer $x$ is a prime number, then its largest proper divisor is $1$, so $x / 1 = x$, meaning $x$ cannot be divided further.

If an integer $x$ is not a prime number, we assume the largest proper divisor of $x$ is $y$, then $x / y$ must be a prime number. Therefore, we find the smallest prime factor $\textit{lpf}[x]$ such that $x \bmod \textit{lpf}[x] = 0$, making $x$ become $\textit{lpf}[x]$, at which point it cannot be divided further.

Thus, we can preprocess the smallest prime factor for each integer from $1$ to $10^6$. Then, we traverse the array from right to left. If the current element is greater than the next element, we change the current element to its smallest prime factor. If after changing the current element to its smallest prime factor it is still greater than the next element, it means the array cannot be made non-decreasing, and we return $-1$. Otherwise, we increment the operation count by one. Continue traversing until the entire array is processed.

The time complexity for preprocessing is $O(M \times \log \log M)$, where $M = 10^6$. The time complexity for traversing the array is $O(n)$, where $n$ is the length of the array. The space complexity is $O(M)$.

<!-- tabs:start -->

#### Python3

```python
mx = 10**6 + 1
lpf = [0] * (mx + 1)
for i in range(2, mx + 1):
    if lpf[i] == 0:
        for j in range(i, mx + 1, i):
            if lpf[j] == 0:
                lpf[j] = i

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                nums[i] = lpf[nums[i]]
                if nums[i] > nums[i + 1]:
                    return -1
                ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
