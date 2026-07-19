---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2700-2799/2799.Count%20Complete%20Subarrays%20in%20an%20Array/README_EN.md
rating: 1397
source: Weekly Contest 356 Q2
tags:
    - Array
    - Hash Table
    - Sliding Window
---

<!-- problem:start -->

# [2799. Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array)

## Description

<!-- description:start -->

<p>You are given an array <code>nums</code> consisting of <strong>positive</strong> integers.</p>

<p>We call a subarray of an array <strong>complete</strong> if the following condition is satisfied:</p>

<ul>
	<li>The number of <strong>distinct</strong> elements in the subarray is equal to the number of distinct elements in the whole array.</li>
</ul>

<p>Return <em>the number of <strong>complete</strong> subarrays</em>.</p>

<p>A <strong>subarray</strong> is a contiguous non-empty part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,5,5,5]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2000</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Enumeration

First, we use a hash table to count the number of distinct elements in the array, denoted as $cnt$.

Next, we enumerate the left endpoint index $i$ of the subarray and maintain a set $s$ to store the elements in the subarray. Each time we move the right endpoint index $j$ to the right, we add $nums[j]$ to the set $s$ and check whether the size of the set $s$ equals $cnt$. If it equals $cnt$, it means the current subarray is a complete subarray, and we increment the answer by $1$.

After the enumeration ends, we return the answer.

Time complexity: $O(n^2)$, Space complexity: $O(n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = len(set(nums))
        ans, n = 0, len(nums)
        for i in range(n):
            s = set()
            for x in nums[i:]:
                s.add(x)
                if len(s) == cnt:
                    ans += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Hash Table + Two Pointers

Similar to Solution 1, we can use a hash table to count the number of distinct elements in the array, denoted as $cnt$.

Next, we use two pointers to maintain a sliding window, where the right endpoint index is $j$ and the left endpoint index is $i$.

Each time we fix the left endpoint index $i$, we move the right endpoint index $j$ to the right. When the number of distinct elements in the sliding window equals $cnt$, it means that all subarrays from the left endpoint index $i$ to the right endpoint index $j$ and beyond are complete subarrays. We then increment the answer by $n - j$, where $n$ is the length of the array. Afterward, we move the left endpoint index $i$ one step to the right and repeat the process.

Time complexity: $O(n)$, Space complexity: $O(n)$, where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        cnt = len(set(nums))
        d = Counter()
        ans, n = 0, len(nums)
        i = 0
        for j, x in enumerate(nums):
            d[x] += 1
            while len(d) == cnt:
                ans += n - j
                d[nums[i]] -= 1
                if d[nums[i]] == 0:
                    d.pop(nums[i])
                i += 1
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
