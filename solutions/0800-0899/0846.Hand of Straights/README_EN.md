---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0846.Hand%20of%20Straights/README_EN.md
tags:
    - Greedy
    - Array
    - Hash Table
    - Sorting
---

<!-- problem:start -->

# [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights)

## Description

<!-- description:start -->

<p>Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size <code>groupSize</code>, and consists of <code>groupSize</code> consecutive cards.</p>

<p>Given an integer array <code>hand</code> where <code>hand[i]</code> is the value written on the <code>i<sup>th</sup></code> card and an integer <code>groupSize</code>, return <code>true</code> if she can rearrange the cards, or <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Alice&#39;s hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> hand = [1,2,3,4,5], groupSize = 4
<strong>Output:</strong> false
<strong>Explanation:</strong> Alice&#39;s hand can not be rearranged into groups of 4.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hand.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= hand[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= groupSize &lt;= hand.length</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1296: <a href="https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/" target="_blank">https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/</a></p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Sorting

We first check whether the length of the array $\textit{hand}$ is divisible by $\textit{groupSize}$. If it is not, this means that the array cannot be partitioned into multiple subarrays of length $\textit{groupSize}$, so we return $\text{false}$.

Next, we use a hash table $\textit{cnt}$ to count the occurrences of each number in the array $\textit{hand}$, and then we sort the array $\textit{hand}$.

After that, we iterate over the sorted array $\textit{hand}$. For each number $x$, if $\textit{cnt}[x] \neq 0$, we enumerate every number $y$ from $x$ to $x + \textit{groupSize} - 1$. If $\textit{cnt}[y] = 0$, it means that we cannot partition the array into multiple subarrays of length $\textit{groupSize}$, so we return $\text{false}$. Otherwise, we decrement $\textit{cnt}[y]$ by $1$.

If the iteration completes successfully, it means that the array can be partitioned into multiple valid subarrays, so we return $\text{true}$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{hand}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        cnt = Counter(hand)
        for x in sorted(hand):
            if cnt[x]:
                for y in range(x, x + groupSize):
                    if cnt[y] == 0:
                        return False
                    cnt[y] -= 1
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Ordered Set

Similar to Solution 1, we first check whether the length of the array $\textit{hand}$ is divisible by $\textit{groupSize}$. If it is not, this means that the array cannot be partitioned into multiple subarrays of length $\textit{groupSize}$, so we return $\text{false}$.

Next, we use an ordered set $\textit{sd}$ to count the occurrences of each number in the array $\textit{hand}$.

Then, we repeatedly take the smallest value $x$ from the ordered set and enumerate each number $y$ from $x$ to $x + \textit{groupSize} - 1$. If all these numbers appear at least once in the ordered set, we decrement their occurrence count by $1$. If any count reaches $0$, we remove that number from the ordered set. Otherwise, if we encounter a number that does not exist in the ordered set, it means that the array cannot be partitioned into valid subarrays, so we return $\text{false}$. If the iteration completes successfully, it means that the array can be partitioned into multiple valid subarrays, so we return $\text{true}$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$, where $n$ is the length of the array $\textit{hand}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        cnt = Counter(hand)
        sd = SortedDict(cnt)
        while sd:
            x = next(iter(sd))
            for y in range(x, x + groupSize):
                if y not in sd:
                    return False
                if sd[y] == 1:
                    del sd[y]
                else:
                    sd[y] -= 1
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
