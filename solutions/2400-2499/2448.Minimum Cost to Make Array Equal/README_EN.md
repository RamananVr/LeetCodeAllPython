---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2400-2499/2448.Minimum%20Cost%20to%20Make%20Array%20Equal/README_EN.md
rating: 2005
source: Weekly Contest 316 Q3
tags:
    - Greedy
    - Array
    - Binary Search
    - Prefix Sum
    - Sorting
---

<!-- problem:start -->

# [2448. Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> arrays <code>nums</code> and <code>cost</code> consisting each of <code>n</code> <strong>positive</strong> integers.</p>

<p>You can do the following operation <strong>any</strong> number of times:</p>

<ul>
	<li>Increase or decrease <strong>any</strong> element of the array <code>nums</code> by <code>1</code>.</li>
</ul>

<p>The cost of doing one operation on the <code>i<sup>th</sup></code> element is <code>cost[i]</code>.</p>

<p>Return <em>the <strong>minimum</strong> total cost such that all the elements of the array </em><code>nums</code><em> become <strong>equal</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,2], cost = [2,3,1,14]
<strong>Output:</strong> 8
<strong>Explanation:</strong> We can make all the elements equal to 2 in the following way:
- Increase the 0<sup>th</sup> element one time. The cost is 2.
- Decrease the 1<sup><span style="font-size: 10.8333px;">st</span></sup> element one time. The cost is 3.
- Decrease the 2<sup>nd</sup> element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,2,2,2,2], cost = [4,2,8,1,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All the elements are already equal, so no operations are needed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length == cost.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], cost[i] &lt;= 10<sup>6</sup></code></li>
	<li>Test cases are generated in a way that the output doesn&#39;t exceed&nbsp;2<sup>53</sup>-1</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sum + Sorting + Enumeration

Let's denote the elements of the array `nums` as $a_1, a_2, \cdots, a_n$ and the elements of the array `cost` as $b_1, b_2, \cdots, b_n$. We can assume that $a_1 \leq a_2 \leq \cdots \leq a_n$, i.e., the array `nums` is sorted in ascending order.

Suppose we change all elements in the array `nums` to $x$, then the total cost we need is:

$$
\begin{aligned}
\sum_{i=1}^{n} \left | a_i-x \right | b_i  &= \sum_{i=1}^{k} (x-a_i)b_i + \sum_{i=k+1}^{n} (a_i-x)b_i \\
&= x\sum_{i=1}^{k} b_i - \sum_{i=1}^{k} a_ib_i + \sum_{i=k+1}^{n}a_ib_i - x\sum_{i=k+1}^{n}b_i
\end{aligned}
$$

where $k$ is the number of elements in $a_1, a_2, \cdots, a_n$ that are less than or equal to $x$.

We can use the prefix sum method to calculate $\sum_{i=1}^{k} b_i$ and $\sum_{i=1}^{k} a_ib_i$, as well as $\sum_{i=k+1}^{n}a_ib_i$ and $\sum_{i=k+1}^{n}b_i$.

Then we enumerate $x$, calculate the above four prefix sums, get the total cost mentioned above, and take the minimum value.

The time complexity is $O(n\times \log n)$, where $n$ is the length of the array `nums`. The main time complexity comes from sorting.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        n = len(arr)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        for i in range(1, n + 1):
            a, b = arr[i - 1]
            f[i] = f[i - 1] + a * b
            g[i] = g[i - 1] + b
        ans = inf
        for i in range(1, n + 1):
            a = arr[i - 1][0]
            l = a * g[i - 1] - f[i - 1]
            r = f[n] - f[i] - a * (g[n] - g[i])
            ans = min(ans, l + r)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Sorting + Median

We can also consider $b_i$ as the occurrence times of $a_i$, then the index of the median is $\frac{\sum_{i=1}^{n} b_i}{2}$. Changing all numbers to the median is definitely optimal.

The time complexity is $O(n\times \log n)$, where $n$ is the length of the array `nums`. The main time complexity comes from sorting.

Similar problems:

- [296. Best Meeting Point](https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0296.Best%20Meeting%20Point/README_EN.md)
- [462. Minimum Moves to Equal Array Elements II](https://github.com/doocs/leetcode/blob/main/solution/0400-0499/0462.Minimum%20Moves%20to%20Equal%20Array%20Elements%20II/README_EN.md)

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        mid = sum(cost) // 2
        s = 0
        for x, c in arr:
            s += c
            if s > mid:
                return sum(abs(v - x) * c for v, c in arr)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
