---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1000-1099/1005.Maximize%20Sum%20Of%20Array%20After%20K%20Negations/README_EN.md
rating: 1274
source: Weekly Contest 127 Q1
tags:
    - Greedy
    - Array
    - Sorting
---

<!-- problem:start -->

# [1005. Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, modify the array in the following way:</p>

<ul>
	<li>choose an index <code>i</code> and replace <code>nums[i]</code> with <code>-nums[i]</code>.</li>
</ul>

<p>You should apply this process exactly <code>k</code> times. You may choose the same index <code>i</code> multiple times.</p>

<p>Return <em>the largest possible sum of the array after modifying it in this way</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,3], k = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> Choose index 1 and nums becomes [4,-2,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,-1,0,2], k = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,-3,-1,5,-4], k = 2
<strong>Output:</strong> 13
<strong>Explanation:</strong> Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Counting

We observe that to maximize the sum of the array, we should try to turn the smallest negative numbers into positive numbers.

Given that the range of elements is $[-100, 100]$, we can use a hash table $\textit{cnt}$ to count the occurrences of each element in the array $\textit{nums}$. Then, starting from $-100$, we iterate through $x$. If $x$ exists in the hash table, we take $m = \min(\textit{cnt}[x], k)$ as the number of times to negate the element $x$. We then subtract $m$ from $\textit{cnt}[x]$, add $m$ to $\textit{cnt}[-x]$, and subtract $m$ from $k$. If $k$ becomes $0$, the operation is complete, and we exit the loop.

If $k$ is still odd and $\textit{cnt}[0] = 0$, we need to take the smallest positive number $x$ in $\textit{cnt}$, subtract $1$ from $\textit{cnt}[x]$, and add $1$ to $\textit{cnt}[-x]$.

Finally, we traverse the hash table $\textit{cnt}$ and sum the products of $x$ and $\textit{cnt}[x]$ to get the answer.

The time complexity is $O(n + M)$, and the space complexity is $O(M)$. Here, $n$ and $M$ are the length of the array $\textit{nums}$ and the size of the data range of $\textit{nums}$, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        for x in range(-100, 0):
            if cnt[x]:
                m = min(cnt[x], k)
                cnt[x] -= m
                cnt[-x] += m
                k -= m
                if k == 0:
                    break
        if k & 1 and cnt[0] == 0:
            for x in range(1, 101):
                if cnt[x]:
                    cnt[x] -= 1
                    cnt[-x] += 1
                    break
        return sum(x * v for x, v in cnt.items())
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
