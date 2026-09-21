---
comments: true
difficulty: Hard
rating: 2476
source: Biweekly Contest 37 Q4
tags:
    - Design
    - Segment Tree
    - Math
    - Number Theory
    - Fermat's Little Theorem
---

<!-- problem:start -->

# [1622. Fancy Sequence](https://leetcode.com/problems/fancy-sequence)

## Description

<!-- description:start -->

<p>Write an API that generates fancy sequences using the <code>append</code>, <code>addAll</code>, and <code>multAll</code> operations.</p>

<p>Implement the <code>Fancy</code> class:</p>

<ul>
	<li><code>Fancy()</code> Initializes the object with an empty sequence.</li>
	<li><code>void append(val)</code> Appends an integer <code>val</code> to the end of the sequence.</li>
	<li><code>void addAll(inc)</code> Increments all existing values in the sequence by an integer <code>inc</code>.</li>
	<li><code>void multAll(m)</code> Multiplies all existing values in the sequence by an integer <code>m</code>.</li>
	<li><code>int getIndex(idx)</code> Gets the current value at index <code>idx</code> (0-indexed) of the sequence <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>. If the index is greater or equal than the length of the sequence, return <code>-1</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;Fancy&quot;, &quot;append&quot;, &quot;addAll&quot;, &quot;append&quot;, &quot;multAll&quot;, &quot;getIndex&quot;, &quot;addAll&quot;, &quot;append&quot;, &quot;multAll&quot;, &quot;getIndex&quot;, &quot;getIndex&quot;, &quot;getIndex&quot;]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
<strong>Output</strong>
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

<strong>Explanation</strong>
Fancy fancy = new Fancy();
fancy.append(2);   // fancy sequence: [2]
fancy.addAll(3);   // fancy sequence: [2+3] -&gt; [5]
fancy.append(7);   // fancy sequence: [5, 7]
fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -&gt; [10, 14]
fancy.getIndex(0); // return 10
fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -&gt; [13, 17]
fancy.append(10);  // fancy sequence: [13, 17, 10]
fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -&gt; [26, 34, 20]
fancy.getIndex(0); // return 26
fancy.getIndex(1); // return 34
fancy.getIndex(2); // return 20
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= val, inc, m &lt;= 100</code></li>
	<li><code>0 &lt;= idx &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>10<sup>5</sup></code> calls total will be made to <code>append</code>, <code>addAll</code>, <code>multAll</code>, and <code>getIndex</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Segment Tree

<!-- thinking:start -->

> **Thinking**
>
> We keep appending values, then add or multiply every value already in the sequence, and query one index. There are up to $10^5$ operations, so scanning the whole sequence each time is too slow.
>
> Both updates hit the prefix that is already present, and a query asks for a single position, so a segment tree fits. Each node stores the range sum and the pending multiply and add that have not been pushed to its children.
>
> The length is at most $10^5$, so we create nodes on demand over $[1,10^5]$. `append` updates one point, `addAll` and `multAll` update the current prefix, and `getIndex` reads one point, all modulo $10^9+7$.

<!-- thinking:end -->

By the problem statement, `append` inserts a number at the end, `addAll` adds the same value to every current number, `multAll` multiplies every current number by the same value, and `getIndex` reads one position. That is range add, range multiply, and a point query, which a segment tree can maintain.

Each node stores:

- `v`: the sum of the numbers in this range;
- `mul`: a pending multiply not yet pushed to the children, initially $1$;
- `add`: a pending add not yet pushed to the children, initially $0$.

The two tags mean: every number in the range should first be multiplied by `mul`, then increased by `add`. If two updates land on the same range, we merge the tags instead of walking to the leaves. After “multiply by $m_1$ then add $a_1$” and “multiply by $m_2$ then add $a_2$”:

$$
(x \cdot m_1 + a_1)\cdot m_2 + a_2 = x\cdot (m_1 m_2) + (a_1 m_2 + a_2)
$$

so the new multiply is $m_1 m_2$ and the new add is $a_1 m_2 + a_2$.

Hence, multiplying a range by $m$ multiplies the node’s `v`, `mul`, and `add` by $m$; adding $inc$ increases `v` by $\textit{length} \times inc$ and `add` by $inc$. Pushing down applies the same “multiply then add” rule to both children. In the code, add and multiply are one operation: add-only is “multiply by $1$ then add $inc$”, and multiply-only is “multiply by $m$ then add $0$”.

Indices are $1$-based and the length is at most $10^5$, so we create nodes over $[1,10^5]$ on demand. `append` increments $n$ and adds $val$ at position $n$; `addAll` and `multAll` update $[1,n]$; `getIndex` queries position $idx+1$. All arithmetic is modulo $10^9+7$.

The time complexity is $O(m \log n)$, and the space complexity is $O(m \log n)$, where $m$ is the number of operations and $n \le 10^5$ is the length bound.

<!-- tabs:start -->

#### Python3

```python
MOD = 10**9 + 7

class Node:
    __slots__ = "left", "right", "l", "r", "mid", "v", "add", "mul"

    def __init__(self, l, r):
        self.left = self.right = None
        self.l, self.r = l, r
        self.mid = (l + r) >> 1
        self.v = self.add = 0
        self.mul = 1

class SegmentTree:
    def __init__(self):
        self.root = Node(1, 10**5 + 1)

    def modify(self, l, r, mul, add, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            self.apply(node, mul, add)
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modify(l, r, mul, add, node.left)
        if r > node.mid:
            self.modify(l, r, mul, add, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = 0
        if l <= node.mid:
            v = (v + self.query(l, r, node.left)) % MOD
        if r > node.mid:
            v = (v + self.query(l, r, node.right)) % MOD
        return v

    def apply(self, node, mul, add):
        node.v = (node.v * mul + (node.r - node.l + 1) * add) % MOD
        node.add = (node.add * mul + add) % MOD
        node.mul = node.mul * mul % MOD

    def pushup(self, node):
        node.v = (node.left.v + node.right.v) % MOD

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)
        if node.add or node.mul != 1:
            self.apply(node.left, node.mul, node.add)
            self.apply(node.right, node.mul, node.add)
            node.add = 0
            node.mul = 1

class Fancy:
    def __init__(self):
        self.n = 0
        self.tree = SegmentTree()

    def append(self, val: int) -> None:
        self.n += 1
        self.tree.modify(self.n, self.n, 1, val)

    def addAll(self, inc: int) -> None:
        self.tree.modify(1, self.n, 1, inc)

    def multAll(self, m: int) -> None:
        self.tree.modify(1, self.n, m, 0)

    def getIndex(self, idx: int) -> int:
        return -1 if idx >= self.n else self.tree.query(idx + 1, idx + 1)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Math + Modular Inverse

<!-- thinking:start -->

> **Thinking**
>
> The segment tree still walks $O(\log n)$ nodes on every update. `addAll` and `multAll` always hit every number already in the sequence, and a newly appended number is not changed by earlier adds or multiplies.
>
> So every number already present will go through the same later adds and multiplies. We only need two global variables: how much those numbers should still be multiplied by, and how much should then be added. The array stores the value before those operations; a query multiplies and adds to recover the true value. The modulus is prime, so division by $a$ becomes multiplication by the modular inverse (Fermat’s little theorem).

<!-- thinking:end -->

Every `addAll` and `multAll` applies to all numbers that exist at that moment, and a number appended later is not affected by earlier updates. Therefore the pending multiply and add for every current number can be described by two global variables: multiply by $a$, then add $b$. Initially $a=1$ and $b=0$.

The array `nums` does not store the current true values. It stores the values before multiplying by $a$ and adding $b$, so that at any time

$$
\text{true value} = (a \times \textit{nums}[i] + b) \bmod (10^9+7)
$$

The operations then become:

- `append(val)`: this new number has not gone through the current $a$ and $b$, so we store an $x$ with $a \times x + b = \textit{val}$, i.e. $x = (\textit{val} - b) \times a^{-1}$;
- `addAll(inc)`: every true value increases by $inc$, so we add $inc$ to $b$;
- `multAll(m)`: every true value is multiplied by $m$, so both $a$ and $b$ are multiplied by $m$;
- `getIndex(idx)`: return $-1$ if the index is out of range, otherwise $a \times \textit{nums}[idx] + b$.

Here $a^{-1}$ is the modular inverse of $a$ modulo $10^9+7$. The modulus is prime, so Fermat’s little theorem gives $a^{-1} \equiv a^{MOD-2} \pmod{MOD}$.

All operations except the inverse in `append` run in $O(1)$ time; the inverse is $O(\log MOD)$. The space complexity is $O(n)$.

<!-- tabs:start -->

#### Python3

```python
class Fancy:
    def __init__(self):
        self.mod = 10**9 + 7
        self.nums = []
        self.a = 1
        self.b = 0

    def append(self, val: int) -> None:
        x = (val - self.b) * pow(self.a, self.mod - 2, self.mod) % self.mod
        self.nums.append(x)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a = self.a * m % self.mod
        self.b = self.b * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        return (self.a * self.nums[idx] + self.b) % self.mod
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
