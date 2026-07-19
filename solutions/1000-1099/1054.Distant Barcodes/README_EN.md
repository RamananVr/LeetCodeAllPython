---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1054.Distant%20Barcodes/README_EN.md
rating: 1701
source: Weekly Contest 138 Q4
tags:
    - Greedy
    - Array
    - Hash Table
    - Counting
    - Sorting
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1054. Distant Barcodes](https://leetcode.com/problems/distant-barcodes)

## Description

<!-- description:start -->

<p>In a warehouse, there is a row of barcodes, where the <code>i<sup>th</sup></code> barcode is <code>barcodes[i]</code>.</p>

<p>Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> barcodes = [1,1,1,2,2,2]
<strong>Output:</strong> [2,1,2,1,2,1]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> barcodes = [1,1,1,1,2,2,3,3]
<strong>Output:</strong> [1,3,1,3,1,2,1,2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= barcodes.length &lt;= 10000</code></li>
	<li><code>1 &lt;= barcodes[i] &lt;= 10000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting + Sorting

First, we use a hash table or array $cnt$ to count the number of occurrences of each number in the array $barcodes$. Then, we sort the numbers in $barcodes$ according to their occurrence times in $cnt$ from large to small. If the occurrence times are the same, we sort them from small to large (to ensure the same numbers are adjacent).

Next, we create an answer array $ans$ of length $n$. We traverse the sorted $barcodes$, and sequentially fill the elements into the even index positions $0, 2, 4, \cdots$ of the answer array. Then, we fill the remaining elements into the odd index positions $1, 3, 5, \cdots$ of the answer array.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(M)$. Where $n$ and $M$ are the length of the array $barcodes$ and the maximum value in the array $barcodes$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        barcodes.sort(key=lambda x: (-cnt[x], x))
        n = len(barcodes)
        ans = [0] * len(barcodes)
        ans[::2] = barcodes[: (n + 1) // 2]
        ans[1::2] = barcodes[(n + 1) // 2 :]
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
