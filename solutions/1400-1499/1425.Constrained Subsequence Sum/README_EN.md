---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1400-1499/1425.Constrained%20Subsequence%20Sum/README_EN.md
rating: 2032
source: Weekly Contest 186 Q4
tags:
    - Queue
    - Array
    - Dynamic Programming
    - Sliding Window
    - Monotonic Queue
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1425. Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return the maximum sum of a <strong>non-empty</strong> subsequence of that array such that for every two <strong>consecutive</strong> integers in the subsequence, <code>nums[i]</code> and <code>nums[j]</code>, where <code>i &lt; j</code>, the condition <code>j - i &lt;= k</code> is satisfied.</p>

<p>A <em>subsequence</em> of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,2,-10,5,20], k = 2
<strong>Output:</strong> 37
<b>Explanation:</b> The subsequence is [10, 2, 5, 20].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,-2,-3], k = 1
<strong>Output:</strong> -1
<b>Explanation:</b> The subsequence must be non-empty, so we choose the largest number.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,-2,-10,-5,20], k = 2
<strong>Output:</strong> 23
<b>Explanation:</b> The subsequence is [10, -2, -5, 20].
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

### Solution 1: Dynamic Programming + Monotonic Queue

We define $f[i]$ to represent the maximum sum of the subsequence ending at $\textit{nums}[i]$ that meets the conditions. Initially, $f[i] = 0$, and the answer is $\max_{0 \leq i \lt n} f(i)$.

We notice that the problem requires us to maintain the maximum value of a sliding window, which is a typical application scenario for a monotonic queue. We can use a monotonic queue to optimize the dynamic programming transition.

We maintain a monotonic queue $q$ that is decreasing from the front to the back, storing the indices $i$. Initially, we add a sentinel $0$ to the queue.

We traverse $i$ from $0$ to $n - 1$. For each $i$, we perform the following operations:

- If the front element $q[0]$ satisfies $i - q[0] > k$, it means the front element is no longer within the sliding window, and we need to remove the front element from the queue;
- Then, we calculate $f[i] = \max(0, f[q[0]]) + \textit{nums}[i]$, which means we add $\textit{nums}[i]$ to the sliding window to get the maximum subsequence sum;
- Next, we update the answer $\textit{ans} = \max(\textit{ans}, f[i])$;
- Finally, we add $i$ to the back of the queue and maintain the monotonicity of the queue. If $f[q[\textit{back}]] \leq f[i]$, we need to remove the back element until the queue is empty or $f[q[\textit{back}]] > f[i]$.

The final answer is $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque([0])
        n = len(nums)
        f = [0] * n
        ans = -inf
        for i, x in enumerate(nums):
            while i - q[0] > k:
                q.popleft()
            f[i] = max(0, f[q[0]]) + x
            ans = max(ans, f[i])
            while q and f[q[-1]] <= f[i]:
                q.pop()
            q.append(i)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
