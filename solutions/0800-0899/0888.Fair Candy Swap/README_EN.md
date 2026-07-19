---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0888.Fair%20Candy%20Swap/README_EN.md
tags:
    - Array
    - Hash Table
    - Binary Search
    - Sorting
---

<!-- problem:start -->

# [888. Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap)

## Description

<!-- description:start -->

<p>Alice and Bob have a different total number of candies. You are given two integer arrays <code>aliceSizes</code> and <code>bobSizes</code> where <code>aliceSizes[i]</code> is the number of candies of the <code>i<sup>th</sup></code> box of candy that Alice has and <code>bobSizes[j]</code> is the number of candies of the <code>j<sup>th</sup></code> box of candy that Bob has.</p>

<p>Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.</p>

<p>Return a<em>n integer array </em><code>answer</code><em> where </em><code>answer[0]</code><em> is the number of candies in the box that Alice must exchange, and </em><code>answer[1]</code><em> is the number of candies in the box that Bob must exchange</em>. If there are multiple answers, you may <strong>return any</strong> one of them. It is guaranteed that at least one answer exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> aliceSizes = [1,1], bobSizes = [2,2]
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> aliceSizes = [1,2], bobSizes = [2,3]
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> aliceSizes = [2], bobSizes = [1,3]
<strong>Output:</strong> [2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= aliceSizes.length, bobSizes.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= aliceSizes[i], bobSizes[j] &lt;= 10<sup>5</sup></code></li>
	<li>Alice and Bob have a different total number of candies.</li>
	<li>There will be at least one valid answer for the given input.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We can first calculate the difference in the total number of candies between Alice and Bob, divide it by two to get the difference in the number of candies to be exchanged $\textit{diff}$, and use a hash table $\textit{s}$ to store the number of candies in Bob's candy boxes. Then, we traverse Alice's candy boxes, and for each candy count $\textit{a}$, we check if $\textit{a} - \textit{diff}$ is in the hash table $\textit{s}$. If it exists, it means we have found a valid answer, and we return it.

The time complexity is $O(m + n)$, and the space complexity is $O(n)$. Where $m$ and $n$ are the number of candy boxes Alice and Bob have, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) >> 1
        s = set(bobSizes)
        for a in aliceSizes:
            if (b := (a - diff)) in s:
                return [a, b]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
