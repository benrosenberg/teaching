---
title: CSCI 35500 SP 2026
author: "[Go to homepage](https://benrosenberg.info/teaching/sp26/cs355/index.html)"
date: "Last updated: 2026-02-26"
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

# Solutions

## Q1: Constraint linearity

For each constraint, state whether or not it can be modeled in an LP.

1. $3x + 2y \leq 10$
   - Yes, this is a normal LP constraint.
2. $x^2 + y^2 = 1$ 
   - No, multiplying decision variables together like $x^2$ is not linear.
   - This is the equation of a circle which is a curved line.
3. $xy \leq 5$
   - No, multiplying decision variables together like $x^2$ is not linear.
4. $\frac{x}{y} = 2$
   - Yes and no - this would be linear because it can be rearranged to $x = 2y$; however, there is a discontinuity at $y = 0$, so it's not convex.
   - Typically you wouldn't write a constraint like this in practice.
5. $\sqrt{x} \leq 4$
   - No, $\sqrt x$ is not linear (it creates a curved line).
6. $x = 10$
   - Yes, we can model this with inequalities like $x\leq 10$, $x\geq 10$.
7. $\max(x,y) \leq 10$
   - Yes, this is linear because the feasible region is convex. (See [this explainer](./min_max_constraint_explainer.html).)
8. $\max(x,y) \geq 10$
   - No, this is not linear because the feasible region is not convex. (See [this explainer](./min_max_constraint_explainer.html).)
10. $\min(x,y) \geq 10$
   - Yes, this is linear because the feasible region is convex. (See [this explainer](./min_max_constraint_explainer.html).)
11. $\min(x,y) \leq 10$
   - No, this is not linear because the feasible region is not convex. (See [this explainer](./min_max_constraint_explainer.html).)
12. $\sin(x) = 0.5$
    - No, this is not linear because $\sin x$ creates a curved line.
13. $x + y \neq 5$
    - No, this is not linear because we can't model $\neq$ (it's not convex).
14. $x > 3$
    - No, we can't model this in an LP because we cannot model strict inequalities like $<$ and $>$.
15. $x < 3 + 4y$
    - No, we can't model this in an LP because we cannot model strict inequalities like $<$ and $>$.
16. $x = y$
    - Yes, this is linear - you can rewrite it as $x - y = 0$; $x$ and $y$ have constant coefficients 1 and -1, and we can model equality using $\leq$ and $\geq$.

## Q2: Constraint modeling

### Simple constraint modeling

Model each statement as a linear constraint, or explain why it is not possible.

1. We must either produce at least 100 units of Product A, or we produce nothing at all.
   - No, this is not modelable in an LP. There is a jump discontinuity in the production function, so it is not convex.
2. The total cost of labor and materials cannot exceed \$5,000.
   - Yes, this is linear and can be modeled like this: $x_L + x_M \leq 5000$.
3. For every unit of iron ore used, we must use at least 2 units of copper ore.
   - Yes, this is linear and can be modeled like this: $x_I \leq 2 x_C$
4. If we decide to use Machine A, we incur a fixed setup cost of \$500 regardless of how many units we make.
   - No, this is not modelable in an LP. There is a jump discontinuity to the right of $x_A = 0$.
5. If we choose Project A, then we cannot choose Project B.
   - No, this is not modelable in an LP.
     - The ILP way to model this would be $x_A + x_B \leq 1; x_A,x_B\in \{0,1\}$.
     - However, this is not convex because the points between 0 and 1 for these decision variables are not contained in the feasible region.

### Synthetic decision variables

The net balance in an account cannot be negative, but we need to represent a negative balance. Use 2 decision variables to simulate this possibility.

We can represent this using $x^+$ and $x^-$ to represent the positive and negative cases for the balance:

- If the balance is positive, then $x^+$ takes on the value of the balance and $x^-$ is equal to 0.
- If the balance is negative, then $x^-$ takes on the value of the balance and $x^+$ is equal to 0.

When using the balance as a variable in the objective function or in our constraints, simply replace $x$ (the variable for the balance) with $x^+ - x^-$.

When we get a solution to the LP, we can calculate the corresponding balance as $x = x^+ - x^-$.