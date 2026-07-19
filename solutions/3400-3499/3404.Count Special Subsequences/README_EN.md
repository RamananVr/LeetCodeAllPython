---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3400-3499/3404.Count%20Special%20Subsequences/README_EN.md
rating: 2445
source: Weekly Contest 430 Q3
tags:
    - Array
    - Hash Table
    - Math
    - Enumeration
---

<!-- problem:start -->

# [3404. Count Special Subsequences](https://leetcode.com/problems/count-special-subsequences)

## Description

<!-- description:start -->

<p>You are given an array <code>nums</code> consisting of positive integers.</p>

<p>A <strong>special subsequence</strong> is defined as a <span data-keyword="subsequence-array">subsequence</span> of length 4, represented by indices <code>(p, q, r, s)</code>, where <code>p &lt; q &lt; r &lt; s</code>. This subsequence <strong>must</strong> satisfy the following conditions:</p>

<ul>
	<li><code>nums[p] * nums[r] == nums[q] * nums[s]</code></li>
	<li>There must be <em>at least</em> <strong>one</strong> element between each pair of indices. In other words, <code>q - p &gt; 1</code>, <code>r - q &gt; 1</code> and <code>s - r &gt; 1</code>.</li>
</ul>

<p>Return the <em>number</em> of different <strong>special</strong> <strong>subsequences</strong> in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,3,6,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is one special subsequence in <code>nums</code>.</p>

<ul>
	<li><code>(p, q, r, s) = (0, 2, 4, 6)</code>:

    <ul>
    	<li>This corresponds to elements <code>(1, 3, 3, 1)</code>.</li>
    	<li><code>nums[p] * nums[r] = nums[0] * nums[4] = 1 * 3 = 3</code></li>
    	<li><code>nums[q] * nums[s] = nums[2] * nums[6] = 3 * 1 = 3</code></li>
    </ul>
    </li>

</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,4,3,4,3,4,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>There are three special subsequences in <code>nums</code>.</p>

<ul>
	<li><code>(p, q, r, s) = (0, 2, 4, 6)</code>:

    <ul>
    	<li>This corresponds to elements <code>(3, 3, 3, 3)</code>.</li>
    	<li><code>nums[p] * nums[r] = nums[0] * nums[4] = 3 * 3 = 9</code></li>
    	<li><code>nums[q] * nums[s] = nums[2] * nums[6] = 3 * 3 = 9</code></li>
    </ul>
    </li>
    <li><code>(p, q, r, s) = (1, 3, 5, 7)</code>:
    <ul>
    	<li>This corresponds to elements <code>(4, 4, 4, 4)</code>.</li>
    	<li><code>nums[p] * nums[r] = nums[1] * nums[5] = 4 * 4 = 16</code></li>
    	<li><code>nums[q] * nums[s] = nums[3] * nums[7] = 4 * 4 = 16</code></li>
    </ul>
    </li>
    <li><code>(p, q, r, s) = (0, 2, 5, 7)</code>:
    <ul>
    	<li>This corresponds to elements <code>(3, 3, 4, 4)</code>.</li>
    	<li><code>nums[p] * nums[r] = nums[0] * nums[5] = 3 * 4 = 12</code></li>
    	<li><code>nums[q] * nums[s] = nums[2] * nums[7] = 3 * 4 = 12</code></li>
    </ul>
    </li>

</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>7 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        for r in range(4, n - 2):
            c = nums[r]
            for s in range(r + 2, n):
                d = nums[s]
                g = gcd(c, d)
                cnt[(d // g, c // g)] += 1
        ans = 0
        for q in range(2, n - 4):
            b = nums[q]
            for p in range(q - 1):
                a = nums[p]
                g = gcd(a, b)
                ans += cnt[(a // g, b // g)]
            c = nums[q + 2]
            for s in range(q + 4, n):
                d = nums[s]
                g = gcd(c, d)
                cnt[(d // g, c // g)] -= 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
