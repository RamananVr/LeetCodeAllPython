---
comments: true
difficulty: Medium
tags:
    - Greedy
    - Array
    - Hash Table
    - Sorting
---

<!-- problem:start -->

# [954. Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs)

## Description

<!-- description:start -->

<p>Given an integer array of even length <code>arr</code>, return <code>true</code><em> if it is possible to reorder </em><code>arr</code><em> such that </em><code>arr[2 * i + 1] = 2 * arr[2 * i]</code><em> for every </em><code>0 &lt;= i &lt; len(arr) / 2</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,3,6]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,1,2,6]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,-2,2,-4]
<strong>Output:</strong> true
<strong>Explanation:</strong> We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>arr.length</code> is even.</li>
	<li><code>-10<sup>5</sup> &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> Reorder the array so each even index is half of the next. Zeros pair only with zeros; an odd count fails. Other values should match from small absolute value to large: each $x$ must find enough remaining $2x$, or a larger number may already have been claimed. A frequency map tracks leftovers.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        if freq[0] & 1:
            return False
        for x in sorted(freq, key=abs):
            if freq[x << 1] < freq[x]:
                return False
            freq[x << 1] -= freq[x]
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
