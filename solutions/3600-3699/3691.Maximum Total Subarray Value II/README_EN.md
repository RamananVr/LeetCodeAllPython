---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3600-3699/3691.Maximum%20Total%20Subarray%20Value%20II/README_EN.md
rating: 2469
source: Weekly Contest 468 Q4
tags:
    - Greedy
    - Segment Tree
    - Array
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [3691. Maximum Total Subarray Value II](https://leetcode.com/problems/maximum-total-subarray-value-ii)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>You must select <strong>exactly</strong> <code>k</code> <strong>distinct</strong> <span data-keyword="subarray-nonempty">subarrays</span> <code>nums[l..r]</code> of <code>nums</code>. Subarrays may overlap, but the exact same subarray (same <code>l</code> and <code>r</code>) <strong>cannot</strong> be chosen more than once.</p>

<p>The <strong>value</strong> of a subarray <code>nums[l..r]</code> is defined as: <code>max(nums[l..r]) - min(nums[l..r])</code>.</p>

<p>The <strong>total value</strong> is the sum of the <strong>values</strong> of all chosen subarrays.</p>

<p>Return the <strong>maximum</strong> possible total value you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal approach is:</p>

<ul>
	<li>Choose <code>nums[0..1] = [1, 3]</code>. The maximum is 3 and the minimum is 1, giving a value of <code>3 - 1 = 2</code>.</li>
	<li>Choose <code>nums[0..2] = [1, 3, 2]</code>. The maximum is still 3 and the minimum is still 1, so the value is also <code>3 - 1 = 2</code>.</li>
</ul>

<p>Adding these gives <code>2 + 2 = 4</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,2,5,1], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>One optimal approach is:</p>

<ul>
	<li>Choose <code>nums[0..3] = [4, 2, 5, 1]</code>. The maximum is 5 and the minimum is 1, giving a value of <code>5 - 1 = 4</code>.</li>
	<li>Choose <code>nums[1..3] = [2, 5, 1]</code>. The maximum is 5 and the minimum is 1, so the value is also <code>4</code>.</li>
	<li>Choose <code>nums[2..3] = [5, 1]</code>. The maximum is 5 and the minimum is 1, so the value is again <code>4</code>.</li>
</ul>

<p>Adding these gives <code>4 + 4 + 4 = 12</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 5 * 10<sup>​​​​​​​4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(10<sup>5</sup>, n * (n + 1) / 2)</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Method 1: Sparse Table (ST) + Priority Queue (Max-Heap)

Consider enumerating the left boundary $l$ of the subarray. As the right boundary $r$ moves to the right, the value of the subarray $\textit{nums}[l..r]$ increases monotonically. This is because the maximum value within the interval can only increase (or remain unchanged), while the minimum value can only decrease (or remain unchanged). Thus, their difference, $\max(\textit{nums}[l..r]) - \min(\textit{nums}[l..r])$, possesses a monotonically non-decreasing property.

This implies that for each fixed left endpoint $l$, we have a monotonically increasing sequence of length $n - l$, where the $i$-th element represents the value of $\textit{nums}[l..l+i]$. The problem then transforms into: **Given $n$ monotonically increasing sequences, find the sum of the top $k$ largest elements across all sequences.**

Since the last element of each sequence (i.e., when $r = n - 1$) is the maximum value of that sequence, we can utilize a **max-heap (priority queue)** to filter them efficiently:

1. **Initialization**: Push the last element of each sequence (where $r = n - 1$) along with its coordinates, represented as $(val, l, n - 1)$, into the max-heap.
2. **Iterative Greedy Choice**: Repeat the operation $k$ times. In each iteration, pop the top element $(val, l, r)$ from the heap and accumulate $val$ into the total answer. If $r > l$, it indicates that there are still smaller, next-largest values remaining in this sequence. We then compute the value of the previous element in the same sequence, $(l, r - 1)$, and push it back into the heap.
3. **Range Minimum/Maximum Query Optimization**: To query both the maximum and minimum values of any subarray $[l, r]$ in $\mathcal{O}(1)$ time, we can precompute a **Sparse Table (ST)**.

The time complexity is $\mathcal{O}(n \log n + k \log n)$, and the space Complexity is $\mathcal{O}(n \log n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class SparseTableRMQ:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.max_log = self.n.bit_length() + 1
        self.f_max = [[0] * self.max_log for _ in range(self.n)]
        self.f_min = [[0] * self.max_log for _ in range(self.n)]

        self.lg = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.lg[i] = self.lg[i >> 1] + 1

        for i in range(self.n):
            self.f_max[i][0] = data[i]
            self.f_min[i][0] = data[i]

        for j in range(1, self.max_log):
            for i in range(self.n - (1 << j) + 1):
                self.f_max[i][j] = max(
                    self.f_max[i][j - 1], self.f_max[i + (1 << (j - 1))][j - 1]
                )
                self.f_min[i][j] = min(
                    self.f_min[i][j - 1], self.f_min[i + (1 << (j - 1))][j - 1]
                )

    def query_max(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return max(self.f_max[l][k], self.f_max[r - (1 << k) + 1][k])

    def query_min(self, l: int, r: int) -> int:
        k = self.lg[r - l + 1]
        return min(self.f_min[l][k], self.f_min[r - (1 << k) + 1][k])

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        st = SparseTableRMQ(nums)
        pq = []
        for l in range(n):
            val = st.query_max(l, n - 1) - st.query_min(l, n - 1)
            heappush(pq, (-val, l, n - 1))

        ans = 0
        for _ in range(k):
            val, l, r = heappop(pq)
            ans += -val
            if r > l:
                val = st.query_max(l, r - 1) - st.query_min(l, r - 1)
                heappush(pq, (-val, l, r - 1))
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
