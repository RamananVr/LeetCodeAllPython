---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3825.Longest%20Strictly%20Increasing%20Subsequence%20With%20Non-Zero%20Bitwise%20AND/README_EN.md
rating: 1845
source: Biweekly Contest 175 Q3
---

<!-- problem:start -->

# [3825. Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>Return the length of the <strong>longest strictly increasing <span data-keyword="subsequence-array-nonempty">subsequence</span></strong> in <code>nums</code> whose bitwise <strong>AND</strong> is <strong>non-zero</strong>. If no such <strong>subsequence</strong> exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>One longest strictly increasing subsequence is <code>[5, 7]</code>. The bitwise AND is <code>5 AND 7 = 5</code>, which is non-zero.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest strictly increasing subsequence is <code>[2, 3, 6]</code>. The bitwise AND is <code>2 AND 3 AND 6 = 2</code>, which is non-zero.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>One longest strictly increasing subsequence is <code>[1]</code>. The bitwise AND is 1, which is non-zero.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code>​​​​​​​</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration + Longest Increasing Subsequence

A non-zero bitwise AND result means that all numbers in the subsequence have a $1$ at a certain bit position. We can enumerate that bit position, then find the longest strictly increasing subsequence among all numbers that have a $1$ at that bit position, and take the maximum value across all enumerations as the answer.

The time complexity is $O(\log M \times n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ and $M$ are the length of the array and the maximum value in the array, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        def lis(arr: List[int]) -> int:
            g = []
            for x in arr:
                j = bisect_left(g, x)
                if j == len(g):
                    g.append(x)
                else:
                    g[j] = x
            return len(g)

        ans = 0
        m = max(nums).bit_length()
        for i in range(m):
            arr = [x for x in nums if x >> i & 1]
            ans = max(ans, lis(arr))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
