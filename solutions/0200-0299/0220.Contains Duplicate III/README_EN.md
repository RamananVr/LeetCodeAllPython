---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0220.Contains%20Duplicate%20III/README_EN.md
tags:
    - Array
    - Bucket Sort
    - Ordered Set
    - Sorting
    - Sliding Window
---

<!-- problem:start -->

# [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and two integers <code>indexDiff</code> and <code>valueDiff</code>.</p>

<p>Find a pair of indices <code>(i, j)</code> such that:</p>

<ul>
	<li><code>i != j</code>,</li>
	<li><code>abs(i - j) &lt;= indexDiff</code>.</li>
	<li><code>abs(nums[i] - nums[j]) &lt;= valueDiff</code>, and</li>
</ul>

<p>Return <code>true</code><em> if such pair exists or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
<strong>Output:</strong> true
<strong>Explanation:</strong> We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --&gt; 0 != 3
abs(i - j) &lt;= indexDiff --&gt; abs(0 - 3) &lt;= 3
abs(nums[i] - nums[j]) &lt;= valueDiff --&gt; abs(1 - 1) &lt;= 0
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= indexDiff &lt;= nums.length</code></li>
	<li><code>0 &lt;= valueDiff &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sliding Window + Ordered Set

We maintain a sliding window of size $k$, and the elements in the window are kept in order.

We traverse the array `nums`. For each element $nums[i]$, we look for the first element in the ordered set that is greater than or equal to $nums[i] - t$. If the element exists, and this element is less than or equal to $nums[i] + t$, it means we have found a pair of elements that meet the conditions, and we return `true`. Otherwise, we insert $nums[i]$ into the ordered set, and if the size of the ordered set exceeds $k$, we need to remove the earliest added element from the ordered set.

The time complexity is $O(n \times \log k)$, where $n$ is the length of the array `nums`. For each element, we need $O(\log k)$ time to find the element in the ordered set, and there are $n$ elements in total, so the total time complexity is $O(n \times \log k)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        s = SortedSet()
        for i, v in enumerate(nums):
            j = s.bisect_left(v - valueDiff)
            if j < len(s) and s[j] <= v + valueDiff:
                return True
            s.add(v)
            if i >= indexDiff:
                s.remove(nums[i - indexDiff])
        return False
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
