---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3510.Minimum%20Pair%20Removal%20to%20Sort%20Array%20II/README_EN.md
rating: 2608
source: Weekly Contest 444 Q4
tags:
    - Array
    - Hash Table
    - Linked List
    - Doubly-Linked List
    - Ordered Set
    - Simulation
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3510. Minimum Pair Removal to Sort Array II](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii)

## Description

<!-- description:start -->

<p>Given an array <code>nums</code>, you can perform the following operation any number of times:</p>

<ul>
	<li>Select the <strong>adjacent</strong> pair with the <strong>minimum</strong> sum in <code>nums</code>. If multiple such pairs exist, choose the leftmost one.</li>
	<li>Replace the pair with their sum.</li>
</ul>

<p>Return the <strong>minimum number of operations</strong> needed to make the array <strong>non-decreasing</strong>.</p>

<p>An array is said to be <strong>non-decreasing</strong> if each element is greater than or equal to its previous element (if it exists).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The pair <code>(3,1)</code> has the minimum sum of 4. After replacement, <code>nums = [5,2,4]</code>.</li>
	<li>The pair <code>(2,4)</code> has the minimum sum of 6. After replacement, <code>nums = [5,6]</code>.</li>
</ul>

<p>The array <code>nums</code> became non-decreasing in two operations.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The array <code>nums</code> is already sorted.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Sorted Set

We define a sorted set $\textit{sl}$ to store tuples $(\textit{s}, i)$ of the sum of all adjacent element pairs and their left index, define another sorted set $\textit{idx}$ to store the indices of remaining elements in the current array, and use the variable $\textit{inv}$ to record the number of inversions in the current array. Initially, we traverse the array $\textit{nums}$, add tuples of the sum of all adjacent element pairs and their left index to the sorted set $\textit{sl}$, and calculate the number of inversions $\textit{inv}$.

In each operation, we retrieve the element pair $(\textit{s}, i)$ with the minimum sum from the sorted set $\textit{sl}$. Then we can determine that the element pair corresponding to indices $i$ and $j$ (where $j$ is the next index after $i$ in the sorted set $\textit{idx}$) is the adjacent element pair with the minimum sum in the current array. If $nums[i] > nums[j]$, this element pair is an inversion, and after merging and replacing, the number of inversions $\textit{inv}$ decreases by one.

Next, we need to update the element pairs related to indices $i$ and $j$:

1. If index $i$ has a predecessor index $h$ in the sorted set $\textit{idx}$, we need to update the element pair $(h, i)$. If $nums[h] > nums[i]$, this element pair is an inversion, and after merging and replacing, the number of inversions $\textit{inv}$ decreases by one. Then, we remove the element pair $(h, i)$ from the sorted set $\textit{sl}$ and add the new element pair $(h, s)$ to the sorted set $\textit{sl}$. If $nums[h] > s$, the new element pair is an inversion, and after merging and replacing, the number of inversions $\textit{inv}$ increases by one.

2. If index $j$ has a successor index $k$ in the sorted set $\textit{idx}$, we need to update the element pair $(j, k)$. If $nums[j] > nums[k]$, this element pair is an inversion, and after merging and replacing, the number of inversions $\textit{inv}$ decreases by one. Then, we remove the element pair $(j, k)$ from the sorted set $\textit{sl}$ and add the new element pair $(s, k)$ to the sorted set $\textit{sl}$. If $s > nums[k]$, the new element pair is an inversion, and after merging and replacing, the number of inversions $\textit{inv}$ increases by one.

Next, we replace the element at index $i$ with $\textit{s}$ and remove index $j$ from the sorted set $\textit{idx}$. We repeat the above process until the number of inversions $\textit{inv}$ becomes zero. Finally, the number of operations is the minimum number of operations required to make the array non-decreasing.

The time complexity is $O(n \log n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList()
        idx = SortedList(range(n))
        inv = 0
        for i in range(n - 1):
            sl.add((nums[i] + nums[i + 1], i))
            if nums[i] > nums[i + 1]:
                inv += 1
        ans = 0
        while inv:
            ans += 1
            s, i = sl.pop(0)
            pos = idx.index(i)
            j = idx[pos + 1]
            if nums[i] > nums[j]:
                inv -= 1
            if pos > 0:
                h = idx[pos - 1]
                if nums[h] > nums[i]:
                    inv -= 1
                sl.remove((nums[h] + nums[i], h))
                if nums[h] > s:
                    inv += 1
                sl.add((nums[h] + s, h))
            if pos + 2 < len(idx):
                k = idx[pos + 2]
                if nums[j] > nums[k]:
                    inv -= 1
                sl.remove((nums[j] + nums[k], j))
                if s > nums[k]:
                    inv += 1
                sl.add((s + nums[k], i))

            nums[i] = s
            idx.remove(j)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
