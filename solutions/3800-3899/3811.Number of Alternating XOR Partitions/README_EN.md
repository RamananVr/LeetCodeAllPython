---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3800-3899/3811.Number%20of%20Alternating%20XOR%20Partitions/README_EN.md
rating: 2005
source: Biweekly Contest 174 Q3
tags:
    - Bit Manipulation
    - Array
    - Hash Table
    - Dynamic Programming
---

<!-- problem:start -->

# [3811. Number of Alternating XOR Partitions](https://leetcode.com/problems/number-of-alternating-xor-partitions)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> and two <strong>distinct</strong> integers <code>target1</code> and <code>target2</code>.</p>

<p>A <strong>partition</strong> of <code>nums</code> splits it into one or more <strong>contiguous, non-empty</strong> blocks that cover the entire array without overlap.</p>

<p>A partition is <strong>valid</strong> if the <strong>bitwise XOR</strong> of elements in its blocks <strong>alternates</strong> between <code>target1</code> and <code>target2</code>, starting with <code>target1</code>.</p>

<p>Formally, for blocks <code>b1</code>, <code>b2</code>, &hellip;:</p>

<ul>
	<li><code>XOR(b1) = target1</code></li>
	<li><code>XOR(b2) = target2</code> (if it exists)</li>
	<li><code>XOR(b3) = target1</code>, and so on.</li>
</ul>

<p>Return the number of valid partitions of <code>nums</code>, modulo <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note:</strong> A single block is valid if its <strong>XOR</strong> equals <code>target1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,1,4], target1 = 1, target2 = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li>The XOR of <code>[2, 3]</code> is 1, which matches <code>target1</code>.</li>
	<li>The XOR of the remaining block <code>[1, 4]</code> is 5, which matches <code>target2</code>.</li>
	<li>This is the only valid alternating partition, so the answer is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,0,0], target1 = 1, target2 = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><strong>​​​​​​​</strong>The XOR of <code>[1, 0, 0]</code> is 1, which matches <code>target1</code>.</li>
	<li>The XOR of <code>[1]</code> and <code>[0, 0]</code> are 1 and 0, matching <code>target1</code> and <code>target2</code>.</li>
	<li>The XOR of <code>[1, 0]</code> and <code>[0]</code> are 1 and 0, matching <code>target1</code> and <code>target2</code>.</li>
	<li>Thus, the answer is 3.​​​​​​​</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [7], target1 = 1, target2 = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The XOR of <code>[7]</code> is 7, which does not match <code>target1</code>, so no valid partition exists.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i], target1, target2 &lt;= 10<sup>5</sup></code></li>
	<li><code>target1 != target2</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Recurrence

We define two hash tables $\textit{cnt1}$ and $\textit{cnt2}$, where $\textit{cnt1}[x]$ represents the number of partition schemes where the bitwise XOR result is $x$ and the partition ends with $\textit{target1}$, while $\textit{cnt2}[x]$ represents the number of partition schemes where the bitwise XOR result is $x$ and the partition ends with $\textit{target2}$. Initially, $\textit{cnt2}[0] = 1$, representing an empty partition.

We use the variable $\textit{pre}$ to record the bitwise XOR result of the current prefix, and the variable $\textit{ans}$ to record the final answer. Then we traverse the array $\textit{nums}$. For each element $x$, we update $\textit{pre}$ and calculate:

$$
a = \textit{cnt2}[\textit{pre} \oplus \textit{target1}]
$$

$$
b = \textit{cnt1}[\textit{pre} \oplus \textit{target2}]
$$

Then we update the answer:

$$
\textit{ans} = (a + b) \mod (10^9 + 7)
$$

Next, we update the hash tables:

$$
\textit{cnt1}[\textit{pre}] = (\textit{cnt1}[\textit{pre}] + a) \mod (10^9 + 7)
$$

$$
\textit{cnt2}[\textit{pre}] = (\textit{cnt2}[\textit{pre}] + b) \mod (10^9 + 7)
$$

Finally, we return $\textit{ans}$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        cnt2[0] = 1
        ans = pre = 0
        mod = 10**9 + 7
        for x in nums:
            pre ^= x
            a = cnt2[pre ^ target1]
            b = cnt1[pre ^ target2]
            ans = (a + b) % mod
            cnt1[pre] = (cnt1[pre] + a) % mod
            cnt2[pre] = (cnt2[pre] + b) % mod
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
