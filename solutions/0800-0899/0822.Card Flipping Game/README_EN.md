---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0822.Card%20Flipping%20Game/README_EN.md
tags:
    - Array
    - Hash Table
---

<!-- problem:start -->

# [822. Card Flipping Game](https://leetcode.com/problems/card-flipping-game)

## Description

<!-- description:start -->

<p>You are given two <strong>0-indexed</strong> integer arrays <code>fronts</code> and <code>backs</code> of length <code>n</code>, where the <code>i<sup>th</sup></code> card has the positive integer <code>fronts[i]</code> printed on the front and <code>backs[i]</code> printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).</p>

<p>After flipping the cards, an integer is considered <strong>good</strong> if it is facing down on some card and <strong>not</strong> facing up on any card.</p>

<p>Return <em>the minimum possible good integer after flipping the cards</em>. If there are no good integers, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3].
2 is the minimum good integer as it appears facing down but not facing up.
It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> fronts = [1], backs = [1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
There are no good integers no matter how we flip the cards, so we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == fronts.length == backs.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= fronts[i], backs[i] &lt;= 2000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table

We observe that for position $i$, if $\textit{fronts}[i]$ is equal to $\textit{backs}[i]$, then it certainly does not satisfy the condition.

Therefore, we first identify all elements that appear the same on both the front and back sides and record them in a hash set $s$.

Next, we iterate through all elements in both the front and back arrays. For any element $x$ that is **not** in the hash set $s$, we update the minimum value of the answer.

Finally, if we find any element that satisfies the condition, we return the minimum answer; otherwise, we return $0$.

The time complexity is $O(n)$ and the space complexity is $O(n)$, where $n$ is the length of the arrays.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        s = {a for a, b in zip(fronts, backs) if a == b}
        return min((x for x in chain(fronts, backs) if x not in s), default=0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
