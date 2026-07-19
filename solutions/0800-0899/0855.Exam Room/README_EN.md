---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0800-0899/0855.Exam%20Room/README_EN.md
tags:
    - Design
    - Ordered Set
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [855. Exam Room](https://leetcode.com/problems/exam-room)

## Description

<!-- description:start -->

<p>There is an exam room with <code>n</code> seats in a single row labeled from <code>0</code> to <code>n - 1</code>.</p>

<p>When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number <code>0</code>.</p>

<p>Design a class that simulates the mentioned exam room.</p>

<p>Implement the <code>ExamRoom</code> class:</p>

<ul>
	<li><code>ExamRoom(int n)</code> Initializes the object of the exam room with the number of the seats <code>n</code>.</li>
	<li><code>int seat()</code> Returns the label of the seat at which the next student will set.</li>
	<li><code>void leave(int p)</code> Indicates that the student sitting at seat <code>p</code> will leave the room. It is guaranteed that there will be a student sitting at seat <code>p</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;ExamRoom&quot;, &quot;seat&quot;, &quot;seat&quot;, &quot;seat&quot;, &quot;seat&quot;, &quot;leave&quot;, &quot;seat&quot;]
[[10], [], [], [], [], [4], []]
<strong>Output</strong>
[null, 0, 9, 4, 2, null, 5]

<strong>Explanation</strong>
ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
examRoom.seat(); // return 9, the student sits at the last seat number 9.
examRoom.seat(); // return 4, the student sits at the last seat number 4.
examRoom.seat(); // return 2, the student sits at the last seat number 2.
examRoom.leave(4);
examRoom.seat(); // return 5, the student sits at the last seat number 5.

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li>It is guaranteed that there is a student sitting at seat <code>p</code>.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>seat</code> and <code>leave</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Ordered Set + Hash Table

Considering that each time we call $\text{seat}()$, we need to find the seat with the maximum distance, we can use an ordered set to store seat intervals. Each element of the ordered set is a tuple $(l, r)$, indicating that the seats between $l$ and $r$ (excluding $l$ and $r$) can be occupied by a student. Initially, the ordered set contains only one element $(-1, n)$, indicating that the seats between $(-1, n)$ can be occupied by a student.

Additionally, we use two hash tables $\textit{left}$ and $\textit{right}$ to maintain the left and right neighbors of each occupied seat, making it easier to merge two seat intervals when calling $\text{leave}(p)$.

The time complexity is $O(\log n)$, and the space complexity is $O(n)$. Here, $n$ is the number of seats in the exam room.

<!-- tabs:start -->

#### Python3

```python
class ExamRoom:
    def __init__(self, n: int):
        def dist(x):
            l, r = x
            return r - l - 1 if l == -1 or r == n else (r - l) >> 1

        self.n = n
        self.ts = SortedList(key=lambda x: (-dist(x), x[0]))
        self.left = {}
        self.right = {}
        self.add((-1, n))

    def seat(self) -> int:
        s = self.ts[0]
        p = (s[0] + s[1]) >> 1
        if s[0] == -1:
            p = 0
        elif s[1] == self.n:
            p = self.n - 1
        self.delete(s)
        self.add((s[0], p))
        self.add((p, s[1]))
        return p

    def leave(self, p: int) -> None:
        l, r = self.left[p], self.right[p]
        self.delete((l, p))
        self.delete((p, r))
        self.add((l, r))

    def add(self, s):
        self.ts.add(s)
        self.left[s[1]] = s[0]
        self.right[s[0]] = s[1]

    def delete(self, s):
        self.ts.remove(s)
        self.left.pop(s[1])
        self.right.pop(s[0])

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
