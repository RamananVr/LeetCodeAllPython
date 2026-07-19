---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1100-1199/1172.Dinner%20Plate%20Stacks/README_EN.md
rating: 2109
source: Weekly Contest 151 Q4
tags:
    - Stack
    - Design
    - Hash Table
    - Heap (Priority Queue)
---

<!-- problem:start -->

# [1172. Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks)

## Description

<!-- description:start -->

<p>You have an infinite number of stacks arranged in a row and numbered (left to right) from <code>0</code>, each of the stacks has the same maximum capacity.</p>

<p>Implement the <code>DinnerPlates</code> class:</p>

<ul>
	<li><code>DinnerPlates(int capacity)</code> Initializes the object with the maximum capacity of the stacks <code>capacity</code>.</li>
	<li><code>void push(int val)</code> Pushes the given integer <code>val</code> into the leftmost stack with a size less than <code>capacity</code>.</li>
	<li><code>int pop()</code> Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns <code>-1</code> if all the stacks are empty.</li>
	<li><code>int popAtStack(int index)</code> Returns the value at the top of the stack with the given index <code>index</code> and removes it from that stack or returns <code>-1</code> if the stack with that given index is empty.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;DinnerPlates&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;push&quot;, &quot;popAtStack&quot;, &quot;push&quot;, &quot;push&quot;, &quot;popAtStack&quot;, &quot;popAtStack&quot;, &quot;pop&quot;, &quot;pop&quot;, &quot;pop&quot;, &quot;pop&quot;, &quot;pop&quot;]
[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
<strong>Output</strong>
[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]

<strong>Explanation:</strong> 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
D.pop()            // Returns 3.  The stacks are now:   1 
                                                        ﹈   
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= val &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= index &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>push</code>, <code>pop</code>, and <code>popAtStack</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Stack Array + Ordered Set

We define the following data structures or variables:

- `capacity`: The capacity of each stack;
- `stacks`: Stack array, used to store all stacks, each with a maximum capacity of `capacity`;
- `not_full`: Ordered set, used to store the indices of all non-full stacks in the stack array.

For the `push(val)` operation:

- We first check if `not_full` is empty. If it is, it means there are no non-full stacks, so we need to create a new stack and push `val` into it. At this point, we check if the capacity `capacity` is greater than $1$. If it is, we add the index of this stack to `not_full`.
- If `not_full` is not empty, it means there are non-full stacks. We take out the smallest index `index` from `not_full`, and push `val` into `stacks[index]`. At this point, if the capacity of `stacks[index]` equals `capacity`, we remove `index` from `not_full`.

For the `popAtStack(index)` operation:

- We first check if `index` is within the index range of `stacks`. If it is not, we directly return $-1$. If `stacks[index]` is empty, we also directly return $-1$.
- If `stacks[index]` is not empty, we pop the top element `val` from `stacks[index]`. If `index` equals the length of `stacks` minus $1$, it means `stacks[index]` is the last stack. If it is empty, we loop to remove the index of the last stack from `not_full`, and remove the last stack from the stack array `stacks`, until the last stack is not empty, or the stack array `stacks` is empty. Otherwise, if `stacks[index]` is not the last stack, we add `index` to `not_full`.
- Finally, return `val`.

For the `pop()` operation:

- We directly call `popAtStack(stacks.length - 1)`.

The time complexity is $(n \times \log n)$, and the space complexity is $O(n)$. Here, $n$ is the number of operations.

<!-- tabs:start -->

#### Python3

```python
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.not_full = SortedSet()

    def push(self, val: int) -> None:
        if not self.not_full:
            self.stacks.append([val])
            if self.capacity > 1:
                self.not_full.add(len(self.stacks) - 1)
        else:
            index = self.not_full[0]
            self.stacks[index].append(val)
            if len(self.stacks[index]) == self.capacity:
                self.not_full.discard(index)

    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if index == len(self.stacks) - 1 and not self.stacks[-1]:
            while self.stacks and not self.stacks[-1]:
                self.not_full.discard(len(self.stacks) - 1)
                self.stacks.pop()
        else:
            self.not_full.add(index)
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
