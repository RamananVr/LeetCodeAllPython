---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3700-3799/3728.Stable%20Subarrays%20With%20Equal%20Boundary%20and%20Interior%20Sum/README_EN.md
rating: 1908
source: Weekly Contest 473 Q3
tags:
    - Array
    - Hash Table
    - Prefix Sum
---

<!-- problem:start -->

# [3728. Stable Subarrays With Equal Boundary and Interior Sum](https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum)

## Description

<!-- description:start -->

<p>You are given an integer array <code>capacity</code>.</p>

<p>A <span data-keyword="subarray-nonempty">subarray</span> <code>capacity[l..r]</code> is considered <strong>stable</strong> if:</p>

<ul>
	<li>Its length is <strong>at least</strong> 3.</li>
	<li>The <strong>first</strong> and <strong>last</strong> elements are each equal to the <strong>sum</strong> of all elements <strong>strictly between</strong> them (i.e., <code>capacity[l] = capacity[r] = capacity[l + 1] + capacity[l + 2] + ... + capacity[r - 1]</code>).</li>
</ul>

<p>Return an integer denoting the number of <strong>stable subarrays</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">capacity = [9,3,3,3,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>[9,3,3,3,9]</code> is stable because the first and last elements are both 9, and the sum of the elements strictly between them is <code>3 + 3 + 3 = 9</code>.</li>
	<li><code>[3,3,3]</code> is stable because the first and last elements are both 3, and the sum of the elements strictly between them is 3.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">capacity = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No subarray of length at least 3 has equal first and last elements, so the answer is 0.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">capacity = [-4,4,0,0,-8,-4]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><code>[-4,4,0,0,-8,-4]</code> is stable because the first and last elements are both -4, and the sum of the elements strictly between them is <code>4 + 0 + 0 + (-8) = -4</code></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= capacity.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= capacity[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix Sum + Hash Table + Enumeration

We define a prefix sum array $\textit{s}$, where $s[i]$ represents the sum of the first $i$ elements in the array $\text{capacity}$, that is, $s[i] = \text{capacity}[0] + \text{capacity}[1] + \ldots + \text{capacity}[i-1]$. Initially, $s[0] = 0$.

According to the problem statement, a subarray $\text{capacity}[l..r]$ is a stable array if:

$$
\text{capacity}[l] = \text{capacity}[r] = \text{capacity}[l + 1] + \text{capacity}[l + 2] + \ldots + \text{capacity}[r - 1]
$$

That is:

$$
\text{capacity}[l] = \text{capacity}[r] = s[r] - s[l + 1]
$$

We can enumerate the right endpoint $r$. For each $r$, we calculate the left endpoint $l = r - 2$, and store the information of the left endpoints that meet the condition in a hash table. Specifically, we use a hash table $\text{cnt}$ to record the number of occurrences of each key-value pair $(\text{capacity}[l], \text{capacity}[l] + s[l + 1])$.

When we enumerate the right endpoint $r$, we can query the hash table $\text{cnt}$ to get the number of left endpoints that meet the condition, that is, the number of occurrences of the key-value pair $(\text{capacity}[r], s[r])$, and add it to the answer.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        s = list(accumulate(capacity, initial=0))
        n = len(capacity)
        ans = 0
        cnt = defaultdict(int)
        for r in range(2, n):
            l = r - 2
            cnt[(capacity[l], capacity[l] + s[l + 1])] += 1
            ans += cnt[(capacity[r], s[r])]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
