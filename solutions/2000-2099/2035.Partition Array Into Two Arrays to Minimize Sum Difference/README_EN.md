---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2035.Partition%20Array%20Into%20Two%20Arrays%20to%20Minimize%20Sum%20Difference/README_EN.md
rating: 2489
source: Weekly Contest 262 Q4
tags:
    - Bit Manipulation
    - Array
    - Two Pointers
    - Binary Search
    - Dynamic Programming
    - Bitmask
    - Ordered Set
    - Sorting
---

<!-- problem:start -->

# [2035. Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of <code>2 * n</code> integers. You need to partition <code>nums</code> into <strong>two</strong> arrays of length <code>n</code> to <strong>minimize the absolute difference</strong> of the <strong>sums</strong> of the arrays. To partition <code>nums</code>, put each element of <code>nums</code> into <strong>one</strong> of the two arrays.</p>

<p>Return <em>the <strong>minimum</strong> possible absolute difference</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="example-1" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2035.Partition%20Array%20Into%20Two%20Arrays%20to%20Minimize%20Sum%20Difference/images/ex1.png" style="width: 240px; height: 106px;" />
<pre>
<strong>Input:</strong> nums = [3,9,7,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-36,36]
<strong>Output:</strong> 72
<strong>Explanation:</strong> One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="example-3" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2000-2099/2035.Partition%20Array%20Into%20Two%20Arrays%20to%20Minimize%20Sum%20Difference/images/ex3.png" style="width: 316px; height: 106px;" />
<pre>
<strong>Input:</strong> nums = [2,-1,0,4,-2,-9]
<strong>Output:</strong> 0
<strong>Explanation:</strong> One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 15</code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>-10<sup>7</sup> &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) >> 1
        f = defaultdict(set)
        g = defaultdict(set)
        for i in range(1 << n):
            s = cnt = 0
            s1 = cnt1 = 0
            for j in range(n):
                if (i & (1 << j)) != 0:
                    s += nums[j]
                    cnt += 1
                    s1 += nums[n + j]
                    cnt1 += 1
                else:
                    s -= nums[j]
                    s1 -= nums[n + j]
            f[cnt].add(s)
            g[cnt1].add(s1)

        ans = inf
        for i in range(n + 1):
            fi, gi = sorted(list(f[i])), sorted(list(g[n - i]))
            # min(abs(f[i] + g[n - i]))
            for a in fi:
                left, right = 0, len(gi) - 1
                b = -a
                while left < right:
                    mid = (left + right) >> 1
                    if gi[mid] >= b:
                        right = mid
                    else:
                        left = mid + 1
                ans = min(ans, abs(a + gi[left]))
                if left > 0:
                    ans = min(ans, abs(a + gi[left - 1]))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
