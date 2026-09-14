---
comments: true
difficulty: Medium
tags:
    - Greedy
    - Array
    - String
    - Sorting
---

<!-- problem:start -->

# [179. Largest Number](https://leetcode.com/problems/largest-number)

## Description

<!-- description:start -->

<p>Given a list of non-negative integers <code>nums</code>, arrange them such that they form the largest number and return it.</p>

<p>Since the result may be very large, so you need to return a string instead of an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,2]
<strong>Output:</strong> &quot;210&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,30,34,5,9]
<strong>Output:</strong> &quot;9534330&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Form the largest number by concatenation. Numeric order and plain lexicographic order both fail: $9$ should precede $98$ because $998>989$. $n\le 100$. Compare $a+b$ with $b+a$ to order two strings, sort by that, and join. If the first character is $0$, every value was zero, so return $\texttt{"0"}$.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(v) for v in nums]
        nums.sort(key=cmp_to_key(lambda a, b: 1 if a + b < b + a else -1))
        return "0" if nums[0] == "0" else "".join(nums)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
