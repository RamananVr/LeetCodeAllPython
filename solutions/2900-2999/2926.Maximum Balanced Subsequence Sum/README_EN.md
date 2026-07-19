---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2900-2999/2926.Maximum%20Balanced%20Subsequence%20Sum/README_EN.md
rating: 2448
source: Weekly Contest 370 Q4
tags:
    - Binary Indexed Tree
    - Segment Tree
    - Array
    - Binary Search
    - Dynamic Programming
---

<!-- problem:start -->

# [2926. Maximum Balanced Subsequence Sum](https://leetcode.com/problems/maximum-balanced-subsequence-sum)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>.</p>

<p>A <strong>subsequence</strong> of <code>nums</code> having length <code>k</code> and consisting of <strong>indices</strong> <code>i<sub>0</sub>&nbsp;&lt;&nbsp;i<sub>1</sub> &lt;&nbsp;... &lt; i<sub>k-1</sub></code> is <strong>balanced</strong> if the following holds:</p>

<ul>
	<li><code>nums[i<sub>j</sub>] - nums[i<sub>j-1</sub>] &gt;= i<sub>j</sub> - i<sub>j-1</sub></code>, for every <code>j</code> in the range <code>[1, k - 1]</code>.</li>
</ul>

<p>A <strong>subsequence</strong> of <code>nums</code> having length <code>1</code> is considered balanced.</p>

<p>Return <em>an integer denoting the <strong>maximum</strong> possible <strong>sum of elements</strong> in a <strong>balanced</strong> subsequence of </em><code>nums</code>.</p>

<p>A <strong>subsequence</strong> of an array is a new <strong>non-empty</strong> array that is formed from the original array by deleting some (<strong>possibly none</strong>) of the elements without disturbing the relative positions of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,5,6]
<strong>Output:</strong> 14
<strong>Explanation:</strong> In this example, the subsequence [3,5,6] consisting of indices 0, 2, and 3 can be selected.
nums[2] - nums[0] &gt;= 2 - 0.
nums[3] - nums[2] &gt;= 3 - 2.
Hence, it is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
The subsequence consisting of indices 1, 2, and 3 is also valid.
It can be shown that it is not possible to get a balanced subsequence with a sum greater than 14.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,-1,-3,8]
<strong>Output:</strong> 13
<strong>Explanation:</strong> In this example, the subsequence [5,8] consisting of indices 0 and 3 can be selected.
nums[3] - nums[0] &gt;= 3 - 0.
Hence, it is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
It can be shown that it is not possible to get a balanced subsequence with a sum greater than 13.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,-1]
<strong>Output:</strong> -1
<strong>Explanation:</strong> In this example, the subsequence [-1] can be selected.
It is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming + Binary Indexed Tree

According to the problem description, we can transform the inequality $nums[i] - nums[j] \ge i - j$ into $nums[i] - i \ge nums[j] - j$. Therefore, we consider defining a new array $arr$, where $arr[i] = nums[i] - i$. A balanced subsequence satisfies that for any $j < i$, $arr[j] \le arr[i]$. The problem is transformed into selecting an increasing subsequence in $arr$ such that the corresponding sum in $nums$ is maximized.

Suppose $i$ is the index of the last element in the subsequence, then we consider the index $j$ of the second to last element in the subsequence. If $arr[j] \le arr[i]$, we can consider whether to add $j$ to the subsequence.

Therefore, we define $f[i]$ as the maximum sum of $nums$ when the index of the last element in the subsequence is $i$. The answer is $\max_{i=0}^{n-1} f[i]$.

The state transition equation is:

$$
f[i] = \max(\max_{j=0}^{i-1} f[j], 0) + nums[i]
$$

where $j$ satisfies $arr[j] \le arr[i]$.

We can use a Binary Indexed Tree to maintain the maximum value of the prefix, i.e., for each $arr[i]$, we maintain the maximum value of $f[i]$ in the prefix $arr[0..i]$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class BinaryIndexedTree:
    def __init__(self, n: int):
        self.n = n
        self.c = [-inf] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] = max(self.c[x], v)
            x += x & -x

    def query(self, x: int) -> int:
        mx = -inf
        while x:
            mx = max(mx, self.c[x])
            x -= x & -x
        return mx

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        arr = [x - i for i, x in enumerate(nums)]
        s = sorted(set(arr))
        tree = BinaryIndexedTree(len(s))
        for i, x in enumerate(nums):
            j = bisect_left(s, x - i) + 1
            v = max(tree.query(j), 0) + x
            tree.update(j, v)
        return tree.query(len(s))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
