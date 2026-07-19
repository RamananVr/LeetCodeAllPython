---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3200-3299/3224.Minimum%20Array%20Changes%20to%20Make%20Differences%20Equal/README_EN.md
rating: 1996
source: Biweekly Contest 135 Q3
tags:
    - Array
    - Hash Table
    - Prefix Sum
---

<!-- problem:start -->

# [3224. Minimum Array Changes to Make Differences Equal](https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of size <code>n</code> where <code>n</code> is <strong>even</strong>, and an integer <code>k</code>.</p>

<p>You can perform some changes on the array, where in one change you can replace <strong>any</strong> element in the array with <strong>any</strong> integer in the range from <code>0</code> to <code>k</code>.</p>

<p>You need to perform some changes (possibly none) such that the final array satisfies the following condition:</p>

<ul>
	<li>There exists an integer <code>X</code> such that <code>abs(a[i] - a[n - i - 1]) = X</code> for all <code>(0 &lt;= i &lt; n)</code>.</li>
</ul>

<p>Return the <strong>minimum</strong> number of changes required to satisfy the above condition.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,1,2,4,3], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong><br />
We can perform the following changes:</p>

<ul>
	<li>Replace <code>nums[1]</code> by 2. The resulting array is <code>nums = [1,<u><strong>2</strong></u>,1,2,4,3]</code>.</li>
	<li>Replace <code>nums[3]</code> by 3. The resulting array is <code>nums = [1,2,1,<u><strong>3</strong></u>,4,3]</code>.</li>
</ul>

<p>The integer <code>X</code> will be 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1,2,3,3,6,5,4], k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong><br />
We can perform the following operations:</p>

<ul>
	<li>Replace <code>nums[3]</code> by 0. The resulting array is <code>nums = [0,1,2,<u><strong>0</strong></u>,3,6,5,4]</code>.</li>
	<li>Replace <code>nums[4]</code> by 4. The resulting array is <code>nums = [0,1,2,0,<strong><u>4</u></strong>,6,5,4]</code>.</li>
</ul>

<p>The integer <code>X</code> will be 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> is even.</li>
	<li><code>0 &lt;= nums[i] &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Difference Array

Assume that in the final array, the difference between the pair $\textit{nums}[i]$ and $\textit{nums}[n-i-1]$ is $s$.

Let's denote $x$ as the smaller value between $\textit{nums}[i]$ and $\textit{nums}[n-i-1]$, and $y$ as the larger value.

For each pair of numbers, we have the following scenarios:

- If no change is needed, then $y - x = s$.
- If one change is made, then $s \le \max(y, k - x)$, where the maximum value is achieved by changing $x$ to $0$, or changing $y$ to $k$.
- If two changes are made, then $s > \max(y, k - x)$.

That is:

- In the range $[0, y-x-1]$, $1$ change is needed.
- At $[y-x]$, no change is needed.
- In the range $[y-x+1, \max(y, k-x)]$, $1$ change is needed.
- In the range $[\max(y, k-x)+1, k]$, $2$ changes are needed.

We enumerate each pair of numbers and use a difference array to update the number of changes needed in different ranges for each pair.

Finally, we find the minimum value among the prefix sums from the difference array, which is the minimum number of changes needed.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

Similar problems:

- [1674. Minimum Moves to Make Array Complementary](https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1674.Minimum%20Moves%20to%20Make%20Array%20Complementary/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        d = [0] * (k + 2)
        n = len(nums)
        for i in range(n // 2):
            x, y = nums[i], nums[-i - 1]
            if x > y:
                x, y = y, x
            d[0] += 1
            d[y - x] -= 1
            d[y - x + 1] += 1
            d[max(y, k - x) + 1] -= 1
            d[max(y, k - x) + 1] += 2
        return min(accumulate(d))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
