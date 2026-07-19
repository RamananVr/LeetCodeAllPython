---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1187.Make%20Array%20Strictly%20Increasing/README_EN.md
rating: 2315
source: Weekly Contest 153 Q4
tags:
    - Array
    - Binary Search
    - Dynamic Programming
    - Sorting
---

<!-- problem:start -->

# [1187. Make Array Strictly Increasing](https://leetcode.com/problems/make-array-strictly-increasing)

## Description

<!-- description:start -->

<p>Given two integer arrays&nbsp;<code>arr1</code> and <code>arr2</code>, return the minimum number of operations (possibly zero) needed&nbsp;to make <code>arr1</code> strictly increasing.</p>

<p>In one operation, you can choose two indices&nbsp;<code>0 &lt;=&nbsp;i &lt; arr1.length</code>&nbsp;and&nbsp;<code>0 &lt;= j &lt; arr2.length</code>&nbsp;and do the assignment&nbsp;<code>arr1[i] = arr2[j]</code>.</p>

<p>If there is no way to make&nbsp;<code>arr1</code>&nbsp;strictly increasing,&nbsp;return&nbsp;<code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Replace <code>5</code> with <code>2</code>, then <code>arr1 = [1, 2, 3, 6, 7]</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [4,3,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Replace <code>5</code> with <code>3</code> and then replace <code>3</code> with <code>4</code>. <code>arr1 = [1, 3, 4, 6, 7]</code>.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong> You can&#39;t make <code>arr1</code> strictly increasing.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 2000</code></li>
	<li><code>0 &lt;= arr1[i], arr2[i] &lt;= 10^9</code></li>
</ul>

<p>&nbsp;</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming

We define $f[i]$ as the minimum number of operations to convert $arr1[0,..,i]$ into a strictly increasing array, and $arr1[i]$ is not replaced. Therefore, we set two sentinels $-\infty$ and $\infty$ at the beginning and end of $arr1$. The last number is definitely not replaced, so $f[n-1]$ is the answer. We initialize $f[0]=0$, and the rest $f[i]=\infty$.

Next, we sort the array $arr2$ and remove duplicates for easy binary search.

For $i=1,..,n-1$, we consider whether $arr1[i-1]$ is replaced. If $arr1[i-1] \lt arr1[i]$, then $f[i]$ can be transferred from $f[i-1]$, that is, $f[i] = f[i-1]$. Then, we consider the case where $arr[i-1]$ is replaced. Obviously, $arr[i-1]$ should be replaced with a number as large as possible and less than $arr[i]$. We perform a binary search in the array $arr2$ and find the first index $j$ that is greater than or equal to $arr[i]$. Then we enumerate the number of replacements in the range $k \in [1, min(i-1, j)]$. If $arr[i-k-1] \lt arr2[j-k]$, then $f[i]$ can be transferred from $f[i-k-1]$, that is, $f[i] = \min(f[i], f[i-k-1] + k)$.

Finally, if $f[n-1] \geq \infty$, it means that it cannot be converted into a strictly increasing array, return $-1$, otherwise return $f[n-1]$.

The time complexity is $(n \times (\log m + \min(m, n)))$, and the space complexity is $O(n)$. Here, $n$ is the length of $arr1$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        m = 0
        for x in arr2:
            if m == 0 or x != arr2[m - 1]:
                arr2[m] = x
                m += 1
        arr2 = arr2[:m]
        arr = [-inf] + arr1 + [inf]
        n = len(arr)
        f = [inf] * n
        f[0] = 0
        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                f[i] = f[i - 1]
            j = bisect_left(arr2, arr[i])
            for k in range(1, min(i - 1, j) + 1):
                if arr[i - k - 1] < arr2[j - k]:
                    f[i] = min(f[i], f[i - k - 1] + k)
        return -1 if f[n - 1] >= inf else f[n - 1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
