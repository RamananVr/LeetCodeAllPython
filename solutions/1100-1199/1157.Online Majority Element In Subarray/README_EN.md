---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1157.Online%20Majority%20Element%20In%20Subarray/README_EN.md
rating: 2205
source: Weekly Contest 149 Q4
tags:
    - Design
    - Binary Indexed Tree
    - Segment Tree
    - Array
    - Binary Search
---

<!-- problem:start -->

# [1157. Online Majority Element In Subarray](https://leetcode.com/problems/online-majority-element-in-subarray)

## Description

<!-- description:start -->

<p>Design a data structure that efficiently finds the <strong>majority element</strong> of a given subarray.</p>

<p>The <strong>majority element</strong> of a subarray is an element that occurs <code>threshold</code> times or more in the subarray.</p>

<p>Implementing the <code>MajorityChecker</code> class:</p>

<ul>
	<li><code>MajorityChecker(int[] arr)</code> Initializes the instance of the class with the given array <code>arr</code>.</li>
	<li><code>int query(int left, int right, int threshold)</code> returns the element in the subarray <code>arr[left...right]</code> that occurs at least <code>threshold</code> times, or <code>-1</code> if no such element exists.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MajorityChecker&quot;, &quot;query&quot;, &quot;query&quot;, &quot;query&quot;]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
<strong>Output</strong>
[null, 1, -1, 2]

<strong>Explanation</strong>
MajorityChecker majorityChecker = new MajorityChecker([1, 1, 2, 2, 1, 1]);
majorityChecker.query(0, 5, 4); // return 1
majorityChecker.query(0, 3, 3); // return -1
majorityChecker.query(2, 3, 2); // return 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= left &lt;= right &lt; arr.length</code></li>
	<li><code>threshold &lt;= right - left + 1</code></li>
	<li><code>2 * threshold &gt; right - left + 1</code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>query</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Segment Tree + Boyer-Moore Voting Algorithm + Binary Search

We notice that the problem requires us to find the possible majority element in a specific interval, so we consider using a segment tree to maintain the candidate majority element and its occurrence in each interval.

We define each node of the segment tree as `Node`, each node contains the following attributes:

- `l`: The left endpoint of the node, the index starts from $1$.
- `r`: The right endpoint of the node, the index starts from $1$.
- `x`: The candidate majority element of the node.
- `cnt`: The occurrence of the candidate majority element of the node.

The segment tree mainly has the following operations:

- `build(u, l, r)`: Build the segment tree.
- `pushup(u)`: Use the information of the child nodes to update the information of the parent node.
- `query(u, l, r)`: Query the interval sum.

In the initialization method of the main function, we first create a segment tree, and use a hash table $d$ to record all indexes of each element in the array.

In the `query(left, right, threshold)` method, we directly call the `query` method of the segment tree to get the candidate majority element $x$. Then use binary search to find the first index $l$ in the array that is greater than or equal to $left$, and the first index $r$ that is greater than $right$. If $r - l \ge threshold$, return $x$, otherwise return $-1$.

In terms of time complexity, the time complexity of the initialization method is $O(n)$, and the time complexity of the query method is $O(\log n)$. The space complexity is $O(n)$. Here, $n$ is the length of the array.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = ("l", "r", "x", "cnt")

    def __init__(self):
        self.l = self.r = 0
        self.x = self.cnt = 0

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l, self.tr[u].r = l, r
        if l == r:
            self.tr[u].x = self.nums[l - 1]
            self.tr[u].cnt = 1
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.pushup(u)

    def query(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].x, self.tr[u].cnt
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if r <= mid:
            return self.query(u << 1, l, r)
        if l > mid:
            return self.query(u << 1 | 1, l, r)
        x1, cnt1 = self.query(u << 1, l, r)
        x2, cnt2 = self.query(u << 1 | 1, l, r)
        if x1 == x2:
            return x1, cnt1 + cnt2
        if cnt1 >= cnt2:
            return x1, cnt1 - cnt2
        else:
            return x2, cnt2 - cnt1

    def pushup(self, u):
        if self.tr[u << 1].x == self.tr[u << 1 | 1].x:
            self.tr[u].x = self.tr[u << 1].x
            self.tr[u].cnt = self.tr[u << 1].cnt + self.tr[u << 1 | 1].cnt
        elif self.tr[u << 1].cnt >= self.tr[u << 1 | 1].cnt:
            self.tr[u].x = self.tr[u << 1].x
            self.tr[u].cnt = self.tr[u << 1].cnt - self.tr[u << 1 | 1].cnt
        else:
            self.tr[u].x = self.tr[u << 1 | 1].x
            self.tr[u].cnt = self.tr[u << 1 | 1].cnt - self.tr[u << 1].cnt

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.tree = SegmentTree(arr)
        self.d = defaultdict(list)
        for i, x in enumerate(arr):
            self.d[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        x, _ = self.tree.query(1, left + 1, right + 1)
        l = bisect_left(self.d[x], left)
        r = bisect_left(self.d[x], right + 1)
        return x if r - l >= threshold else -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
