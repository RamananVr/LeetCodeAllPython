---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3300-3399/3312.Sorted%20GCD%20Pair%20Queries/README_EN.md
rating: 2532
source: Weekly Contest 418 Q4
tags:
    - Array
    - Hash Table
    - Math
    - Binary Search
    - Combinatorics
    - Counting
    - Number Theory
    - Prefix Sum
---

<!-- problem:start -->

# [3312. Sorted GCD Pair Queries](https://leetcode.com/problems/sorted-gcd-pair-queries)

## Description

<!-- description:start -->

<p>You are given an integer array <code>nums</code> of length <code>n</code> and an integer array <code>queries</code>.</p>

<p>Let <code>gcdPairs</code> denote an array obtained by calculating the <span data-keyword="gcd-function">GCD</span> of all possible pairs <code>(nums[i], nums[j])</code>, where <code>0 &lt;= i &lt; j &lt; n</code>, and then sorting these values in <strong>ascending</strong> order.</p>

<p>For each query <code>queries[i]</code>, you need to find the element at index <code>queries[i]</code> in <code>gcdPairs</code>.</p>

<p>Return an integer array <code>answer</code>, where <code>answer[i]</code> is the value at <code>gcdPairs[queries[i]]</code> for each query.</p>

<p>The term <code>gcd(a, b)</code> denotes the <strong>greatest common divisor</strong> of <code>a</code> and <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4], queries = [0,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p><code>gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1]</code>.</p>

<p>After sorting in ascending order, <code>gcdPairs = [1, 1, 2]</code>.</p>

<p>So, the answer is <code>[gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,4,2,1], queries = [5,3,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,2,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p><code>gcdPairs</code> sorted in ascending order is <code>[1, 1, 1, 2, 2, 4]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2], queries = [0,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p><code>gcdPairs = [2]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= queries[i] &lt; n * (n - 1) / 2</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Preprocessing + Prefix Sum + Binary Search

We can preprocess to obtain the occurrence count of the greatest common divisor (GCD) of all pairs in the array $\textit{nums}$, recorded in the array $\textit{cntG}$. Then, we calculate the prefix sum of the array $\textit{cntG}$. Finally, for each query, we can use binary search to find the index of the first element in the array $\textit{cntG}$ that is greater than $\textit{queries}[i]$, which is the answer.

Let $\textit{mx}$ denote the maximum value in the array $\textit{nums}$, and let $\textit{cnt}$ record the occurrence count of each number in the array $\textit{nums}$. Let $\textit{cntG}[i]$ denote the number of pairs in the array $\textit{nums}$ whose GCD is equal to $i$. To calculate $\textit{cntG}[i]$, we can follow these steps:

1. Calculate the occurrence count $v$ of multiples of $i$ in the array $\textit{nums}$. Then, the number of pairs formed by any two elements from these multiples must have a GCD that is a multiple of $i$, i.e., $\textit{cntG}[i]$ needs to be increased by $v \times (v - 1) / 2$;
2. We need to exclude pairs whose GCD is a multiple of $i$ and greater than $i$. Therefore, for multiples $j$ of $i$, we need to subtract $\textit{cntG}[j]$.

The above steps require us to traverse $i$ from large to small so that when calculating $\textit{cntG}[i]$, we have already calculated all $\textit{cntG}[j]$.

Finally, we calculate the prefix sum of the array $\textit{cntG}$, and for each query, we can use binary search to find the index of the first element in the array $\textit{cntG}$ that is greater than $\textit{queries}[i]$, which is the answer.

The time complexity is $O(n + (M + q) \times \log M)$, and the space complexity is $O(M)$. Here, $n$ and $M$ represent the length and the maximum value of the array $\textit{nums}$, respectively, and $q$ represents the number of queries.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = Counter(nums)
        cnt_g = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            v = 0
            for j in range(i, mx + 1, i):
                v += cnt[j]
                cnt_g[i] -= cnt_g[j]
            cnt_g[i] += v * (v - 1) // 2
        s = list(accumulate(cnt_g))
        return [bisect_right(s, q) for q in queries]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
