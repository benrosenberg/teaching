---
title: CSCI 35500 SP 2026
author: "[Go to homepage](https://benrosenberg.info/teaching/sp26/cs355/index.html)"
date: "Last updated: 2026-02-25"
css: "../../../style.css"
toc: true
---

# LP constraint formulation problems

## Q1: Constraint linearity

For each constraint, state whether or not it can be modeled in an LP.

1. $3x + 2y \leq 10$
2. $x^2 + y^2 = 1$ 
3. $xy \leq 5$
4. $\frac{x}{y} = 2$
5. $\sqrt{x} \leq 4$
6. $x = 10$
7. $\max(x,y) \leq 10$
8. $\max(x,y) \geq 10$
9. $\min(x,y) \geq 10$
10. $\min(x,y) \leq 10$
11. $\sin(x) = 0.5$
12. $x + y \neq 5$
13. $x > 3$
14. $x < 3 + 4y$
15. $x = y$

## Q2: Constraint modeling

### Simple constraint modeling

Model each statement as a linear constraint, or explain why it is not possible.

1. We must either produce at least 100 units of Product A, or we produce nothing at all.
2. The total cost of labor and materials cannot exceed \$5,000.
3. For every unit of iron ore used, we must use at least 2 units of copper ore.
4. If we decide to use Machine A, we incur a fixed setup cost of \$500 regardless of how many units we make.
5. If we choose Project A, then we cannot choose Project B.

### Synthetic decision variables

The net balance in an account cannot be negative, but we need to represent a negative balance. Use 2 decision variables to simulate this possibility.