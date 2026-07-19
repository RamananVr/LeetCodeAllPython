---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0100-0199/0135.Candy/README_EN.md
tags:
    - Greedy
    - Array
---

<!-- problem:start -->

# [135. Candy](https://leetcode.com/problems/candy)

## Description

<!-- description:start -->

<p>There are <code>n</code> children standing in a line. Each child is assigned a rating value given in the integer array <code>ratings</code>.</p>

<p>You are giving candies to these children subjected to the following requirements:</p>

<ul>
	<li>Each child must have at least one candy.</li>
	<li>Children with a higher rating get more candies than their neighbors.</li>
</ul>

<p>Return <em>the minimum number of candies you need to have to distribute the candies to the children</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> ratings = [1,0,2]
<strong>Output:</strong> 5
<strong>Explanation:</strong> You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> ratings = [1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == ratings.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Two traversals

We initialize two arrays $left$ and $right$, where $left[i]$ represents the minimum number of candies the current child should get when the current child's score is higher than the left child's score, and $right[i]$ represents the minimum number of candies the current child should get when the current child's score is higher than the right child's score. Initially, $left[i]=1$, $right[i]=1$.

We traverse the array from left to right once, and if the current child's score is higher than the left child's score, then $left[i]=left[i-1]+1$; similarly, we traverse the array from right to left once, and if the current child's score is higher than the right child's score, then $right[i]=right[i+1]+1$.

Finally, we traverse the array of scores once, and the minimum number of candies each child should get is the maximum of $left[i]$ and $right[i]$, and we add them up to get the answer.

Time complexity $O(n)$, space complexity $O(n)$. Where $n$ is the length of the array of scores.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        return sum(max(a, b) for a, b in zip(left, right))
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
