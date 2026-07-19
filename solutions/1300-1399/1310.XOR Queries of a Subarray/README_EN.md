---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1300-1399/1310.XOR%20Queries%20of%20a%20Subarray/README_EN.md
rating: 1459
source: Weekly Contest 170 Q2
tags:
    - Bit Manipulation
    - Array
    - Prefix Sum
---

<!-- problem:start -->

# [1310. XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray)

## Description

<!-- description:start -->

<p>You are given an array <code>arr</code> of positive integers. You are also given the array <code>queries</code> where <code>queries[i] = [left<sub>i, </sub>right<sub>i</sub>]</code>.</p>

<p>For each query <code>i</code> compute the <strong>XOR</strong> of elements from <code>left<sub>i</sub></code> to <code>right<sub>i</sub></code> (that is, <code>arr[left<sub>i</sub>] XOR arr[left<sub>i</sub> + 1] XOR ... XOR arr[right<sub>i</sub>]</code> ).</p>

<p>Return an array <code>answer</code> where <code>answer[i]</code> is the answer to the <code>i<sup>th</sup></code> query.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
<strong>Output:</strong> [2,7,14,8] 
<strong>Explanation:</strong> 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
<strong>Output:</strong> [8,0,4,4]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length, queries.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt; arr.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Prefix XOR

We can use a prefix XOR array $s$ of length $n+1$ to store the prefix XOR results of the array $\textit{arr}$, where $s[i] = s[i-1] \oplus \textit{arr}[i-1]$. That is, $s[i]$ represents the XOR result of the first $i$ elements of $\textit{arr}$.

For a query $[l, r]$, we can obtain:

$$
\begin{aligned}
\textit{arr}[l] \oplus \textit{arr}[l+1] \oplus \cdots \oplus \textit{arr}[r] &= (\textit{arr}[0] \oplus \textit{arr}[1] \oplus \cdots \oplus \textit{arr}[l-1]) \oplus (\textit{arr}[0] \oplus \textit{arr}[1] \oplus \cdots \oplus \textit{arr}[r]) \\
&= s[l] \oplus s[r+1]
\end{aligned}
$$

Time complexity is $O(n+m)$, and space complexity is $O(n)$. Here, $n$ and $m$ are the lengths of the array $\textit{arr}$ and the query array $\textit{queries}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        s = list(accumulate(arr, xor, initial=0))
        return [s[r + 1] ^ s[l] for l, r in queries]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
