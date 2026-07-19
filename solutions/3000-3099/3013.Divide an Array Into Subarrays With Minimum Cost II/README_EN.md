---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3000-3099/3013.Divide%20an%20Array%20Into%20Subarrays%20With%20Minimum%20Cost%20II/README_EN.md
rating: 2540
source: Biweekly Contest 122 Q4
tags:
    - Array
    - Hash Table
    - Sliding Window
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3013. Divide an Array Into Subarrays With Minimum Cost II](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code> of length <code>n</code>, and two <strong>positive</strong> integers <code>k</code> and <code>dist</code>.</p>

<p>The <strong>cost</strong> of an array is the value of its <strong>first</strong> element. For example, the cost of <code>[1,2,3]</code> is <code>1</code> while the cost of <code>[3,4,1]</code> is <code>3</code>.</p>

<p>You need to divide <code>nums</code> into <code>k</code> <strong>disjoint contiguous </strong><span data-keyword="subarray-nonempty">subarrays</span>, such that the difference between the starting index of the <strong>second</strong> subarray and the starting index of the <code>kth</code> subarray should be <strong>less than or equal to</strong> <code>dist</code>. In other words, if you divide <code>nums</code> into the subarrays <code>nums[0..(i<sub>1</sub> - 1)], nums[i<sub>1</sub>..(i<sub>2</sub> - 1)], ..., nums[i<sub>k-1</sub>..(n - 1)]</code>, then <code>i<sub>k-1</sub> - i<sub>1</sub> &lt;= dist</code>.</p>

<p>Return <em>the <strong>minimum</strong> possible sum of the cost of these</em> <em>subarrays</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,6,4,2], k = 3, dist = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,1,2,2,2,1], k = 4, dist = 3
<strong>Output:</strong> 15
<strong>Explanation:</strong> The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between i<sub>k-1</sub> and i<sub>1</sub> is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,8,18,9], k = 3, dist = 1
<strong>Output:</strong> 36
<strong>Explanation:</strong> The best possible way to divide nums into 3 subarrays is: [10], [8], and [18,9]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between i<sub>k-1</sub> and i<sub>1</sub> is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>3 &lt;= k &lt;= n</code></li>
	<li><code>k - 2 &lt;= dist &lt;= n - 2</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Ordered Set

The problem requires us to divide the array $\textit{nums}$ into $k$ consecutive and non-overlapping subarrays, and the distance between the first element of the second subarray and the first element of the $k$-th subarray should not exceed $\textit{dist}$. This is equivalent to finding a subarray of size $\textit{dist}+1$ starting from the element at index $1$ in $\textit{nums}$, and calculating the sum of the smallest $k-1$ elements in it. We subtract $1$ from $k$, so we only need to find the sum of the smallest $k$ elements and add $\textit{nums}[0]$ to it.

We can use two ordered sets $\textit{l}$ and $\textit{r}$ to maintain the elements of the window of size $\textit{dist} + 1$. The set $\textit{l}$ maintains the smallest $k$ elements, while the set $\textit{r}$ maintains the remaining elements of the window. We maintain a variable $\textit{s}$ to represent the sum of $\textit{nums}[0]$ and the elements in $\textit{l}$. Initially, we add the sum of the first $\textit{dist}+2$ elements to $\textit{s}$ and add all elements with indices $[1, \textit{dist} + 1]$ to $\textit{l}$. If the size of $\textit{l}$ is greater than $k$, we repeatedly move the largest element from $\textit{l}$ to $\textit{r}$ until the size of $\textit{l}$ equals $k$, updating the value of $\textit{s}$ in the process.

At this point, the initial answer is $\textit{ans} = \textit{s}$.

Next, we traverse $\textit{nums}$ starting from $\textit{dist}+2$. For each element $\textit{nums}[i]$, we need to remove $\textit{nums}[i-\textit{dist}-1]$ from either $\textit{l}$ or $\textit{r}$, and then add $\textit{nums}[i]$ to either $\textit{l}$ or $\textit{r}$. If $\textit{nums}[i]$ is less than the largest element in $\textit{l}$, we add $\textit{nums}[i]$ to $\textit{l}$; otherwise, we add it to $\textit{r}$. If the size of $\textit{l}$ is less than $k$, we move the smallest element from $\textit{r}$ to $\textit{l}$ until the size of $\textit{l}$ equals $k$. If the size of $\textit{l}$ is greater than $k$, we move the largest element from $\textit{l}$ to $\textit{r}$ until the size of $\textit{l}$ equals $k$. During this process, we update the value of $\textit{s}$ and update $\textit{ans} = \min(\textit{ans}, \textit{s})$.

The final answer is $\textit{ans}$.

The time complexity is $O(n \times \log \textit{dist})$, and the space complexity is $O(\textit{dist})$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        def l2r():
            nonlocal s
            x = l.pop()
            s -= x
            r.add(x)

        def r2l():
            nonlocal s
            x = r.pop(0)
            l.add(x)
            s += x

        k -= 1
        s = sum(nums[: dist + 2])
        l = SortedList(nums[1 : dist + 2])
        r = SortedList()
        while len(l) > k:
            l2r()
        ans = s
        for i in range(dist + 2, len(nums)):
            x = nums[i - dist - 1]
            if x in l:
                l.remove(x)
                s -= x
            else:
                r.remove(x)
            y = nums[i]
            if y < l[-1]:
                l.add(y)
                s += y
            else:
                r.add(y)
            while len(l) < k:
                r2l()
            while len(l) > k:
                l2r()
            ans = min(ans, s)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
