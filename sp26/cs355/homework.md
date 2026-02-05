---
title: CSCI 35500 SP 2026
author: "[Go to homepage](https://benrosenberg.info/teaching/sp26/cs355/index.html)"
date: "Last updated: 2026-02-05"
css: "../../style.css"
toc: true
---

# Homeworks

Homework instructions/advice:

- **Problems will be posted here periodically, until the homework is due.** What is posted here is not necessarily the full homework assigment.
- **Show your work** for all homework problems. Check your work with WolframAlpha, ChatGPT, your calculator, Python, MATLAB, or whatever other resource you want to use.
- All questions on the homework are weighted equally.
- If you wait until the full homework is due to start, you may have more difficulty completing it on time.
- If you have questions on the homework, please ask them in class.
- If you think we didn't cover something in class, feel free to look it up, or ask a question in class.

---

## HW 1 (due date TBD)

### Linear algebra review

#### Problem 1

Define $A$ and $b$ as follows:
$$A = \begin{bmatrix}
3 & 7 & 6 \\ 4 & 1 & 4 \\ 3 & 8 & 7
\end{bmatrix}, b = \begin{bmatrix}
2 \\ 4 \\ 6
\end{bmatrix}$$

Solve the matrix-vector equation $Ax = b$ using row-reduction. You should get integer results.

#### Problem 2

Define $A$ as follows:
$$A = \begin{bmatrix} 1 & 4 & 1 \\ 7 & 5 & 7 \\ 8 & 4 & 8 \end{bmatrix}$$

Show that $A$ is not invertible, and give a nontrivial solution to $Ax = 0$.

#### Problem 3

Define $A$ as follows:
$$A = \begin{bmatrix} 1 & 4 \\ 7 & 5 \end{bmatrix}$$

Find $AA^\intercal$.

#### Problem 4

Give a counterexample that shows matrix multiplication is not commutative for $2\times 2$ matrices.

#### Problem 5

Show that $I_2A = A$ for all matrices $A$ with dimension $2\times 2$.

### Linear programming basics

#### Problem 7

A small bakery makes two types of muffins: blueberry and chocolate chip. Each blueberry muffin requires 0.5 cups of flour and 0.25 cups of sugar. Each chocolate chip muffin requires 0.5 cups of flour and 0.5 cups of sugar. The bakery has 20 cups of flour and 15 cups of sugar available each day. The profit from each blueberry muffin is \$2, and the profit from each chocolate chip muffin is \$3. The bakery wants to maximize its daily profit.

You will create and solve a linear program that models the above scenario:

- Define the decision variables you will use in your LP model, and state what they represent. (You should have two decision variables.)
- List the constraints in your LP model in terms of the decision variables you created.
- State the objective function of your LP model in terms of the decision variables.
- Convert the LP to canonical form (if necessary), and state the contents of $A$, $c$, and $b$, as they correspond respectively to the matrix and vectors in the canonical $\max c^\intercal x$ s.t. $Ax\leq b$, $x\geq 0$ format.
- Graph the feasible region of your LP model (since you should have 2 decision variables, you should be able to graph this in 2 dimensions) and determine the solution.

#### Problem 8

Note: this problem is a little more complex than the above problem, but is still possible to model using 3 decision variables (for the obvious quantities).

A furniture company produces three types of chairs: basic, deluxe, and executive. The production of each chair requires different amounts of wood, labor, and fabric. The company wants to maximize its profit given its limited daily resources.

The company's goal is to maximize profit. The profit for each chair type, along with its material cost, is as follows:

- Basic chair: \$100
  - Wood cost: 3 units
  - Labor cost: 2 units
  - Fabric cost: 2 units
- Deluxe chair: \$150
  - Wood cost: 5 units
  - Labor cost: 3 units
  - Fabric cost: 6 units
- Executive chair: \$250
  - Wood cost: 4 units
  - Labor cost: 5 units
  - Fabric cost: 8 units

The company has these additional constraints:

- The amount of wood used must be less than or equal to the amount of fabric used.
- The total number of labor used cannot exceed 20 units.
- Any unused labor (under the 20-unit limit) costs the company \$20 per unit, due to the additional upkeep on the company ping-pong tables that the employees use when not working.

You will create (but not solve) a linear program that models the above problem:

- Define the decision variables you will use in your LP model, and state what they represent. (You should have three decision variables.)
- List the constraints in your LP model in terms of the decision variables you created.
- State the objective function of your LP model in terms of the decision variables.
- Convert the LP to canonical form (if necessary), and state the contents of $A$, $c$, and $b$, as they correspond respectively to the matrix and vectors in the canonical $\max c^\intercal x$ s.t. $Ax\leq b$, $x\geq 0$ format.

More problems will be added...

---
