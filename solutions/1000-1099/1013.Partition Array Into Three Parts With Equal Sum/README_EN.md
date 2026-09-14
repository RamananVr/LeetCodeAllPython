---
comments: true
difficulty: Easy
rating: 1378
source: Weekly Contest 129 Q1
tags:
    - Greedy
    - Array
---

<!-- problem:start -->

# [1013. Partition Array Into Three Parts With Equal Sum](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum)

## Description

<!-- description:start -->

<p>Given an array of integers <code>arr</code>, return <code>true</code> if we can partition the array into three <strong>non-empty</strong> parts with equal sums.</p>

<p>Formally, we can partition the array if we can find indexes <code>i + 1 &lt; j</code> with <code>(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])</code></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [0,2,1,-6,6,-7,9,1,2,0,1]
<strong>Output:</strong> true
<strong>Explanation: </strong>0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [0,2,1,-6,6,7,9,-1,2,0,1]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,3,6,5,-2,2,5,1,-9,4]
<strong>Output:</strong> true
<strong>Explanation: </strong>3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Traversal and Summation

<!-- thinking:start -->

> **Thinking**
>
> Trying every pair of cuts is $O(n^2)$. Three equal parts exist only when the total is divisible by $3$ and we can form at least three contiguous pieces each summing to $s=\textit{sum}/3$.
>
> A left-to-right accumulation that resets at every $s$ counts such pieces. Extra pieces may be absorbed into the last part, so a count of at least $3$ is enough.
>
> We reject a nonzero remainder modulo $3$, then maintain the running part sum and the part count in one pass.

<!-- thinking:end -->

First, we calculate the sum of the entire array and check if the sum is divisible by 3. If it is not, we directly return $\textit{false}$.

Otherwise, let $\textit{s}$ represent the sum of each part. We use a variable $\textit{cnt}$ to record the number of parts found so far, and another variable $\textit{t}$ to record the current part's sum. Initially, $\textit{cnt} = 0$ and $\textit{t} = 0$.

Then we traverse the array. For each element $x$, we add $x$ to $\textit{t}$. If $\textit{t}$ equals $s$, it means we have found one part, so we increment $\textit{cnt}$ by one and reset $\textit{t}$ to 0.

Finally, we check if $\textit{cnt}$ is greater than or equal to 3.

The time complexity is $O(n)$, where $n$ is the length of the array $\textit{arr}$. The space complexity is $O(1)$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s, mod = divmod(sum(arr), 3)
        if mod:
            return False
        cnt = t = 0
        for x in arr:
            t += x
            if t == s:
                cnt += 1
                t = 0
        return cnt >= 3
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
