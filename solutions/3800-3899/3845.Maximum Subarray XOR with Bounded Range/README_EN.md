---
comments: true
difficulty: Hard
rating: 2347
source: Weekly Contest 489 Q4
tags:
    - Bit Manipulation
    - Trie
    - Queue
    - Array
    - Prefix Sum
    - Sliding Window
    - Monotonic Queue
---

<!-- problem:start -->

# [3845. Maximum Subarray XOR with Bounded Range](https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range)

## Description

<!-- description:start -->

<p>You are given a non-negative integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>You must select a <strong><span data-keyword="subarray-nonempty">subarray</span></strong> of <code>nums</code> such that the <strong>difference</strong> between its <strong>maximum</strong> and <strong>minimum</strong> elements is at most <code>k</code>. The <strong>value</strong> of this subarray is the bitwise XOR of all elements in the subarray.</p>

<p>Return an integer denoting the <strong>maximum</strong> possible <strong>value</strong> of the selected subarray.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,5,6], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Select the subarray <code>[5, <u><strong>4, 5, 6</strong></u>]</code>.</li>
	<li>The difference between its maximum and minimum elements is <code>6 - 4 = 2 &lt;= k</code>.</li>
	<li>The value is <code>4 XOR 5 XOR 6 = 7</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,5,6], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Select the subarray <code>[5, 4, 5, <u><strong>6</strong></u>]</code>.</li>
	<li>The difference between its maximum and minimum elements is <code>6 - 6 = 0 &lt;= k</code>.</li>
	<li>The value is 6.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt; 2<sup>15</sup></code></li>
	<li><code>0 &lt;= k &lt; 2<sup>15</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> A subarray must satisfy $\max-\min \le k$ while maximizing its XOR. $n \le 4 \times 10^4$ and values lie below $2^{15}$.
>
> A subarray XOR is the XOR of two prefix XORs. For a fixed right end the legal left ends form a $\max-\min$ window, inside which we query the best prefix XOR.
>
> Monotonic deques shrink the window; a binary trie inserts and deletes prefix XORs and greedily takes the opposite bit.
>
> As the right end advances, the window and the trie slide together; each prefix enters and leaves once.

<!-- thinking:end -->
<!-- tabs:start -->

#### Python3

```python
class TrieNode:
    __slots__ = ("children", "count")

    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Solution:
    def maxXor(self, nums: List[int], k: int) -> int:
        root = TrieNode()

        def update(value: int, delta: int) -> None:
            cur = root
            for bit in range(14, -1, -1):
                b = (value >> bit) & 1
                if cur.children[b] is None:
                    cur.children[b] = TrieNode()
                cur = cur.children[b]
                cur.count += delta

        def get_max_xor(value: int) -> int:
            cur = root
            ans = 0
            for bit in range(14, -1, -1):
                b = (value >> bit) & 1
                opp = 1 - b
                if cur.children[opp] is not None and cur.children[opp].count > 0:
                    ans |= 1 << bit
                    cur = cur.children[opp]
                else:
                    cur = cur.children[b]
            return ans

        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] ^ x

        maxq, minq = deque(), deque()
        left = 0
        ans = 0
        update(prefix[0], 1)
        for right, x in enumerate(nums):
            while maxq and nums[maxq[-1]] <= x:
                maxq.pop()
            while minq and nums[minq[-1]] >= x:
                minq.pop()
            maxq.append(right)
            minq.append(right)
            while nums[maxq[0]] - nums[minq[0]] > k:
                if maxq[0] == left:
                    maxq.popleft()
                if minq[0] == left:
                    minq.popleft()
                update(prefix[left], -1)
                left += 1
            ans = max(ans, get_max_xor(prefix[right + 1]))
            update(prefix[right + 1], 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
