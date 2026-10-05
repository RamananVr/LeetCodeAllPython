---
comments: true
difficulty: Medium
tags:
    - Array
    - Divide and Conquer
    - Quickselect
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>largest element in the array</em>.</p>

<p>Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>Can you solve it without sorting?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,1,5,6,4], k = 2
<strong>Output:</strong> 5
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3,1,2,4,5,5,6], k = 4
<strong>Output:</strong> 4
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Quick Select

<!-- thinking:start -->

> **Thinking**
>
> Full sorting finds the $k$-th largest but orders every other position as well. Quickselect only needs the side that contains that rank.
>
> After partitioning around a pivot we recurse only into the interval that holds the target. The implementation converts “ $k$-th largest” into “ $(n-k)$-th smallest”.

<!-- thinking:end -->

Quick Select is an algorithm for finding the $k^{th}$ largest or smallest element in an unsorted array. Its basic idea is to select a pivot element each time, dividing the array into two parts: one part contains elements smaller than the pivot, and the other part contains elements larger than the pivot. Then, based on the position of the pivot, it decides whether to continue the search on the left or right side until the $k^{th}$ largest element is found.

The time complexity is $O(n)$, and the space complexity is $O(\log n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(l: int, r: int) -> int:
            if l == r:
                return nums[l]
            i, j = l - 1, r + 1
            x = nums[(l + r) >> 1]
            while i < j:
                while 1:
                    i += 1
                    if nums[i] >= x:
                        break
                while 1:
                    j -= 1
                    if nums[j] <= x:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if j < k:
                return quick_sort(j + 1, r)
            return quick_sort(l, j)

        n = len(nums)
        k = n - k
        return quick_sort(0, n - 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Priority Queue (Min Heap)

<!-- thinking:start -->

> **Thinking**
>
> Quickselect is linear on average but quadratic in the worst case. A min-heap of size $k$ is enough if we only need that order statistic.
>
> After one pass the heap stores the $k$ largest values and its top is the answer, in $O(n\log k)$ time.

<!-- thinking:end -->

We can maintain a min heap $\textit{minQ}$ of size $k$, and then iterate through the array $\textit{nums}$, adding each element to the min heap. When the size of the min heap exceeds $k$, we pop the top element of the heap. This way, the final $k$ elements in the min heap are the $k$ largest elements in the array, and the top element of the heap is the $k^{th}$ largest element.

The time complexity is $O(n\log k)$, and the space complexity is $O(k)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 3: Counting Sort

<!-- thinking:start -->

> **Thinking**
>
> The heap still pays a log factor. With a bounded value range we count frequencies, then walk values from high to low until $k$ occurrences are gathered.
>
> Time is linear in $n$ plus the value range, with no comparison sort.

<!-- thinking:end -->

We can use the idea of counting sort, counting the occurrence of each element in the array $\textit{nums}$ and recording it in a hash table $\textit{cnt}$. Then, we iterate over the elements $i$ from largest to smallest, subtracting the occurrence count $\textit{cnt}[i]$ each time, until $k$ is less than or equal to $0$. At this point, the element $i$ is the $k^{th}$ largest element in the array.

The time complexity is $O(n + m)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$, and $m$ is the maximum value among the elements in $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        for i in count(max(cnt), -1):
            k -= cnt[i]
            if k <= 0:
                return i
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
