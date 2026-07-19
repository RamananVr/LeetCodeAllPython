---
comments: true
difficulty: Hard
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0600-0699/0691.Stickers%20to%20Spell%20Word/README_EN.md
tags:
    - Bit Manipulation
    - Memoization
    - Array
    - Hash Table
    - String
    - Dynamic Programming
    - Backtracking
    - Bitmask
---

<!-- problem:start -->

# [691. Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word)

## Description

<!-- description:start -->

<p>We are given <code>n</code> different types of <code>stickers</code>. Each sticker has a lowercase English word on it.</p>

<p>You would like to spell out the given string <code>target</code> by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.</p>

<p>Return <em>the minimum number of stickers that you need to spell out </em><code>target</code>. If the task is impossible, return <code>-1</code>.</p>

<p><strong>Note:</strong> In all test cases, all words were chosen randomly from the <code>1000</code> most common US English words, and <code>target</code> was chosen as a concatenation of two random words.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> stickers = [&quot;with&quot;,&quot;example&quot;,&quot;science&quot;], target = &quot;thehat&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>
We can use 2 &quot;with&quot; stickers, and 1 &quot;example&quot; sticker.
After cutting and rearrange the letters of those stickers, we can form the target &quot;thehat&quot;.
Also, this is the minimum number of stickers necessary to form the target string.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> stickers = [&quot;notice&quot;,&quot;possible&quot;], target = &quot;basicbasic&quot;
<strong>Output:</strong> -1
Explanation:
We cannot form the target &quot;basicbasic&quot; from cutting letters from the given stickers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == stickers.length</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= stickers[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= target.length &lt;= 15</code></li>
	<li><code>stickers[i]</code> and <code>target</code> consist of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: BFS + State Compression

We notice that the length of the string `target` does not exceed 15. We can use a binary number of length 15 to represent whether each character of `target` has been spelled out. If the $i$th bit is 1, it means that the $i$th character of `target` has been spelled out; otherwise, it has not been spelled out.

We define an initial state 0, which means that all characters have not been spelled out. Then we use the Breadth-First Search (BFS) method, starting from the initial state. Each time we search, we enumerate all the stickers. For each sticker, we try to spell out each character of `target`. If we spell out a character, we set the $i$th bit of the corresponding binary number to 1, indicating that the character has been spelled out. Then we continue to search until we spell out all the characters of `target`.

The time complexity is $O(2^n \times m \times (l + n))$, and the space complexity is $O(2^n)$. Where $n$ is the length of the string `target`, and $m$ and $l$ are the number of stickers and the average length of the stickers, respectively.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        q = deque([0])
        vis = [False] * (1 << n)
        vis[0] = True
        ans = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == (1 << n) - 1:
                    return ans
                for s in stickers:
                    cnt = Counter(s)
                    nxt = cur
                    for i, c in enumerate(target):
                        if (cur >> i & 1) == 0 and cnt[c] > 0:
                            cnt[c] -= 1
                            nxt |= 1 << i
                    if not vis[nxt]:
                        vis[nxt] = True
                        q.append(nxt)
            ans += 1
        return -1
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
