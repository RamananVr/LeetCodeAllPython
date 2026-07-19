---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2800-2899/2831.Find%20the%20Longest%20Equal%20Subarray/README_EN.md
rating: 1975
source: Weekly Contest 359 Q4
tags:
    - Array
    - Hash Table
    - Binary Search
    - Sliding Window
---

<!-- problem:start -->

# [2831. Find the Longest Equal Subarray](https://leetcode.com/problems/find-the-longest-equal-subarray)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>A subarray is called <strong>equal</strong> if all of its elements are equal. Note that the empty subarray is an <strong>equal</strong> subarray.</p>

<p>Return <em>the length of the <strong>longest</strong> possible equal subarray after deleting <strong>at most</strong> </em><code>k</code><em> elements from </em><code>nums</code>.</p>

<p>A <b>subarray</b> is a contiguous, possibly empty sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,3,1,3], k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> It&#39;s optimal to delete the elements at index 2 and index 4.
After deleting them, nums becomes equal to [1, 3, 3, 3].
The longest equal subarray starts at i = 1 and ends at j = 3 with length equal to 3.
It can be proven that no longer equal subarrays can be created.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2,2,1,1], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> It&#39;s optimal to delete the elements at index 2 and index 3.
After deleting them, nums becomes equal to [1, 1, 1, 1].
The array itself is an equal subarray, so the answer is 4.
It can be proven that no longer equal subarrays can be created.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Hash Table + Two Pointers

We use two pointers to maintain a monotonically variable length window, and a hash table to maintain the number of occurrences of each element in the window.

The number of all elements in the window minus the number of the most frequently occurring element in the window is the number of elements that need to be deleted from the window.

Each time, we add the element pointed to by the right pointer to the window, then update the hash table, and also update the number of the most frequently occurring element in the window. When the number of elements that need to be deleted from the window exceeds $k$, we move the left pointer once, and then update the hash table.

After the traversal, return the number of the most frequently occurring element.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        l = 0
        mx = 0
        for r, x in enumerate(nums):
            cnt[x] += 1
            mx = max(mx, cnt[x])
            if r - l + 1 - mx > k:
                cnt[nums[l]] -= 1
                l += 1
        return mx
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- source:start -->

### Solution 2: Hash Table + Two Pointers (Method 2)

We can use a hash table $g$ to maintain the index list of each element.

Next, we enumerate each element as the equal value element. We take out the index list $ids$ of this element from the hash table $g$. Then we define two pointers $l$ and $r$ to maintain a window, so that the number of elements in the window minus the number of equal value elements does not exceed $k$. Therefore, we only need to find the largest window that meets the condition.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Where $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        g = defaultdict(list)
        for i, x in enumerate(nums):
            g[x].append(i)
        ans = 0
        for ids in g.values():
            l = 0
            for r in range(len(ids)):
                while ids[r] - ids[l] - (r - l) > k:
                    l += 1
                ans = max(ans, r - l + 1)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
