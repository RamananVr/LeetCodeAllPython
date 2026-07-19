---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1481.Least%20Number%20of%20Unique%20Integers%20after%20K%20Removals/README_EN.md
rating: 1284
source: Weekly Contest 193 Q2
tags:
    - Greedy
    - Array
    - Hash Table
    - Counting
    - Sorting
---

<!-- problem:start -->

# [1481. Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals)

## Description

<!-- description:start -->

<p>Given an array of integers&nbsp;<code>arr</code>&nbsp;and an integer <code>k</code>.&nbsp;Find the <em>least number of unique integers</em>&nbsp;after removing <strong>exactly</strong> <code>k</code> elements<b>.</b></p>

<ol>

</ol>

<p>&nbsp;</p>

<p><strong class="example">Example 1:</strong></p>

<pre>

<strong>Input: </strong>arr = [5,5,4], k = 1

<strong>Output: </strong>1

<strong>Explanation</strong>: Remove the single 4, only 5 is left.

</pre>

<strong class="example">Example 2:</strong>

<pre>

<strong>Input: </strong>arr = [4,3,1,1,3,3,2], k = 3

<strong>Output: </strong>2

<strong>Explanation</strong>: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.</pre>

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>

    <li><code>1 &lt;= arr.length&nbsp;&lt;= 10^5</code></li>

    <li><code>1 &lt;= arr[i] &lt;= 10^9</code></li>

    <li><code>0 &lt;= k&nbsp;&lt;= arr.length</code></li>

</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Sorting

We use the hash table $cnt$ to count the number of times each integer in the array $arr$ appears, and then sort the values in $cnt$ in ascending order, and record them in the array $nums$.

Next, we traverse the array $nums$. For the current value that we traverse to $nums[i]$, we subtract $k$ by $nums[i]$. If $k \lt 0$, it means that we have removed $k$ elements, and the minimum number of different integers in the array is the length of $nums$ minus the index $i$ that we traverse to at the current time. Return directly.

If we traverse to the end, it means that we have removed all the elements, and the minimum number of different integers in the array is $0$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $arr$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)
        for i, v in enumerate(sorted(cnt.values())):
            k -= v
            if k < 0:
                return len(cnt) - i
        return 0
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
