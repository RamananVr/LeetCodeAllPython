---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2856.Minimum%20Array%20Length%20After%20Pair%20Removals/README_EN.md
rating: 1749
source: Biweekly Contest 113 Q2
tags:
    - Greedy
    - Array
    - Hash Table
    - Two Pointers
    - Binary Search
    - Counting
---

<!-- problem:start -->

# [2856. Minimum Array Length After Pair Removals](https://leetcode.com/problems/minimum-array-length-after-pair-removals)

## Description

<!-- description:start -->

<p>Given an integer array <code>num</code> sorted in non-decreasing order.</p>

<p>You can perform the following operation any number of times:</p>

<ul>
	<li>Choose <strong>two</strong> indices, <code>i</code> and <code>j</code>, where <code>nums[i] &lt; nums[j]</code>.</li>
	<li>Then, remove the elements at indices <code>i</code> and <code>j</code> from <code>nums</code>. The remaining elements retain their original order, and the array is re-indexed.</li>
</ul>

<p>Return the <strong>minimum</strong> length of <code>nums</code> after applying the operation zero or more times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2856.Minimum%20Array%20Length%20After%20Pair%20Removals/images/tcase1.gif" style="width: 160px; height: 70px;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,2,3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2856.Minimum%20Array%20Length%20After%20Pair%20Removals/images/tcase2.gif" style="width: 240px; height: 70px;" /></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1000000000,1000000000]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Since both numbers are equal, they cannot be removed.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,4,4,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2800-2899/2856.Minimum%20Array%20Length%20After%20Pair%20Removals/images/tcase3.gif" style="width: 210px; height: 70px;" /></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Greedy + Priority Queue (Max Heap)

We use a hash table $cnt$ to count the occurrence of each element in the array $nums$, then add each value in $cnt$ to a priority queue (max heap) $pq$. Each time we take out two elements $x$ and $y$ from $pq$, decrease their values by one. If the value after decrement is still greater than $0$, we add the decremented value back to $pq$. Each time we take out two elements from $pq$, it means we delete a pair of numbers from the array, so the length of the array decreases by $2$. When the size of $pq$ is less than $2$, we stop the deletion operation.

The time complexity is $O(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array $nums$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        pq = [-x for x in cnt.values()]
        heapify(pq)
        ans = len(nums)
        while len(pq) > 1:
            x, y = -heappop(pq), -heappop(pq)
            x -= 1
            y -= 1
            if x > 0:
                heappush(pq, -x)
            if y > 0:
                heappush(pq, -y)
            ans -= 2
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
