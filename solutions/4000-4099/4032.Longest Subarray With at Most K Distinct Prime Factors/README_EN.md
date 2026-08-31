---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/4000-4099/4032.Longest%20Subarray%20With%20at%20Most%20K%20Distinct%20Prime%20Factors/README_EN.md
---

<!-- problem:start -->

# [4032. Longest Subarray With at Most K Distinct Prime Factors](https://leetcode.com/problems/longest-subarray-with-at-most-k-distinct-prime-factors)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> consisting of positive integers and an integer <code>k</code>.</p>

<p>The <strong>prime factor set</strong> of a <span data-keyword="subarray-nonempty"><strong>subarray</strong></span> is the <strong>union</strong> of the distinct <span data-keyword="prime-number"><strong>prime</strong></span> factors of all its elements.</p>

<p>Return the length of the <strong>longest</strong> subarray whose prime factor set contains <strong>at most</strong> <code>k</code> distinct prime factors. If no such subarray exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [7,6,10,12,11], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Consider the subarray <code>[6, 10, 12]</code>:</p>

<ul>
	<li>The distinct prime factors of 6 are <code>{2, 3}</code>.</li>
	<li>The distinct prime factors of 10 are <code>{2, 5}</code>.</li>
	<li>The distinct prime factors of 12 are <code>{2, 3}</code>.</li>
	<li>The union of these sets is <code>{2, 3, 5}</code>, which contains 3 distinct prime factors.</li>
</ul>

<p>No longer subarray satisfies the condition. Therefore, the answer is 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,6,9,18], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Consider the entire array <code>[4, 6, 9, 18]</code>:</p>

<ul>
	<li>The distinct prime factors of 4 are <code>{2}</code>.</li>
	<li>The distinct prime factors of 6 are <code>{2, 3}</code>.</li>
	<li>The distinct prime factors of 9 are <code>{3}</code>.</li>
	<li>The distinct prime factors of 18 are <code>{2, 3}</code>.</li>
	<li>The union of these sets is <code>{2, 3}</code>, which contains 2 distinct prime factors.</li>
</ul>

<p>Since <code>2 &lt;= 4</code>, the entire array is valid. Therefore, the answer is 4.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [6,10,15], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Every subarray of length at least 2 has prime factor set <code>{2, 3, 5}</code>, which contains 3 distinct prime factors.</p>

<p>Since <code>3 &gt; 2</code>, only subarrays of length 1 are valid. Therefore, the answer is 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Sliding Window

First, we preprocess the list of prime factors for every number in $[2, 10^5]$ and store them in $\textit{primes}$. Specifically, we enumerate $i = 2, 3, \cdots, M$. If $\textit{primes}[i]$ is empty, then $i$ is a prime, and we add $i$ to the prime-factor list of every multiple of $i$.

Then we use a sliding window to find the longest valid subarray. A hash table $\textit{cnt}$ records the occurrence count of each prime factor in the current window. When the right pointer $r$ expands, we add all prime factors of $\textit{nums}[r]$ to the window. When the number of distinct prime factors in the window exceeds $k$, the left pointer $l$ shrinks and we remove the prime factors of $\textit{nums}[l]$. Whenever the window is valid, we update the answer with the window length.

The time complexity is $O(M \log \log M + n \log M)$, and the space complexity is $O(M \log \log M)$, where $n$ is the length of $\textit{nums}$ and $M = 10^5$ is the maximum value of the array elements.

<!-- tabs:start -->

#### Python3

```python
mx = 100001
primes = [[] for _ in range(mx)]
for i in range(2, mx):
    if not primes[i]:
        for j in range(i, mx, i):
            primes[j].append(i)

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = l = 0
        for r, x in enumerate(nums):
            for y in primes[x]:
                cnt[y] += 1
            while len(cnt) > k:
                for y in primes[nums[l]]:
                    cnt[y] -= 1
                    if cnt[y] == 0:
                        cnt.pop(y)
                l += 1
            ans = max(ans, r - l + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
