---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3900-3999/3915.Maximum%20Sum%20of%20Alternating%20Subsequence%20With%20Distance%20at%20Least%20K/README_EN.md
rating: 2288
source: Weekly Contest 499 Q4
tags:
    - Segment Tree
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [3915. Maximum Sum of Alternating Subsequence With Distance at Least K](https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>Pick a <strong><span data-keyword="subsequence-sequence">subsequence</span></strong> with indices <code>0 &lt;= i<sub>1</sub> &lt; i<sub>2</sub> &lt; ... &lt; i<sub>m</sub> &lt; n</code> such that:</p>

<ul>
	<li>For every <code>1 &lt;= t &lt; m</code>, <code>i<sub>t+1</sub> - i<sub>t</sub> &gt;= k</code>.</li>
	<li>The selected values form a <strong>strictly alternating</strong> sequence. In other words, either:
	<ul>
		<li><code>nums[i<sub>1</sub>] &lt; nums[i<sub>2</sub>] &gt; nums[i<sub>3</sub>] &lt; ...</code>, or</li>
		<li><code>nums[i<sub>1</sub>] &gt; nums[i<sub>2</sub>] &lt; nums[i<sub>3</sub>] &gt; ...</code></li>
	</ul>
	</li>
</ul>

<p>A <strong>subsequence</strong> of length 1 is also considered <strong>strictly</strong> alternating. The score of a <strong>valid</strong> subsequence is the <strong>sum</strong> of its selected values.</p>

<p>Return an integer denoting the <strong>maximum</strong> possible <strong>score</strong> of a valid subsequence.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>An optimal choice is indices <code>[0, 2]</code>, which gives values <code>[5, 2]</code>.</p>

<ul>
	<li>The distance condition holds because <code>2 - 0 = 2 &gt;= k</code>.</li>
	<li>The values are strictly alternating because <code>5 &gt; 2</code>.</li>
</ul>

<p>The score is <code>5 + 2 = 7</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,5,4,2,4], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong></p>

<p>An optimal choice is indices <code>[0, 1, 3, 4]</code>, which gives values <code>[3, 5, 2, 4]</code>.</p>

<ul>
	<li>The distance condition holds because each pair of consecutive chosen indices differs by at least <code>k = 1</code>.</li>
	<li>The values are strictly alternating since <code>3 &lt; 5 &gt; 2 &lt; 4</code>.</li>
</ul>

<p>The score is <code>3 + 5 + 2 + 4 = 14</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The only valid subsequence is <code>[5]</code>. A subsequence with 1 element is always strictly alternating, so the score is 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Dynamic Programming + Binary Indexed Tree

**State Definition**

Let $f[i][0]$ denote the maximum sum of a valid subsequence ending at index $i$ where the last element is a **valley** (the next element must be larger to maintain alternation), and $f[i][1]$ denote the maximum sum where the last element is a **peak** (the next element must be smaller).

**Transitions**

When transitioning, we enumerate a predecessor index $j$ satisfying $j \leq i - k$:

- State $f[i][0]$ (valley): transitions from $f[j][1]$, requiring $\text{nums}[j] > \text{nums}[i]$, i.e., query the maximum $f[\cdot][1]$ over the value range $(\text{nums}[i],\ +\infty)$:

$$f[i][0] = \text{nums}[i] + \max\!\left(0,\ \max_{\substack{j \leq i-k \\ \text{nums}[j] > \text{nums}[i]}} f[j][1]\right)$$

- State $f[i][1]$ (peak): transitions from $f[j][0]$, requiring $\text{nums}[j] < \text{nums}[i]$, i.e., query the maximum $f[\cdot][0]$ over the value range $[1,\ \text{nums}[i]-1]$:

$$f[i][1] = \text{nums}[i] + \max\!\left(0,\ \max_{\substack{j \leq i-k \\ \text{nums}[j] < \text{nums}[i]}} f[j][0]\right)$$

The final answer is $\max_{0 \leq i < n}\max(f[i][0],\ f[i][1])$.

**Optimization**

The transitions involve dynamic prefix/suffix maximum queries over a value domain, which can be maintained efficiently with two **Binary Indexed Trees (BITs)**:

- BIT $\text{bit}_0$: indexed by value, maintains the prefix maximum of $f[\cdot][0]$, used to query cases where $\text{nums}[j] < \text{nums}[i]$.
- BIT $\text{bit}_1$: indexed by $M + 1 - \text{val}$ (reversed, where $M = \max(\text{nums})$ ), maintains the prefix maximum of $f[\cdot][1]$, equivalent to a suffix maximum over the value domain, used to query cases where $\text{nums}[j] > \text{nums}[i]$.

To ensure only indices $j \leq i - k$ participate in transitions, when processing index $i$, we insert the state of index $i - k$ into the BITs using a sliding pointer.

The time complexity is $O(n \log M)$ and the space complexity is $O(M)$, where $n$ is the length of the array and $M = \max(\text{nums})$.

<!-- tabs:start -->

#### Python3

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, index: int, val: int) -> None:
        while index <= self.n:
            self.tree[index] = max(self.tree[index], val)
            index += index & (-index)  # 往后更新

    def preSum(self, pos):
        # 按照预期的方式求前缀最大值
        ans = 0
        while pos >= 1:
            ans = max(ans, self.tree[pos])
            pos -= pos & (-pos)
        return ans

class Solution:
    def maxAlternatingSum(self, nums: list[int], k: int) -> int:
        stl = sorted(set(nums))  # 将nums中不同的数字进行排序
        rank = {
            v: i + 1 for i, v in enumerate(stl)
        }  # 将nums中的值快速转换成stl中的索引
        fwt0 = FenwickTree(len(stl))
        fwt1 = FenwickTree(len(stl))

        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        res = nums[0]
        for i in range(n):
            dp[i][0] = dp[i][1] = nums[i]
            if i >= k:
                indx = rank[nums[i]]  # 找到nums[i]在stl中的索引
                dp[i][1] = max(
                    dp[i][1], fwt0.preSum(indx - 1) + nums[i]
                )  # indx-1即表示小于nums[i]的部分
                dp[i][0] = max(
                    dp[i][0], fwt1.preSum(len(stl) - indx) + nums[i]
                )  # len(stl)-indx即表示在倒序列表中大于nums[i]的部分

            if i - k + 1 >= 0:
                indx = rank[nums[i - k + 1]]
                fwt0.update(indx, dp[i - k + 1][0])  # 在正序列表中更新i-k+1位置的值
                fwt1.update(
                    len(stl) - indx + 1, dp[i - k + 1][1]
                )  # 在倒序列表中更新i-k+1位置的值

            res = max(res, dp[i][0], dp[i][1])  # 更新答案

        return res
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
