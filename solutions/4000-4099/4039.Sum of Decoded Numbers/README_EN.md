---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/4000-4099/4039.Sum%20of%20Decoded%20Numbers/README_EN.md
---

<!-- problem:start -->

# [4039. Sum of Decoded Numbers](https://leetcode.com/problems/sum-of-decoded-numbers)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>Each <code>nums[i]</code> is an <strong>encoded</strong> integer representing two positive integers <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code>. To decode <code>nums[i]</code>, define:</p>

<ul>
	<li><code>width<sub>i</sub> = nums[i] % 10</code>.</li>
	<li><code>d<sub>i</sub> = floor(nums[i] / 10)</code>.</li>
	<li><code>x<sub>i</sub></code> as the integer formed by the first <code>width<sub>i</sub></code> digits of the decimal representation of <code>d<sub>i</sub></code>.</li>
	<li><code>y<sub>i</sub></code> as the integer formed by all remaining digits of the decimal representation of <code>d<sub>i</sub></code>.</li>
</ul>

<p>It is guaranteed that the decimal representation of <code>d<sub>i</sub></code> contains more than <code>width<sub>i</sub></code> digits. Therefore, both <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> contain at least one digit.</p>

<p>The <strong>decoded value</strong> of <code>nums[i]</code> is <code>x<sub>i</sub><sup>y<sub>i</sub></sup></code>.</p>

<p>Return the sum of the decoded values of all elements in <code>nums</code>, modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>The <code>floor()</code> function returns the integer part of the division.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [231]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For 231, we have <code>width = 1</code>, <code>d = 23</code>, <code>x = 2</code>, and <code>y = 3</code>.</li>
	<li>The decoded value of 231 is <code>2<sup>3</sup> = 8</code>.</li>
	<li>Since there is only one element in <code>nums</code>, the sum of the decoded values is 8.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2522,2101]</span></p>

<p><strong>Output:</strong> <span class="example-io">1649</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For 2522, we have <code>width = 2</code>, <code>d = 252</code>, <code>x = 25</code>, and <code>y = 2</code>.</li>
	<li>The decoded value of 2522 is <code>25<sup>2</sup> = 625</code>.</li>
	<li>For 2101, we have <code>width = 1</code>, <code>d = 210</code>, <code>x = 2</code>, and <code>y = 10</code>.</li>
	<li>The decoded value of 2101 is <code>2<sup>10</sup> = 1024</code>.</li>
	<li>The sum of the decoded values is <code>625 + 1024 = 1649</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2301]</span></p>

<p><strong>Output:</strong> <span class="example-io">73741817</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For 2301, we have <code>width = 1</code>, <code>d = 230</code>, <code>x = 2</code>, and <code>y = 30</code>.</li>
	<li>The decoded value is <code>2<sup>30</sup> = 1073741824</code>.</li>
	<li>Therefore, the answer is <code>1073741824 modulo (10<sup>9</sup> + 7) = 73741817</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>100 &lt; nums[i] &lt; 10<sup>15</sup></code></li>
	<li><code>1 &lt;= width<sub>i</sub> &lt;= 9</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt; 10<sup>9</sup></code></li>
	<li>The digit sequences used to form <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> do not have leading zeros.</li>
	<li>It is guaranteed that every element in <code>nums</code> is a valid encoded integer.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation + Fast Power

We decode each element exactly as the statement describes. For each element $v$ in $\textit{nums}$, its width is $w = v \bmod 10$, and the number left after dropping the last digit is $d = \lfloor v / 10 \rfloor$. Converting $d$ to its decimal string $s$, the value $x$ is the integer formed by the first $w$ characters of $s$, and $y$ is the integer formed by the remaining characters.

Since $y$ can be as large as $10^9$, multiplying repeatedly would be too slow, so we use fast power to compute $x^y \bmod (10^9 + 7)$ in $O(\log y)$ time, then accumulate the decoded values modulo $10^9 + 7$.

The time complexity is $O(n \times \log M)$, and the space complexity is $O(\log M)$. Here, $n$ is the length of the array $\textit{nums}$, and $M$ is the maximum value in the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def sumDecoded(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        ans = 0
        for v in nums:
            d, w = divmod(v, 10)
            s = str(d)
            x = int(s[:w])
            y = int(s[w:])
            ans = (ans + pow(x, y, mod)) % mod
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
