---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2100-2199/2170.Minimum%20Operations%20to%20Make%20the%20Array%20Alternating/README_EN.md
rating: 1662
source: Weekly Contest 280 Q2
tags:
    - Greedy
    - Array
    - Hash Table
    - Counting
---

<!-- problem:start -->

# [2170. Minimum Operations to Make the Array Alternating](https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> array <code>nums</code> consisting of <code>n</code> positive integers.</p>

<p>The array <code>nums</code> is called <strong>alternating</strong> if:</p>

<ul>
	<li><code>nums[i - 2] == nums[i]</code>, where <code>2 &lt;= i &lt;= n - 1</code>.</li>
	<li><code>nums[i - 1] != nums[i]</code>, where <code>1 &lt;= i &lt;= n - 1</code>.</li>
</ul>

<p>In one <strong>operation</strong>, you can choose an index <code>i</code> and <strong>change</strong> <code>nums[i]</code> into <strong>any</strong> positive integer.</p>

<p>Return <em>the <strong>minimum number of operations</strong> required to make the array alternating</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,3,2,4,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
One way to make the array alternating is by converting it to [3,1,3,<u><strong>1</strong></u>,<u><strong>3</strong></u>,<u><strong>1</strong></u>].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,2,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
One way to make the array alternating is by converting it to [1,2,<u><strong>1</strong></u>,2,<u><strong>1</strong></u>].
The number of operations required in this case is 2.
Note that the array cannot be converted to [<u><strong>2</strong></u>,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Maintain Count of Odd and Even Positions

According to the problem description, if an array $\textit{nums}$ is an alternating array, then the elements at odd positions and even positions must be different, and the elements at odd positions are the same, as well as the elements at even positions.

To minimize the number of operations required to transform the array $\textit{nums}$ into an alternating array, we can count the occurrence of elements at odd and even positions. We find the two elements with the highest occurrence at even positions, $a_0$ and $a_2$, and their corresponding counts $a_1$ and $a_3$; similarly, we find the two elements with the highest occurrence at odd positions, $b_0$ and $b_2$, and their corresponding counts $b_1$ and $b_3$.

If $a_0 \neq b_0$, then we can change all elements at even positions in the array $\textit{nums}$ to $a_0$ and all elements at odd positions to $b_0$, making the number of operations $n - (a_1 + b_1)$; if $a_0 = b_0$, then we can change all elements at even positions in the array $\textit{nums}$ to $a_0$ and all elements at odd positions to $b_2$, or change all elements at even positions to $a_2$ and all elements at odd positions to $b_0$, making the number of operations $n - \max(a_1 + b_3, a_3 + b_1)$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def f(i: int) -> Tuple[int, int, int, int]:
            k1 = k2 = 0
            cnt = Counter(nums[i::2])
            for k, v in cnt.items():
                if cnt[k1] < v:
                    k2, k1 = k1, k
                elif cnt[k2] < v:
                    k2 = k
            return k1, cnt[k1], k2, cnt[k2]

        a, b = f(0), f(1)
        n = len(nums)
        if a[0] != b[0]:
            return n - (a[1] + b[1])
        return n - max(a[1] + b[3], a[3] + b[1])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
