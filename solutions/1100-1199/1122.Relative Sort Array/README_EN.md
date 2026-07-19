---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1122.Relative%20Sort%20Array/README_EN.md
rating: 1188
source: Weekly Contest 145 Q1
tags:
    - Array
    - Hash Table
    - Counting Sort
    - Sorting
---

<!-- problem:start -->

# [1122. Relative Sort Array](https://leetcode.com/problems/relative-sort-array)

## Description

<!-- description:start -->

<p>Given two arrays <code>arr1</code> and <code>arr2</code>, the elements of <code>arr2</code> are distinct, and all elements in <code>arr2</code> are also in <code>arr1</code>.</p>

<p>Sort the elements of <code>arr1</code> such that the relative ordering of items in <code>arr1</code> are the same as in <code>arr2</code>. Elements that do not appear in <code>arr2</code> should be placed at the end of <code>arr1</code> in <strong>ascending</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
<strong>Output:</strong> [2,2,2,1,4,3,3,9,6,7,19]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
<strong>Output:</strong> [22,28,8,6,17,44]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= arr1[i], arr2[i] &lt;= 1000</code></li>
	<li>All the elements of <code>arr2</code> are <strong>distinct</strong>.</li>
	<li>Each&nbsp;<code>arr2[i]</code> is in <code>arr1</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Custom Sorting

First, we use a hash table $pos$ to record the position of each element in array $arr2$. Then, we map each element in array $arr1$ to a tuple $(pos.get(x, 1000 + x), x)$, and sort these tuples. Finally, we take out the second element of all tuples and return it.

The time complexity is $O(n \times \log n + m)$, and the space complexity is $O(n + m)$. Here, $n$ and $m$ are the lengths of arrays $arr1$ and $arr2$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {x: i for i, x in enumerate(arr2)}
        return sorted(arr1, key=lambda x: pos.get(x, 1000 + x))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Counting Sort

We can use the idea of counting sort. First, count the occurrence of each element in array $arr1$. Then, according to the order in array $arr2$, put the elements in $arr1$ into the answer array $ans$ according to their occurrence. Finally, we traverse all elements in $arr1$ and put the elements that do not appear in $arr2$ in ascending order at the end of the answer array $ans$.

The time complexity is $O(n + m)$, and the space complexity is $O(n)$. Where $n$ and $m$ are the lengths of arrays $arr1$ and $arr2$ respectively.

<!-- solution:start -->

#### Python3

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        ans = []
        for x in arr2:
            ans.extend([x] * cnt[x])
            cnt.pop(x)
        mi, mx = min(arr1), max(arr1)
        for x in range(mi, mx + 1):
            ans.extend([x] * cnt[x])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
