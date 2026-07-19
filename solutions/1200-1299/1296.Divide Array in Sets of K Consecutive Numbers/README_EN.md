---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1296.Divide%20Array%20in%20Sets%20of%20K%20Consecutive%20Numbers/README_EN.md
rating: 1490
source: Weekly Contest 168 Q2
tags:
    - Greedy
    - Array
    - Hash Table
    - Sorting
---

<!-- problem:start -->

# [1296. Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers)

## Description

<!-- description:start -->

<p>Given an array of integers <code>nums</code> and a positive integer <code>k</code>, check whether it is possible to divide this array into sets of <code>k</code> consecutive numbers.</p>

<p>Return <code>true</code> <em>if it is possible</em>.<strong> </strong>Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,3,4,4,5,6], k = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> Array can be divided into [1,2,3,4] and [3,4,5,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4], k = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> Each array should be divided in subarrays of size 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Note:</strong> This question is the same as&nbsp;846:&nbsp;<a href="https://leetcode.com/problems/hand-of-straights/" target="_blank">https://leetcode.com/problems/hand-of-straights/</a>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Sorting

First, we check if the length of the array $\textit{nums}$ is divisible by $\textit{k}$. If it is not divisible, it means the array cannot be divided into subarrays of length $\textit{k}$, and we return $\text{false}$ directly.

Next, we use a hash table $\textit{cnt}$ to count the occurrences of each number in the array $\textit{nums}$, and then we sort the array $\textit{nums}$.

After sorting, we iterate through the array $\textit{nums}$, and for each number $x$, if $\textit{cnt}[x]$ is not $0$, we enumerate each number $y$ from $x$ to $x + \textit{k} - 1$. If $\textit{cnt}[y]$ is $0$, it means we cannot divide the array into subarrays of length $\textit{k}$, and we return $\text{false}$ directly. Otherwise, we decrement $\textit{cnt}[y]$ by $1$.

After the loop, if no issues were encountered, it means we can divide the array into subarrays of length $\textit{k}$, and we return $\text{true}$.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        cnt = Counter(nums)
        for x in sorted(nums):
            if cnt[x]:
                for y in range(x, x + k):
                    if cnt[y] == 0:
                        return False
                    cnt[y] -= 1
        return True
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Ordered Set

Similar to Solution 1, we first check if the length of the array $\textit{nums}$ is divisible by $\textit{k}$. If it is not divisible, it means the array cannot be divided into subarrays of length $\textit{k}$, and we return $\text{false}$ directly.

Next, we use an ordered set $\textit{sd}$ to count the occurrences of each number in the array $\textit{nums}$.

Then, we repeatedly extract the smallest value $x$ from the ordered set and enumerate each number $y$ from $x$ to $x + \textit{k} - 1$. If these numbers all appear in the ordered set with non-zero occurrences, we decrement their occurrence count by $1$. If the occurrence count becomes $0$ after the decrement, we remove the number from the ordered set; otherwise, it means we cannot divide the array into subarrays of length $\textit{k}$, and we return $\text{false}$.

If we can successfully divide the array into subarrays of length $\textit{k}$, we return $\text{true}$ after completing the traversal.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $\textit{nums}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        cnt = Counter(nums)
        sd = SortedDict(cnt)
        while sd:
            x = next(iter(sd))
            for y in range(x, x + k):
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
