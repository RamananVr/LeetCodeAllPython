---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2200-2299/2286.Booking%20Concert%20Tickets%20in%20Groups/README_EN.md
rating: 2470
source: Biweekly Contest 79 Q4
tags:
    - Design
    - Binary Indexed Tree
    - Segment Tree
    - Binary Search
---

<!-- problem:start -->

# [2286. Booking Concert Tickets in Groups](https://leetcode.com/problems/booking-concert-tickets-in-groups)

## Description

<!-- description:start -->

<p>A concert hall has <code>n</code> rows numbered from <code>0</code> to <code>n - 1</code>, each with <code>m</code> seats, numbered from <code>0</code> to <code>m - 1</code>. You need to design a ticketing system that can allocate seats in the following cases:</p>

<ul>
	<li>If a group of <code>k</code> spectators can sit <strong>together</strong> in a row.</li>
	<li>If <strong>every</strong> member of a group of <code>k</code> spectators can get a seat. They may or <strong>may not</strong> sit together.</li>
</ul>

<p>Note that the spectators are very picky. Hence:</p>

<ul>
	<li>They will book seats only if each member of their group can get a seat with row number <strong>less than or equal</strong> to <code>maxRow</code>. <code>maxRow</code> can <strong>vary</strong> from group to group.</li>
	<li>In case there are multiple rows to choose from, the row with the <strong>smallest</strong> number is chosen. If there are multiple seats to choose in the same row, the seat with the <strong>smallest</strong> number is chosen.</li>
</ul>

<p>Implement the <code>BookMyShow</code> class:</p>

<ul>
	<li><code>BookMyShow(int n, int m)</code> Initializes the object with <code>n</code> as number of rows and <code>m</code> as number of seats per row.</li>
	<li><code>int[] gather(int k, int maxRow)</code> Returns an array of length <code>2</code> denoting the row and seat number (respectively) of the <strong>first seat</strong> being allocated to the <code>k</code> members of the group, who must sit <strong>together</strong>. In other words, it returns the smallest possible <code>r</code> and <code>c</code> such that all <code>[c, c + k - 1]</code> seats are valid and empty in row <code>r</code>, and <code>r &lt;= maxRow</code>. Returns <code>[]</code> in case it is <strong>not possible</strong> to allocate seats to the group.</li>
	<li><code>boolean scatter(int k, int maxRow)</code> Returns <code>true</code> if all <code>k</code> members of the group can be allocated seats in rows <code>0</code> to <code>maxRow</code>, who may or <strong>may not</strong> sit together. If the seats can be allocated, it allocates <code>k</code> seats to the group with the <strong>smallest</strong> row numbers, and the smallest possible seat numbers in each row. Otherwise, returns <code>false</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;BookMyShow&quot;, &quot;gather&quot;, &quot;gather&quot;, &quot;scatter&quot;, &quot;scatter&quot;]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
<strong>Output</strong>
[null, [0, 0], [], true, false]

<strong>Explanation</strong>
BookMyShow bms = new BookMyShow(2, 5); // There are 2 rows with 5 seats each 
bms.gather(4, 0); // return [0, 0]
                  // The group books seats [0, 3] of row 0. 
bms.gather(2, 0); // return []
                  // There is only 1 seat left in row 0,
                  // so it is not possible to book 2 consecutive seats. 
bms.scatter(5, 1); // return True
                   // The group books seat 4 of row 0 and seats [0, 3] of row 1. 
bms.scatter(5, 1); // return False
                   // There is only one seat left in the hall.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m, k &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= maxRow &lt;= n - 1</code></li>
	<li>At most <code>5 * 10<sup>4</sup></code> calls <strong>in total</strong> will be made to <code>gather</code> and <code>scatter</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Segment Tree

From the problem description, we can deduce the following:

- For the `gather(k, maxRow)` operation, the goal is to seat $k$ people on the same row with consecutive seats. In other words, we need to find the smallest row where the remaining seats are greater than or equal to $k$.
- For the `scatter(k, maxRow)` operation, we just need to find $k$ seats in total, but we want to minimize the row number. Therefore, we need to find the first row that has more than $0$ seats remaining, allocate seats there, and continue searching for the rest.

We can implement this using a segment tree. Each segment tree node contains the following information:

- `l`: The left endpoint of the node's interval
- `r`: The right endpoint of the node's interval
- `s`: The total remaining seats in the interval corresponding to the node
- `mx`: The maximum remaining seats in the interval corresponding to the node

Note that the index range for the segment tree starts from $1$.

The operations of the segment tree are as follows:

- `build(u, l, r)`: Builds node $u$, corresponding to the interval $[l, r]$, and recursively builds its left and right children.
- `modify(u, x, v)`: Starting from node $u$, finds the first node corresponding to the interval $[l, r]$ where $l = r = x$, and modifies the `s` and `mx` values of this node to $v$, then updates the tree upwards.
- `query_sum(u, l, r)`: Starting from node $u$, calculates the sum of `s` values in the interval $[l, r]$.
- `query_idx(u, l, r, k)`: Starting from node $u$, finds the first node in the interval $[l, r]$ where `mx` is greater than or equal to $k$, and returns the left endpoint `l` of this node. When searching, we start from the largest interval $[1, maxRow]$. Since we need to find the leftmost node with `mx` greater than or equal to $k$, we check whether the `mx` of the first half of the interval meets the condition. If so, the answer is in the first half, and we recursively search that half. Otherwise, the answer is in the second half, and we search that half recursively.
- `pushup(u)`: Updates the information of node $u$ using the information from its children.

For the `gather(k, maxRow)` operation, we first use `query_idx(1, 1, n, k)` to find the first row where the remaining seats are greater than or equal to $k$, denoted as $i$. Then, we use `query_sum(1, i, i)` to get the remaining seats in this row, denoted as $s$. Next, we use `modify(1, i, s - k)` to modify the remaining seats of this row to $s - k$, and update the tree upwards. Finally, we return the result $[i - 1, m - s]$.

For the `scatter(k, maxRow)` operation, we first use `query_sum(1, 1, maxRow)` to calculate the total remaining seats in the first $maxRow$ rows, denoted as $s$. If $s \lt k$, there are not enough seats, so we return `false`. Otherwise, we use `query_idx(1, 1, maxRow, 1)` to find the first row where the remaining seats are greater than or equal to $1$, denoted as $i$. Starting from this row, we use `query_sum(1, i, i)` to get the remaining seats in row $i$, denoted as $s_i$. If $s_i \geq k$, we directly use `modify(1, i, s_i - k)` to modify the remaining seats of this row to $s_i - k$, update the tree upwards, and return `true`. Otherwise, we update $k = k - s_i$, modify the remaining seats of this row to $0$, and update the tree upwards. Finally, we return `true`.

Time complexity:

- The initialization time complexity is $O(n)$.
- The time complexity of `gather(k, maxRow)` is $O(\log n)$.
- The time complexity of `scatter(k, maxRow)` is $O((n + q) \times \log n)$.

The overall time complexity is $O(n + q \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the number of rows, and $q$ is the number of operations.

<!-- tabs:start -->

#### Python3

```python
class Node:
    __slots__ = "l", "r", "s", "mx"

    def __init__(self):
        self.l = self.r = 0
        self.s = self.mx = 0

class SegmentTree:
    def __init__(self, n, m):
        self.m = m
        self.tr = [Node() for _ in range(n << 2)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l, self.tr[u].r = l, r
        if l == r:
            self.tr[u].s = self.tr[u].mx = self.m
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)
        self.pushup(u)

    def modify(self, u, x, v):
        if self.tr[u].l == x and self.tr[u].r == x:
            self.tr[u].s = self.tr[u].mx = v
            return
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if x <= mid:
            self.modify(u << 1, x, v)
        else:
            self.modify(u << 1 | 1, x, v)
        self.pushup(u)

    def query_sum(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].s
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        v = 0
        if l <= mid:
            v += self.query_sum(u << 1, l, r)
        if r > mid:
            v += self.query_sum(u << 1 | 1, l, r)
        return v

    def query_idx(self, u, l, r, k):
        if self.tr[u].mx < k:
            return 0
        if self.tr[u].l == self.tr[u].r:
            return self.tr[u].l
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if self.tr[u << 1].mx >= k:
            return self.query_idx(u << 1, l, r, k)
        if r > mid:
            return self.query_idx(u << 1 | 1, l, r, k)
        return 0

    def pushup(self, u):
        self.tr[u].s = self.tr[u << 1].s + self.tr[u << 1 | 1].s
        self.tr[u].mx = max(self.tr[u << 1].mx, self.tr[u << 1 | 1].mx)

class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.tree = SegmentTree(n, m)

    def gather(self, k: int, maxRow: int) -> List[int]:
        maxRow += 1
        i = self.tree.query_idx(1, 1, maxRow, k)
        if i == 0:
            return []
        s = self.tree.query_sum(1, i, i)
        self.tree.modify(1, i, s - k)
        return [i - 1, self.tree.m - s]

    def scatter(self, k: int, maxRow: int) -> bool:
        maxRow += 1
        if self.tree.query_sum(1, 1, maxRow) < k:
            return False
        i = self.tree.query_idx(1, 1, maxRow, 1)
        for j in range(i, self.n + 1):
            s = self.tree.query_sum(1, j, j)
            if s >= k:
                self.tree.modify(1, j, s - k)
                return True
            k -= s
            self.tree.modify(1, j, 0)
        return True

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
