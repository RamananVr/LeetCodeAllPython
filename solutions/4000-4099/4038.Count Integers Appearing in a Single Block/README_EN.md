---
comments: true
difficulty: Easy
rating: 1165
source: Weekly Contest 517 Q1
---

<!-- problem:start -->

# [4038. Count Integers Appearing in a Single Block](https://leetcode.com/problems/count-integers-appearing-in-a-single-block)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code>.</p>

<p>An integer <code>x</code> is <strong>special</strong> if all occurrences of <code>x</code> in <code>nums</code> appear in a single <strong>contiguous</strong> block.</p>

<p>Return the number of <strong>distinct</strong> special integers in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>1 appears at indices 0 and 3, forming two separate blocks, so it is not special.</li>
	<li>2 appears in a single contiguous block at indices <code>[1, 2]</code>, so it is special.</li>
</ul>

<p>Therefore, there is one special integer.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,3,1,2,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>3 appears in a single contiguous block at indices <code>[0, 1]</code>, so it is special.</li>
	<li>1 appears at indices 2 and 5, forming two separate blocks, so it is not special.</li>
	<li>2 appears in a single contiguous block at indices <code>[3, 4]</code>, so it is special.</li>
</ul>

<p>Therefore, there are two special integers.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Count the Blocks of Each Integer

<!-- thinking:start -->

> **Thinking**
>
> A special integer is one that forms exactly one contiguous equal block. Collecting every index of each value just to test contiguity would store extra lists.
>
> A scan increments a counter at the start of each block; afterwards we count how many values have counter $1$.
>
> The universe has size $100$, so a frequency table suffices.

<!-- thinking:end -->

Call each maximal run of consecutive equal elements a **block**. An integer $x$ is special if and only if it forms exactly one block.

So we traverse the array, and whenever $i = 0$ or $\textit{nums}[i] \neq \textit{nums}[i - 1]$, position $i$ starts a new block, and we increment $\textit{cnt}[\textit{nums}[i]]$. After the traversal, the answer is the number of integers whose count in $\textit{cnt}$ is exactly $1$.

The time complexity is $O(n + M)$, and the space complexity is $O(M)$. Here, $n$ is the length of the array $\textit{nums}$, and $M = 100$ is the maximum value in the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countSpecialIntegers(self, nums: List[int]) -> int:
        cnt = Counter(x for i, x in enumerate(nums) if i == 0 or x != nums[i - 1])
        return sum(v == 1 for v in cnt.values())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
