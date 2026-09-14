---
comments: true
difficulty: Medium
rating: 1678
source: Biweekly Contest 68 Q2
tags:
    - Graph
    - Topological Sort
    - Array
    - Hash Table
    - String
    - Directed Acyclic Graph
---

<!-- problem:start -->

# [2115. Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies)

## Description

<!-- description:start -->

<p>You have information about <code>n</code> different recipes. You are given a string array <code>recipes</code> and a 2D string array <code>ingredients</code>. The <code>i<sup>th</sup></code> recipe has the name <code>recipes[i]</code>, and you can <strong>create</strong> it if you have <strong>all</strong> the needed ingredients from <code>ingredients[i]</code>. A recipe can also be an ingredient for <strong>other </strong>recipes, i.e., <code>ingredients[i]</code> may contain a string that is in <code>recipes</code>.</p>

<p>You are also given a string array <code>supplies</code> containing all the ingredients that you initially have, and you have an infinite supply of all of them.</p>

<p>Return <em>a list of all the recipes that you can create. </em>You may return the answer in <strong>any order</strong>.</p>

<p>Note that two recipes may contain each other in their ingredients.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> recipes = [&quot;bread&quot;], ingredients = [[&quot;yeast&quot;,&quot;flour&quot;]], supplies = [&quot;yeast&quot;,&quot;flour&quot;,&quot;corn&quot;]
<strong>Output:</strong> [&quot;bread&quot;]
<strong>Explanation:</strong>
We can create &quot;bread&quot; since we have the ingredients &quot;yeast&quot; and &quot;flour&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> recipes = [&quot;bread&quot;,&quot;sandwich&quot;], ingredients = [[&quot;yeast&quot;,&quot;flour&quot;],[&quot;bread&quot;,&quot;meat&quot;]], supplies = [&quot;yeast&quot;,&quot;flour&quot;,&quot;meat&quot;]
<strong>Output:</strong> [&quot;bread&quot;,&quot;sandwich&quot;]
<strong>Explanation:</strong>
We can create &quot;bread&quot; since we have the ingredients &quot;yeast&quot; and &quot;flour&quot;.
We can create &quot;sandwich&quot; since we have the ingredient &quot;meat&quot; and can create the ingredient &quot;bread&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> recipes = [&quot;bread&quot;,&quot;sandwich&quot;,&quot;burger&quot;], ingredients = [[&quot;yeast&quot;,&quot;flour&quot;],[&quot;bread&quot;,&quot;meat&quot;],[&quot;sandwich&quot;,&quot;meat&quot;,&quot;bread&quot;]], supplies = [&quot;yeast&quot;,&quot;flour&quot;,&quot;meat&quot;]
<strong>Output:</strong> [&quot;bread&quot;,&quot;sandwich&quot;,&quot;burger&quot;]
<strong>Explanation:</strong>
We can create &quot;bread&quot; since we have the ingredients &quot;yeast&quot; and &quot;flour&quot;.
We can create &quot;sandwich&quot; since we have the ingredient &quot;meat&quot; and can create the ingredient &quot;bread&quot;.
We can create &quot;burger&quot; since we have the ingredient &quot;meat&quot; and can create the ingredients &quot;bread&quot; and &quot;sandwich&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == recipes.length == ingredients.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= ingredients[i].length, supplies.length &lt;= 100</code></li>
	<li><code>1 &lt;= recipes[i].length, ingredients[i][j].length, supplies[k].length &lt;= 10</code></li>
	<li><code>recipes[i], ingredients[i][j]</code>, and <code>supplies[k]</code> consist only of lowercase English letters.</li>
	<li>All the values of <code>recipes</code> and <code>supplies</code>&nbsp;combined are unique.</li>
	<li>Each <code>ingredients[i]</code> does not contain any duplicate values.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution 1

<!-- thinking:start -->

> **Thinking**
>
> A recipe is cookable once every ingredient is available from the initial supplies or from already cooked recipes, which is a directed dependency graph. Rechecking ingredients per recipe repeats work and mishandles chains.
>
> Point each ingredient to recipes that need it, with in-degree equal to the number of ingredients. Supplies are the sources; a recipe whose in-degree falls to zero can be cooked and used to unlock others.
>
> We build that graph and run Kahn’s algorithm from $\textit{supplies}$, appending a recipe when its in-degree hits zero.

<!-- thinking:end -->

<!-- tabs:start -->

#### Python3

```python
class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:
        g = defaultdict(list)
        indeg = defaultdict(int)
        for a, b in zip(recipes, ingredients):
            for v in b:
                g[v].append(a)
            indeg[a] += len(b)
        q = supplies
        ans = []
        for i in q:
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    ans.append(j)
                    q.append(j)
        return ans
```

<!-- tabs:end -->

<!-- solution:end -->

<!-- problem:end -->
