---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3100-3199/3164.Find%20the%20Number%20of%20Good%20Pairs%20II/README_EN.md
rating: 1777
source: Weekly Contest 399 Q3
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [3164. Find the Number of Good Pairs II](https://leetcode.com/problems/find-the-number-of-good-pairs-ii)

## Description

<!-- description:start -->

<p>You are given 2 integer arrays <code>nums1</code> and <code>nums2</code> of lengths <code>n</code> and <code>m</code> respectively. You are also given a <strong>positive</strong> integer <code>k</code>.</p>

<p>A pair <code>(i, j)</code> is called <strong>good</strong> if <code>nums1[i]</code> is divisible by <code>nums2[j] * k</code> (<code>0 &lt;= i &lt;= n - 1</code>, <code>0 &lt;= j &lt;= m - 1</code>).</p>

<p>Return the total number of <strong>good</strong> pairs.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [1,3,4], nums2 = [1,3,4], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>
The 5 good pairs are <code>(0, 0)</code>, <code>(1, 0)</code>, <code>(1, 1)</code>, <code>(2, 0)</code>, and <code>(2, 2)</code>.</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [1,2,4,12], nums2 = [2,4], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The 2 good pairs are <code>(3, 0)</code> and <code>(3, 1)</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>3</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Enumerate Multiples

We use a hash table `cnt1` to record the occurrence times of each number divided by $k$ in array `nums1`, and a hash table `cnt2` to record the occurrence times of each number in array `nums2`.

Next, we enumerate each number $x$ in array `nums2`. For each number $x$, we enumerate its multiples $y$, where the range of $y$ is $[x, \textit{mx}]$, where `mx` is the maximum key value in `cnt1`. Then we count the sum of `cnt1[y]`, denoted as $s$. Finally, we add $s \times v$ to the answer, where $v$ is `cnt2[x]`.

The time complexity is $O(n + m + (M / k) \times \log m)$, and the space complexity is $O(n + m)$. Where $n$ and $m$ are the lengths of arrays `nums1` and `nums2` respectively, and $M$ is the maximum value in array `nums1`.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt1 = Counter(x // k for x in nums1 if x % k == 0)
        if not cnt1:
            return 0
        cnt2 = Counter(nums2)
        ans = 0
        mx = max(cnt1)
        for x, v in cnt2.items():
            s = sum(cnt1[y] for y in range(x, mx + 1, x))
            ans += s * v
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
