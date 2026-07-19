---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2000-2099/2032.Two%20Out%20of%20Three/README_EN.md
rating: 1269
source: Weekly Contest 262 Q1
tags:
    - Bit Manipulation
    - Array
    - Hash Table
---

<!-- problem:start -->

# [2032. Two Out of Three](https://leetcode.com/problems/two-out-of-three)

## Description

<!-- description:start -->

Given three integer arrays <code>nums1</code>, <code>nums2</code>, and <code>nums3</code>, return <em>a <strong>distinct</strong> array containing all the values that are present in <strong>at least two</strong> out of the three arrays. You may return the values in <strong>any</strong> order</em>.

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
<strong>Output:</strong> [3,2]
<strong>Explanation:</strong> The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
<strong>Output:</strong> [2,3,1]
<strong>Explanation:</strong> The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
<strong>Output:</strong> []
<strong>Explanation:</strong> No value is present in at least two arrays.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length, nums3.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums1[i], nums2[j], nums3[k] &lt;= 100</code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Array + Enumeration

We can first put each element of the arrays into an array, then enumerate each number $i$ from $1$ to $100$, and check whether $i$ appears in at least two arrays. If so, add $i$ to the answer array.

The time complexity is $O(n_1 + n_2 + n_3)$, and the space complexity is $O(n_1 + n_2 + n_3)$. Here, $n_1, n_2, n_3$ are the lengths of the arrays `nums1`, `nums2`, and `nums3`, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return [i for i in range(1, 101) if (i in s1) + (i in s2) + (i in s3) > 1]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Hash Table + Bit Manipulation

We can use a hash table `mask` to record which arrays each number appears in. For each array, we add its elements to the hash table and set the corresponding bit to `1`. For example, if it is the first array, set the corresponding bit to `1`; if it is the second array, set it to `2`; if it is the third array, set it to `4`.

Finally, we iterate through each number in the hash table and check if its corresponding value has at least two bits set to `1` in binary. If so, add that number to the answer array.

The time complexity is $O(n_1 + n_2 + n_3)$, and the space complexity is $O(n_1 + n_2 + n_3)$, where $n_1, n_2, n_3$ are the lengths of the arrays `nums1`, `nums2`, and `nums3`, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        mask = defaultdict(int)
        for i, nums in enumerate((nums1, nums2, nums3)):
            for x in nums:
                mask[x] |= 1 << i
        return [x for x, v in mask.items() if v & (v - 1)]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
