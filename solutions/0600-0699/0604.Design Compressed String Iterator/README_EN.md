---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0604.Design%20Compressed%20String%20Iterator/README_EN.md
tags:
    - Design
    - Array
    - String
    - Iterator
---

<!-- problem:start -->

# [604. Design Compressed String Iterator 🔒](https://leetcode.com/problems/design-compressed-string-iterator)

## Description

<!-- description:start -->

<p>Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.</p>

<p>Implement the&nbsp;StringIterator class:</p>

<ul>
	<li><code>next()</code>&nbsp;Returns <strong>the next character</strong> if the original string still has uncompressed characters, otherwise returns a <strong>white space</strong>.</li>
	<li><code>hasNext()</code>&nbsp;Returns true if&nbsp;there is any letter needs to be uncompressed in the original string, otherwise returns <code>false</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;StringIterator&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;, &quot;hasNext&quot;, &quot;next&quot;, &quot;hasNext&quot;]
[[&quot;L1e2t1C1o1d1e1&quot;], [], [], [], [], [], [], [], [], []]
<strong>Output</strong>
[null, &quot;L&quot;, &quot;e&quot;, &quot;e&quot;, &quot;t&quot;, &quot;C&quot;, &quot;o&quot;, true, &quot;d&quot;, true]

<strong>Explanation</strong>
StringIterator stringIterator = new StringIterator(&quot;L1e2t1C1o1d1e1&quot;);
stringIterator.next(); // return &quot;L&quot;
stringIterator.next(); // return &quot;e&quot;
stringIterator.next(); // return &quot;e&quot;
stringIterator.next(); // return &quot;t&quot;
stringIterator.next(); // return &quot;C&quot;
stringIterator.next(); // return &quot;o&quot;
stringIterator.hasNext(); // return True
stringIterator.next(); // return &quot;d&quot;
stringIterator.hasNext(); // return True
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;compressedString.length &lt;= 1000</code></li>
	<li><code>compressedString</code> consists of lower-case an upper-case English letters and digits.</li>
	<li>The number of a single character repetitions in&nbsp;<code>compressedString</code> is in the range <code>[1, 10^9]</code></li>
	<li>At most <code>100</code> calls will be made to <code>next</code> and <code>hasNext</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Parsing and Storing

Parse the `compressedString` into characters $c$ and their corresponding repetition counts $x$, and store them in an array or list $d$. Use $p$ to point to the current character.

Then perform operations in `next` and `hasNext`.

The initialization time complexity is $O(n)$, and the time complexity of the other operations is $O(1)$. Here, $n$ is the length of `compressedString`.

<!-- tabs:start -->

#### Python3

```python
class StringIterator:
    def __init__(self, compressedString: str):
        self.d = []
        self.p = 0
        n = len(compressedString)
        i = 0
        while i < n:
            c = compressedString[i]
            x = 0
            i += 1
            while i < n and compressedString[i].isdigit():
                x = x * 10 + int(compressedString[i])
                i += 1
            self.d.append([c, x])

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        ans = self.d[self.p][0]
        self.d[self.p][1] -= 1
        if self.d[self.p][1] == 0:
            self.p += 1
        return ans

    def hasNext(self) -> bool:
        return self.p < len(self.d) and self.d[self.p][1] > 0

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
