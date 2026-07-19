---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2602.Minimum%20Operations%20to%20Make%20All%20Array%20Elements%20Equal/README_EN.md
rating: 1903
source: Weekly Contest 338 Q3
tags:
    - Array
    - Binary Search
    - Prefix Sum
    - Sorting
---

<!-- problem:start -->

# [2602. Minimum Operations to Make All Array Elements Equal](https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal)

## Description

<!-- description:start -->

<p>You are given an array <code>nums</code> consisting of positive integers.</p>

<p>You are also given an integer array <code>queries</code> of size <code>m</code>. For the <code>i<sup>th</sup></code> query, you want to make all of the elements of <code>nums</code> equal to<code> queries[i]</code>. You can perform the following operation on the array <strong>any</strong> number of times:</p>

<ul>
	<li><strong>Increase</strong> or <strong>decrease</strong> an element of the array by <code>1</code>.</li>
</ul>

<p>Return <em>an array </em><code>answer</code><em> of size </em><code>m</code><em> where </em><code>answer[i]</code><em> is the <strong>minimum</strong> number of operations to make all elements of </em><code>nums</code><em> equal to </em><code>queries[i]</code>.</p>

<p><strong>Note</strong> that after each query the array is reset to its original state.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,6,8], queries = [1,5]
<strong>Output:</strong> [14,10]
<strong>Explanation:</strong> For the first query we can do the following operations:
- Decrease nums[0] 2 times, so that nums = [1,1,6,8].
- Decrease nums[2] 5 times, so that nums = [1,1,1,8].
- Decrease nums[3] 7 times, so that nums = [1,1,1,1].
So the total number of operations for the first query is 2 + 5 + 7 = 14.
For the second query we can do the following operations:
- Increase nums[0] 2 times, so that nums = [5,1,6,8].
- Increase nums[1] 4 times, so that nums = [5,5,6,8].
- Decrease nums[2] 1 time, so that nums = [5,5,5,8].
- Decrease nums[3] 3 times, so that nums = [5,5,5,5].
So the total number of operations for the second query is 2 + 4 + 1 + 3 = 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,9,6,3], queries = [10]
<strong>Output:</strong> [20]
<strong>Explanation:</strong> We can increase each value in the array to 10. The total number of operations will be 8 + 1 + 4 + 7 = 20.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == queries.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], queries[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: sort + prefix sum + binary search

First, we sort the array $nums$ and calculate the prefix sum array $s$ with a length of $n+1$, where $s[i]$ represents the sum of the first $i$ elements in the array $nums$.

Then, we traverse each query $queries[i]$, we need to reduce all elements greater than $queries[i]$ to $queries[i]$, and increase all elements less than $queries[i]$ to $queries[i]$.

We can use binary search to find the index $i$ of the first element in the array $nums$ that is greater than $queries[i]$. There are $n-i$ elements that need to be reduced to $queries[i]$, and the sum of these elements is $s[n]-s[i]$. These elements need to be reduced by $n-i$ $queries[i]$, so the total number of operations to reduce these elements to $queries[i]$ is $s[n]-s[i]-(n-i)\times queries[i]$.

Similarly, we can find the index $i$ of the first element in the array $nums$ that is greater than or equal to $queries[i]$. There are $i$ elements that need to be increased to $queries[i]$, and the sum of these elements is $s[i]$. Therefore, the total number of operations to increase these elements to $queries[i]$ is $queries[i]\times i-s[i]$.

Finally, add these two total operation counts together to get the minimum number of operations to change all elements in the array $nums$ to $queries[i]$, that is, $ans[i]=s[n]-s[i]-(n-i)\times queries[i]+queries[i]\times i-s[i]$.

Time complexity $O(n \times \log n)$, space complexity $O(n)$, where $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        s = list(accumulate(nums, initial=0))
        ans = []
        for x in queries:
            i = bisect_left(nums, x + 1)
            t = s[-1] - s[i] - (len(nums) - i) * x
            i = bisect_left(nums, x)
            t += x * i - s[i]
            ans.append(t)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
