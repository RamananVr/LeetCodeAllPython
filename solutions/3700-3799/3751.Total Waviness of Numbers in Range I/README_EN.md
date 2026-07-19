---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3751.Total%20Waviness%20of%20Numbers%20in%20Range%20I/README_EN.md
rating: 1404
source: Biweekly Contest 170 Q2
tags:
    - Math
    - Dynamic Programming
    - Enumeration
---

<!-- problem:start -->

# [3751. Total Waviness of Numbers in Range I](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i)

## Description

<!-- description:start -->

<p>You are given two integers <code>num1</code> and <code>num2</code> representing an <strong>inclusive</strong> range <code>[num1, num2]</code>.</p>

<p>The <strong>waviness</strong> of a number is defined as the total count of its <strong>peaks</strong> and <strong>valleys</strong>:</p>

<ul>
	<li>A digit is a <strong>peak</strong> if it is <strong>strictly greater</strong> than both of its immediate neighbors.</li>
	<li>A digit is a <strong>valley</strong> if it is <strong>strictly less</strong> than both of its immediate neighbors.</li>
	<li>The first and last digits of a number <strong>cannot</strong> be peaks or valleys.</li>
	<li>Any number with fewer than 3 digits has a waviness of 0.</li>
</ul>
Return the total sum of waviness for all numbers in the range <code>[num1, num2]</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 120, num2 = 130</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>
In the range <code>[120, 130]</code>:

<ul>
	<li><code>120</code>: middle digit 2 is a peak, waviness = 1.</li>
	<li><code>121</code>: middle digit 2 is a peak, waviness = 1.</li>
	<li><code>130</code>: middle digit 3 is a peak, waviness = 1.</li>
	<li>All other numbers in the range have a waviness of 0.</li>
</ul>

<p>Thus, total waviness is <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 198, num2 = 202</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>
In the range <code>[198, 202]</code>:

<ul>
	<li><code>198</code>: middle digit 9 is a peak, waviness = 1.</li>
	<li><code>201</code>: middle digit 0 is a valley, waviness = 1.</li>
	<li><code>202</code>: middle digit 0 is a valley, waviness = 1.</li>
	<li>All other numbers in the range have a waviness of 0.</li>
</ul>

<p>Thus, total waviness is <code>1 + 1 + 1 = 3</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num1 = 4848, num2 = 4848</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Number <code>4848</code>: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1 &lt;= num2 &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We define a helper function $f(x)$ to calculate the waviness value of integer $x$. In this function, we store each digit of integer $x$ in an array $\textit{nums}$. If the number has fewer than 3 digits, the waviness value is 0. Otherwise, we iterate through each non-leading and non-trailing digit in the array $\textit{nums}$, determine whether it is a peak or valley, and count the waviness value.

Then, we iterate through each integer $x$ in the range $[\textit{num1}, \textit{num2}]$ and accumulate its waviness value $f(x)$ to obtain the final result.

The time complexity is $O((\textit{num2} - \textit{num1} + 1) \cdot \log \textit{num2})$ and the space complexity is $O(\log \textit{num2})$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def f(x: int) -> int:
            nums = []
            while x:
                nums.append(x % 10)
                x //= 10
            m = len(nums)
            if m < 3:
                return 0
            s = 0
            for i in range(1, m - 1):
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    s += 1
                elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                    s += 1
            return s

        return sum(f(x) for x in range(num1, num2 + 1))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
