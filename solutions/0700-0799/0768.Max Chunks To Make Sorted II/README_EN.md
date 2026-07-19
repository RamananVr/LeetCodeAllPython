---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0700-0799/0768.Max%20Chunks%20To%20Make%20Sorted%20II/README_EN.md
tags:
    - Stack
    - Greedy
    - Array
    - Sorting
    - Monotonic Stack
---

<!-- problem:start -->

# [768. Max Chunks To Make Sorted II](https://leetcode.com/problems/max-chunks-to-make-sorted-ii)

## Description

<!-- description:start -->

<p>You are given an integer array <code>arr</code>.</p>

<p>We split <code>arr</code> into some number of <strong>chunks</strong> (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.</p>

<p>Return <em>the largest number of chunks we can make to sort the array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [5,4,3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn&#39;t sorted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,1,3,4,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 2000</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>8</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Monotonic Stack

According to the problem, we can find that from left to right, each chunk has a maximum value, and these maximum values are monotonically increasing (non-strictly increasing). We can use a stack to store these maximum values of the chunks. The size of the final stack is the maximum number of chunks that can be sorted.

Time complexity is $O(n)$, where $n$ represents the length of $\textit{arr}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stk = []
        for v in arr:
            if not stk or v >= stk[-1]:
                stk.append(v)
            else:
                mx = stk.pop()
                while stk and stk[-1] > v:
                    stk.pop()
                stk.append(mx)
        return len(stk)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Prefix Maximums + Suffix Minimums

We would like to partition the array of length $n$ into several chunks such that
after sorting each chunk individually, the entire array remains sorted.

Consider two adjacent chunks:

- left chunk: `left_chunk`
- right chunk: `right_chunk`

If the following condition holds:

`max(left_chunk)` <= `min(right_chunk)`

it means:

- every element in the left chunk is less than or equal to every element in the right chunk
- therefore, after sorting both chunks independently, they can still be concatenated into a globally sorted array

Thus, for every index $i$ satisfying:

$$
1 \le i < n
$$

we check whether:

$$
\max(arr[:i]) \le \min(arr[i:])
$$

holds.

If true, then index $i$ can serve as a valid partition point.

---

To efficiently evaluate the above condition, we preprocess:

- `prefix_maxs[j]`

which represents:

$$
\max(arr[:j + 1])
$$

i.e. the prefix maximum.

- `suffix_min[j]`

which represents:

$$
\min(arr[j:])
$$

i.e. the suffix minimum.

Next:

1. Traverse the array from left to right to compute all prefix maximums
2. Traverse the array from right to left to compute all suffix minimums
3. For each index $i$, check whether:

`prefix_maxs[i - 1]` <= `suffix_min[i]`

holds.

If true, then:

- every element on the left side is less than or equal to every element on the right side
- therefore, the array can be partitioned at index $i$

Finally, count all valid partition points.

Note that:

Even if the array is strictly decreasing, the entire array itself can still be treated as one valid chunk.

Therefore, our final answer is equal to all valid partition points + $1$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ represents the length of $\textit{arr}$.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        prefix_maxs = []  # Max of each arr[:i + 1] where 0 <= i < len(arr).

        for num in arr:
            if not prefix_maxs:
                prefix_maxs.append(num)
                continue

            prefix_maxs.append(max(num, prefix_maxs[-1]))

        max_chunks = 1  # Base case.
        suffix_min = arr[-1]  # Min of arr[i:] where 0 <= i < len(arr).

        for idx in range(len(arr) - 1, 0, -1):
            if arr[idx] < suffix_min:
                suffix_min = arr[idx]

            if prefix_maxs[idx - 1] <= suffix_min:
                max_chunks += 1

        return max_chunks
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
