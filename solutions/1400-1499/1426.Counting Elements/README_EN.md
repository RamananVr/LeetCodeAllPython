---
comments: true
difficulty: Easy
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [1426. Counting Elements 🔒](https://leetcode.com/problems/counting-elements)

## Description

<!-- description:start -->

<p>Given an integer array <code>arr</code>, count how many elements <code>x</code> there are, such that <code>x + 1</code> is also in <code>arr</code>. If there are duplicates in <code>arr</code>, count them separately.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1 and 2 are counted cause 2 and 3 are in arr.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,1,3,3,5,5,7,7]
<strong>Output:</strong> 0
<strong>Explanation:</strong> No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 1000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Counting

<!-- thinking:start -->

> **Thinking**
>
> $n\le 1000$ would allow a scan for $x+1$ per element. After counting, for each seen $x$ we add its frequency if $x+1$ also occurs.

<!-- thinking:end -->

We can use a hash table or array $cnt$ to record the frequency of each number in the array $arr$. Then, we traverse each number $x$ in $cnt$. If $x+1$ also exists in $cnt$, we add $cnt[x]$ to the answer.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $arr$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        return sum(v for x, v in cnt.items() if cnt[x + 1])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
