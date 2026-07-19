---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2600-2699/2612.Minimum%20Reverse%20Operations/README_EN.md
rating: 2824
source: Weekly Contest 339 Q4
tags:
    - Breadth-First Search
    - Union Find
    - Array
    - Hash Table
    - Ordered Set
---

<!-- problem:start -->

# [2612. Minimum Reverse Operations](https://leetcode.com/problems/minimum-reverse-operations)

## Description

<!-- description:start -->

<p>You are given an integer <code>n</code> and an integer <code>p</code> representing an array <code>arr</code> of length <code>n</code> where all elements are set to 0&#39;s, except position <code>p</code> which is set to 1. You are also given an integer array <code>banned</code> containing restricted positions. Perform the following operation on <code>arr</code>:</p>

<ul>
	<li>Reverse a <span data-keyword="subarray-nonempty"><strong>subarray</strong></span> with size <code>k</code> if the single 1 is not set to a position in <code>banned</code>.</li>
</ul>

<p>Return an integer array <code>answer</code> with <code>n</code> results where the <code>i<sup>th</sup></code> result is<em> </em>the <strong>minimum</strong> number of operations needed to bring the single 1 to position <code>i</code> in <code>arr</code>, or -1 if it is impossible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, p = 0, banned = [1,2], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,-1,-1,1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Initially 1 is placed at position 0 so the number of operations we need for position 0 is 0.</li>
	<li>We can never place 1 on the banned positions, so the answer for positions 1 and 2 is -1.</li>
	<li>Perform the operation of size 4 to reverse the whole array.</li>
	<li>After a single operation 1 is at position 3 so the answer for position 3 is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, p = 0, banned = [2,4], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,-1,-1,-1,-1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Initially 1 is placed at position 0 so the number of operations we need for position 0 is 0.</li>
	<li>We cannot perform the operation on the subarray positions <code>[0, 2]</code> because position 2 is in banned.</li>
	<li>Because 1 cannot be set at position 2, it is impossible to set 1 at other positions in more operations.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, p = 2, banned = [0,1,3], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,-1,0,-1]</span></p>

<p><strong>Explanation:</strong></p>

<p>Perform operations of size 1 and 1 never changes its position.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= p &lt;= n - 1</code></li>
	<li><code>0 &lt;= banned.length &lt;= n - 1</code></li>
	<li><code>0 &lt;= banned[i] &lt;= n - 1</code></li>
	<li><code>1 &lt;= k &lt;= n&nbsp;</code></li>
	<li><code>banned[i] != p</code></li>
	<li>all values in <code>banned</code>&nbsp;are <strong>unique</strong>&nbsp;</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Ordered Set + BFS

We notice that for any index $i$ in the subarray interval $[l,..r]$, the flipped index $j = l + r - i$.

If the subarray moves one position to the right, then $j = l + 1 + r + 1 - i = l + r - i + 2$, that is, $j$ will increase by $2$.

Similarly, if the subarray moves one position to the left, then $j = l - 1 + r - 1 - i = l + r - i - 2$, that is, $j$ will decrease by $2$.

Therefore, for a specific index $i$, all its flipped indices form an arithmetic progression with common difference $2$, that is, all the flipped indices have the same parity.

Next, we consider the range of values ​​of the index $i$ after flipping $j$.

- If the boundary is not considered, the range of values ​​of $j$ is $[i - k + 1, i + k - 1]$.
- If the subarray is on the left, then $[l, r] = [0, k - 1]$, so the flipped index $j$ of $i$ is $0 + k - 1 - i$, that is, $j = k - i - 1$, so the left boundary $mi = max(i - k + 1, k - i - 1)$.
- If the subarray is on the right, then $[l, r] = [n - k, n - 1]$, so the flipped index $j= n - k + n - 1 - i$ is $j = n \times 2 - k - i - 1$, so the right boundary of $j$ is $mx = min(i + k - 1, n \times 2 - k - i - 1)$.

We use two ordered sets to store all the odd indices and even indices to be searched, here we need to exclude the indices in the array $banned$ and the index $p$.

Then we use BFS to search, each time searching all the flipped indices $j$ of the current index $i$, that is, $j = mi, mi + 2, mi + 4, \dots, mx$, updating the answer of index $j$ and adding index $j$ to the search queue, and removing index $j$ from the corresponding ordered set.

When the search is over, the answer to all indices can be obtained.

The time complexity is $O(n \times \log n)$ and the space complexity is $O(n)$. Where $n$ is the given array length in the problem.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minReverseOperations(
        self, n: int, p: int, banned: List[int], k: int
    ) -> List[int]:
        ans = [-1] * n
        ans[p] = 0
        ts = [SortedSet() for _ in range(2)]
        for i in range(n):
            ts[i % 2].add(i)
        ts[p % 2].remove(p)
        for i in banned:
            ts[i % 2].remove(i)
        ts[0].add(n)
        ts[1].add(n)
        q = deque([p])
        while q:
            i = q.popleft()
            mi = max(i - k + 1, k - i - 1)
            mx = min(i + k - 1, n * 2 - k - i - 1)
            s = ts[mi % 2]
            j = s.bisect_left(mi)
            while s[j] <= mx:
                q.append(s[j])
                ans[s[j]] = ans[i] + 1
                s.remove(s[j])
                j = s.bisect_left(mi)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
