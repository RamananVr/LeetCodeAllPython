---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3766.Minimum%20Operations%20to%20Make%20Binary%20Palindrome/README_EN.md
rating: 1656
source: Biweekly Contest 171 Q2
tags:
    - Bit Manipulation
    - Array
    - Two Pointers
    - Binary Search
---

<!-- problem:start -->

# [3766. Minimum Operations to Make Binary Palindrome](https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>For each element <code>nums[i]</code>, you may perform the following operations <strong>any</strong> number of times (including zero):</p>

<ul>
	<li>Increase <code>nums[i]</code> by 1, or</li>
	<li>Decrease <code>nums[i]</code> by 1.</li>
</ul>

<p>A number is called a <strong>binary palindrome</strong> if its binary representation without leading zeros reads the same forward and backward.</p>

<p>Your task is to return an integer array <code>ans</code>, where <code>ans[i]</code> represents the <strong>minimum</strong> number of operations required to convert <code>nums[i]</code> into a <strong>binary palindrome</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal set of operations:</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>nums[i]</code></th>
			<th style="border: 1px solid black;">Binary(<code>nums[i]</code>)</th>
			<th style="border: 1px solid black;">Nearest<br />
			Palindrome</th>
			<th style="border: 1px solid black;">Binary<br />
			(Palindrome)</th>
			<th style="border: 1px solid black;">Operations Required</th>
			<th style="border: 1px solid black;"><code>ans[i]</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Already palindrome</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">10</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">11</td>
			<td style="border: 1px solid black;">Increase by 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">100</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">11</td>
			<td style="border: 1px solid black;">Decrease by 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

<p>Thus, <code>ans = [0, 1, 1]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [6,7,12]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,0,3]</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal set of operations:</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;"><code>nums[i]</code></th>
			<th style="border: 1px solid black;">Binary(<code>nums[i]</code>)</th>
			<th style="border: 1px solid black;">Nearest<br />
			Palindrome</th>
			<th style="border: 1px solid black;">Binary<br />
			(Palindrome)</th>
			<th style="border: 1px solid black;">Operations Required</th>
			<th style="border: 1px solid black;"><code>ans[i]</code></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">110</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">101</td>
			<td style="border: 1px solid black;">Decrease by 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">111</td>
			<td style="border: 1px solid black;">7</td>
			<td style="border: 1px solid black;">111</td>
			<td style="border: 1px solid black;">Already palindrome</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">12</td>
			<td style="border: 1px solid black;">1100</td>
			<td style="border: 1px solid black;">15</td>
			<td style="border: 1px solid black;">1111</td>
			<td style="border: 1px solid black;">Increase by 3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>

<p>Thus, <code>ans = [1, 0, 3]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code><sup>​​​​​​​</sup>1 &lt;= nums[i] &lt;=<sup> </sup>5000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Binary Search

We observe that the range of numbers given in the problem is only $[1, 5000]$. Therefore, we directly preprocess all binary palindromic numbers in the range $[0, 2^{14})$ and store them in an array, denoted as $\textit{p}$.

Next, for each number $x$, we use binary search to find the first palindromic number greater than or equal to $x$ in the array $\textit{p}$, denoted as $\textit{p}[i]$, as well as the first palindromic number less than $x$, denoted as $\textit{p}[i - 1]$. Then, we calculate the number of operations required to convert $x$ to these two palindromic numbers and take the minimum value as the answer.

The time complexity is $O(n \times \log M)$, and the space complexity is $O(M)$. Where $n$ is the length of the array $\textit{nums}$, and $M$ is the number of preprocessed binary palindromic numbers.

<!-- tabs:start -->

#### Python3

```python
p = []
for i in range(1 << 14):
    s = bin(i)[2:]
    if s == s[::-1]:
        p.append(i)

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            i = bisect_left(p, x)
            times = inf
            if i < len(p):
                times = min(times, p[i] - x)
            if i >= 1:
                times = min(times, x - p[i - 1])
            ans.append(times)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
