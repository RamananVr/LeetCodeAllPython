---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/1200-1299/1286.Iterator%20for%20Combination/README_EN.md
rating: 1591
source: Biweekly Contest 15 Q3
tags:
    - Design
    - String
    - Backtracking
    - Iterator
---

<!-- problem:start -->

# [1286. Iterator for Combination](https://leetcode.com/problems/iterator-for-combination)

## Description

<!-- description:start -->

<p>Design the <code>CombinationIterator</code> class:</p>

<ul>
	<li><code>CombinationIterator(string characters, int combinationLength)</code> Initializes the object with a string <code>characters</code> of <strong>sorted distinct</strong> lowercase English letters and a number <code>combinationLength</code> as arguments.</li>
	<li><code>next()</code> Returns the next combination of length <code>combinationLength</code> in <strong>lexicographical order</strong>.</li>
	<li><code>hasNext()</code> Returns <code>true</code> if and only if there exists a next combination.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;CombinationIterator&quot;, &quot;next&quot;, &quot;hasNext&quot;, &quot;next&quot;, &quot;hasNext&quot;, &quot;next&quot;, &quot;hasNext&quot;]
[[&quot;abc&quot;, 2], [], [], [], [], [], []]
<strong>Output</strong>
[null, &quot;ab&quot;, true, &quot;ac&quot;, true, &quot;bc&quot;, false]

<strong>Explanation</strong>
CombinationIterator itr = new CombinationIterator(&quot;abc&quot;, 2);
itr.next();    // return &quot;ab&quot;
itr.hasNext(); // return True
itr.next();    // return &quot;ac&quot;
itr.hasNext(); // return True
itr.next();    // return &quot;bc&quot;
itr.hasNext(); // return False
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= combinationLength &lt;= characters.length &lt;= 15</code></li>
	<li>All the characters of <code>characters</code> are <strong>unique</strong>.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>next</code> and <code>hasNext</code>.</li>
	<li>It is guaranteed that all calls of the function <code>next</code> are valid.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- tabs:start -->

#### Python3

```python
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        def dfs(i):
            if len(t) == combinationLength:
                cs.append(''.join(t))
                return
            if i == n:
                return
            t.append(characters[i])
            dfs(i + 1)
            t.pop()
            dfs(i + 1)

        cs = []
        n = len(characters)
        t = []
        dfs(0)
        self.cs = cs
        self.idx = 0

    def next(self) -> str:
        ans = self.cs[self.idx]
        self.idx += 1
        return ans

    def hasNext(self) -> bool:
        return self.idx < len(self.cs)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2

<!-- tabs:start -->

#### Python3

```python
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.curr = (1 << len(characters)) - 1
        self.size = combinationLength
        self.cs = characters[::-1]

    def next(self) -> str:
        while self.curr >= 0 and self.curr.bit_count() != self.size:
            self.curr -= 1
        ans = []
        for i in range(len(self.cs)):
            if (self.curr >> i) & 1:
                ans.append(self.cs[i])
        self.curr -= 1
        return ''.join(ans[::-1])

    def hasNext(self) -> bool:
        while self.curr >= 0 and self.curr.bit_count() != self.size:
            self.curr -= 1
        return self.curr >= 0

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
