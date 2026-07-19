---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0624.Maximum%20Distance%20in%20Arrays/README_EN.md
tags:
    - Greedy
    - Array
---

<!-- problem:start -->

# [624. Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays)

## Description

<!-- description:start -->

<p>You are given <code>m</code> <code>arrays</code>, where each array is sorted in <strong>ascending order</strong>.</p>

<p>You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers <code>a</code> and <code>b</code> to be their absolute difference <code>|a - b|</code>.</p>

<p>Return <em>the maximum distance</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arrays = [[1,2,3],[4,5],[1,2,3]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arrays = [[1],[1]]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == arrays.length</code></li>
	<li><code>2 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arrays[i].length &lt;= 500</code></li>
	<li><code>-10<sup>4</sup> &lt;= arrays[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>arrays[i]</code> is sorted in <strong>ascending order</strong>.</li>
	<li>There will be at most <code>10<sup>5</sup></code> integers in all the arrays.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Maintain Maximum and Minimum Values

We notice that the maximum distance must be the distance between the maximum value in one array and the minimum value in another array. Therefore, we can maintain two variables $\textit{mi}$ and $\textit{mx}$, representing the minimum and maximum values of the arrays we have traversed. Initially, $\textit{mi}$ and $\textit{mx}$ are the first and last elements of the first array, respectively.

Next, we traverse from the second array. For each array, we first calculate the distance between the first element of the current array and $\textit{mx}$, and the distance between the last element of the current array and $\textit{mi}$. Then, we update the maximum distance. At the same time, we update $\textit{mi} = \min(\textit{mi}, \textit{arr}[0])$ and $\textit{mx} = \max(\textit{mx}, \textit{arr}[\textit{size} - 1])$.

After traversing all arrays, we get the maximum distance.

The time complexity is $O(m)$, where $m$ is the number of arrays. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        mi, mx = arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            a, b = abs(arr[0] - mx), abs(arr[-1] - mi)
            ans = max(ans, a, b)
            mi = min(mi, arr[0])
            mx = max(mx, arr[-1])
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
