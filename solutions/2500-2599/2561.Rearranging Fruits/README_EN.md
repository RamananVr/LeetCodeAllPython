---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2500-2599/2561.Rearranging%20Fruits/README_EN.md
rating: 2221
source: Weekly Contest 331 Q4
tags:
    - Greedy
    - Sort
    - Array
    - Hash Table
---

<!-- problem:start -->

# [2561. Rearranging Fruits](https://leetcode.com/problems/rearranging-fruits)

## Description

<!-- description:start -->

<p>You have two fruit baskets containing <code>n</code> fruits each. You are given two <strong>0-indexed</strong> integer arrays <code>basket1</code> and <code>basket2</code> representing the cost of fruit in each basket. You want to make both baskets <strong>equal</strong>. To do so, you can use the following operation as many times as you want:</p>

<ul>
	<li>Choose two indices <code>i</code> and <code>j</code>, and swap the <code>i<sup><font size="1">th</font></sup></code> fruit of <code>basket1</code> with the <code>j<sup><font size="1">th</font></sup></code> fruit of <code>basket2</code>.</li>
	<li>The cost of the swap is <code>min(basket1[i], basket2[j])</code>.</li>
</ul>

<p>Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.</p>

<p>Return <em>the minimum cost to make both the baskets equal or </em><code>-1</code><em> if impossible.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> basket1 = [4,2,2,2], basket2 = [1,4,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> basket1 = [2,3,4,1], basket2 = [3,2,5,1]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be shown that it is impossible to make both the baskets equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>basket1.length == basket2.length</code></li>
	<li><code>1 &lt;= basket1.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= basket1[i], basket2[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Construction

First, we can remove the common elements from both arrays. For the remaining numbers, the occurrence of each number must be even, otherwise, it is impossible to construct identical arrays. Let's denote the arrays after removing common elements as $a$ and $b$.

Next, we consider how to perform the swaps.

If we want to swap the smallest number in $a$, we need to find the largest number in $b$ to swap with it; similarly, if we want to swap the smallest number in $b$, we need to find the largest number in $a$ to swap with it. This can be achieved by sorting.

However, there is another swapping scheme. We can use a smallest number $mi$ as a transition element, first swap the number in $a$ with $mi$, and then swap $mi$ with the number in $b$. In this way, the cost of swapping is $2 \times mi$.

In the code implementation, we can directly merge arrays $a$ and $b$ into an array $nums$, and then sort the array $nums$. Next, we enumerate the first half of the numbers, calculate the minimum cost each time, and add it to the answer.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        cnt = Counter()
        for a, b in zip(basket1, basket2):
            cnt[a] += 1
            cnt[b] -= 1
        mi = min(cnt)
        nums = []
        for x, v in cnt.items():
            if v % 2:
                return -1
            nums.extend([x] * (abs(v) // 2))
        nums.sort()
        m = len(nums) // 2
        return sum(min(x, mi * 2) for x in nums[:m])
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
