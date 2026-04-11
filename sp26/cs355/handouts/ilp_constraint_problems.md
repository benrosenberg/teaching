---
title: CSCI 35500 SP 2026
author: "[Go to homepage](https://benrosenberg.info/teaching/sp26/cs355/index.html)"
date: "Last updated: 2026-04-11"
css: "../../../style.css"
toc: true
---

# ILP constraint formulation problems

## Q1: Constraint modelability

For each constraint, state whether or not it can be modeled in an ILP.

Assume that $x$ and $y$ are integer variables, and $a$, $b$, $c$ are binary variables.

1. $3x + 2y \leq 10$
2. $x^2 + y^2 = 1$
3. $a^2 + b^2 = 1$
4. $xy \leq 5$
5. $ab \leq 5$
6. $xyz = 0$
7. $abc = 0$
8. $x = 10$
9. $\max(x,y) \leq 10$
10. $\max(x,y) \geq 10$
11. $\min(x,y) \geq 10$
12. $\min(x,y) \leq 10$
13. $\sin(x) = 0.5$
14. $x + y \neq 5$
15. $x > 3$
16. $x < 3 + 4y$
17. $x = y$

## Q2: Constraint modeling

Model each statement as an integer linear constraint.

1. At least one of Project A, Project B, and Project C must be chosen.
2. Exactly one of Project A, Project B, and Project C must be chosen.
3. If we choose Project A, then we cannot choose Project B.
4. We must either produce at least 100 units of Product A, or we produce nothing at all.
5. The total cost of labor and materials cannot exceed \$5,000.
6. For every unit of iron ore used, we must use at least 2 units of copper ore.
7. If we decide to use Machine A, we incur a fixed setup cost of \$500 regardless of how many units we make.