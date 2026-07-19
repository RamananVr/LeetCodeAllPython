---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2552.Count%20Increasing%20Quadruplets/README_EN.md
rating: 2432
source: Weekly Contest 330 Q4
tags:
    - Binary Indexed Tree
    - Array
    - Dynamic Programming
    - Enumeration
    - Prefix Sum
---

<!-- problem:start -->

# [2552. Count Increasing Quadruplets](https://leetcode.com/problems/count-increasing-quadruplets)

## Description

<!-- description:start -->

<p>Given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>n</code> containing all numbers from <code>1</code> to <code>n</code>, return <em>the number of increasing quadruplets</em>.</p>

<p>A quadruplet <code>(i, j, k, l)</code> is increasing if:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; k &lt; l &lt; n</code>, and</li>
	<li><code>nums[i] &lt; nums[k] &lt; nums[j] &lt; nums[l]</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,4,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
- When i = 0, j = 1, k = 2, and l = 3, nums[i] &lt; nums[k] &lt; nums[j] &lt; nums[l].
- When i = 0, j = 1, k = 2, and l = 4, nums[i] &lt; nums[k] &lt; nums[j] &lt; nums[l]. 
There are no other quadruplets, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There exists only one quadruplet with i = 0, j = 1, k = 2, l = 3, but since nums[j] &lt; nums[k], we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>4 &lt;= nums.length &lt;= 4000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
	<li>All the integers of <code>nums</code> are <strong>unique</strong>. <code>nums</code> is a permutation.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Enumeration + Preprocessing

We can enumerate $j$ and $k$ in the quadruplet, then the problem is transformed into, for the current $j$ and $k$:

- Count how many $l$ satisfy $l > k$ and $nums[l] > nums[j]$;
- Count how many $i$ satisfy $i < j$ and $nums[i] < nums[k]$.

We can use two two-dimensional arrays $f$ and $g$ to record these two pieces of information. Where $f[j][k]$ represents how many $l$ satisfy $l > k$ and $nums[l] > nums[j]$, and $g[j][k]$ represents how many $i$ satisfy $i < j$ and $nums[i] < nums[k]$.

Therefore, the answer is the sum of all $f[j][k] \times g[j][k]$.

The time complexity is $O(n^2)$, and the space complexity is $O(n^2)$. Where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        g = [[0] * n for _ in range(n)]
        for j in range(1, n - 2):
            cnt = sum(nums[l] > nums[j] for l in range(j + 1, n))
            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    f[j][k] = cnt
                else:
                    cnt -= 1
        for k in range(2, n - 1):
            cnt = sum(nums[i] < nums[k] for i in range(k))
            for j in range(k - 1, 0, -1):
                if nums[j] > nums[k]:
                    g[j][k] = cnt
                else:
                    cnt -= 1
        return sum(
            f[j][k] * g[j][k] for j in range(1, n - 2) for k in range(j + 1, n - 1)
        )
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
