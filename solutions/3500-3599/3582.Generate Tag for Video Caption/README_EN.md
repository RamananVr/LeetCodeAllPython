---
comments: true
difficulty: Easy
edit_url: https://github.com/doocs/leetcode/edit/main/solution/3500-3599/3582.Generate%20Tag%20for%20Video%20Caption/README_EN.md
rating: 1316
source: Weekly Contest 454 Q1
tags:
    - String
    - Simulation
---

<!-- problem:start -->

# [3582. Generate Tag for Video Caption](https://leetcode.com/problems/generate-tag-for-video-caption)

## Description

<!-- description:start -->

<p>You are given a string <code><font face="monospace">caption</font></code> representing the caption for a video.</p>

<p>The following actions must be performed <strong>in order</strong> to generate a <strong>valid tag</strong> for the video:</p>

<ol>
	<li>
	<p><strong>Combine all words</strong> in the string into a single <em>camelCase string</em> prefixed with <code>&#39;#&#39;</code>. A <em>camelCase string</em> is one where the first letter of all words <em>except</em> the first one is capitalized. All characters after the first character in <strong>each</strong> word must be lowercase.</p>
	</li>
	<li>
	<p><b>Remove</b> all characters that are not an English letter, <strong>except</strong> the first <code>&#39;#&#39;</code>.</p>
	</li>
	<li>
	<p><strong>Truncate</strong> the result to a maximum of 100 characters.</p>
	</li>
</ol>

<p>Return the <strong>tag</strong> after performing the actions on <code>caption</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">caption = &quot;Leetcode daily streak achieved&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;#leetcodeDailyStreakAchieved&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The first letter for all words except <code>&quot;leetcode&quot;</code> should be capitalized.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">caption = &quot;can I Go There&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;#canIGoThere&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The first letter for all words except <code>&quot;can&quot;</code> should be capitalized.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">caption = &quot;hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Since the first word has length 101, we need to truncate the last two letters from the word.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= caption.length &lt;= 150</code></li>
	<li><code>caption</code> consists only of English letters and <code>&#39; &#39;</code>.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Simulation

We first split the title string into words, then process each word. The first word should be all lowercase, while for the subsequent words, the first letter is capitalized and the rest are lowercase. Next, we concatenate all the processed words and add a # symbol at the beginning. Finally, if the generated tag exceeds 100 characters in length, we truncate it to the first 100 characters.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the length of the title string.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def generateTag(self, caption: str) -> str:
        words = [s.capitalize() for s in caption.split()]
        if words:
            words[0] = words[0].lower()
        return "#" + "".join(words)[:99]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
