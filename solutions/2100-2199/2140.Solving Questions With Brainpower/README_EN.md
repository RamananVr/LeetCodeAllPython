---
comments: true
difficulty: Medium
edit_url: https://github.com/doocs/leetcode/edit/main/solution/2100-2199/2140.Solving%20Questions%20With%20Brainpower/README_EN.md
rating: 1709
source: Weekly Contest 276 Q3
tags:
    - Array
    - Dynamic Programming
---

<!-- problem:start -->

# [2140. Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower)

## Description

<!-- description:start -->

<p>You are given a <strong>0-indexed</strong> 2D integer array <code>questions</code> where <code>questions[i] = [points<sub>i</sub>, brainpower<sub>i</sub>]</code>.</p>

<p>The array describes the questions of an exam, where you have to process the questions <strong>in order</strong> (i.e., starting from question <code>0</code>) and make a decision whether to <strong>solve</strong> or <strong>skip</strong> each question. Solving question <code>i</code> will <strong>earn</strong> you <code>points<sub>i</sub></code> points but you will be <strong>unable</strong> to solve each of the next <code>brainpower<sub>i</sub></code> questions. If you skip question <code>i</code>, you get to make the decision on the next question.</p>

<ul>
	<li>For example, given <code>questions = [[3, 2], [4, 3], [4, 4], [2, 5]]</code>:

    <ul>
    	<li>If question <code>0</code> is solved, you will earn <code>3</code> points but you will be unable to solve questions <code>1</code> and <code>2</code>.</li>
    	<li>If instead, question <code>0</code> is skipped and question <code>1</code> is solved, you will earn <code>4</code> points but you will be unable to solve questions <code>2</code> and <code>3</code>.</li>
    </ul>
    </li>

</ul>

<p>Return <em>the <strong>maximum</strong> points you can earn for the exam</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> questions = [[3,2],[4,3],[4,4],[2,5]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= questions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>questions[i].length == 2</code></li>
	<li><code>1 &lt;= points<sub>i</sub>, brainpower<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1: Memoization

We design a function $\textit{dfs}(i)$, which represents the maximum score that can be obtained starting from the $i$-th question. The answer is $\textit{dfs}(0)$.

The function $\textit{dfs}(i)$ is calculated as follows:

- If $i \geq n$, it means all questions have been solved, so return $0$;
- Otherwise, let the score of the $i$-th question be $p$, and the number of questions to skip be $b$. Then, $\textit{dfs}(i) = \max(p + \textit{dfs}(i + b + 1), \textit{dfs}(i + 1))$.

To avoid repeated calculations, we can use memoization by storing the values of $\textit{dfs}(i)$ in an array $f$.

The time complexity is $O(n)$, and the space complexity is $O(n)$, where $n$ is the number of questions.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i >= len(questions):
                return 0
            p, b = questions[i]
            return max(p + dfs(i + b + 1), dfs(i + 1))

        return dfs(0)
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- solution:start -->

### Solution 2: Dynamic Programming

We define $f[i]$ as the maximum score that can be obtained starting from the $i$-th problem. Therefore, the answer is $f[0]$.

Considering $f[i]$, let the score of the $i$-th problem be $p$, and the number of problems to skip be $b$. If we solve the $i$-th problem, then we need to solve the problem after skipping $b$ problems, thus $f[i] = p + f[i + b + 1]$. If we skip the $i$-th problem, then we start solving from the $(i + 1)$-th problem, thus $f[i] = f[i + 1]$. We take the maximum value of the two. The state transition equation is as follows:

$$
f[i] = \max(p + f[i + b + 1], f[i + 1])
$$

We calculate the values of $f$ from back to front, and finally return $f[0]$.

The time complexity is $O(n)$, and the space complexity is $O(n)$. Here, $n$ is the number of problems.

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        f = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            p, b = questions[i]
            j = i + b + 1
            f[i] = max(f[i + 1], p + (0 if j > n else f[j]))
        return f[0]
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
