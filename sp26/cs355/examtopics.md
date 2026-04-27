---
title: CSCI 35500 SP 2026
author: "[Go to homepage](https://benrosenberg.info/teaching/sp26/cs355/index.html)"
date: "Last updated: 2026-04-26"
css: "../../style.css"
toc: true
---

Here are lists of topics to study for the exams.

# Midterm exam topics

## Linear algebra review

- Matrix multiplication
- Matrix inverse
- Solving $Ax = b$ for $x$
- Linear independence/invertibility for matrices

## Linear programming theory

- Knowing how many optimal solutions an LP can have
- Geometric interpretation of an LP's objective function
- Identifying whether a shape/set is convex or not
- Knowing runtime guarantees for LP solving
- Knowing why the feasible region of an LP is always convex

## LP modeling

- Knowing whether a constraint is modelable in a linear program
- Sketching feasible regions for an LP and determining whether it is feasible, infeasible, or unbounded, based on the feasible region and the objective function direction
- Being able to understand how the LP model of a problem we have seen in class, such as max flow, will be modified by the introduction of new elements (see HW 1 problem 18)

## LP integrality

- Knowing whether it is sufficient to have all integer $A, b, c$ to have a guarantee of obtaining an all-integer optimal solution for an LP
- Understanding whether modifications to an existing problem preserve integrality (see HW 1 problem 18)

## Runtime complexity analysis

- Being able to determine big-O time complexity for a Python function

---

# Final exam topics

## ILP solving

- Familiarity with branch and bound
- Knowing how to create a branch and bound tree, using a table for the LP-relaxation solutions (see homework 2 problems for examples of table-oriented approach)
- Understanding the relationship between an ILP and its LP-relaxation

## ILP theory

- Knowing what the feasible regions of an ILP look like
- Knowing how many ILP-feasible points there are based on the number of and types of decision variables in a problem
- Having the geometric intuition to understand when the number of ILP-feasible solutions will be large or small, and how that changes with problem coefficients

## ILP formulations

- Being able to formulate an ILP for combinatorial problems (similar to those discussed as examples in lecture, and the ILP project)
- Being able to do small proofs (by induction or otherwise) for certain problem characteristics
- Understanding how to modify formulations to remove or add dimensions to decision variables, and how that changes the variables' domain
- Knowing how to determine the number of constraints and variables there are in a model formulation to get an idea of model size

## ILP constraints and variable relationships

- Knowing how to represent relationships between variables in an ILP formulation
- Knowing which relationships are representable and which are not
- Familiarity with binary relationships between variables (AND, OR, NOT, IMPLIES, etc.) and how they can be represented in an ILP
- Understanding which types of optimization problems can be formulated as ILPs and which cannot

## ILP formulation tricks

- Understanding how the big-$M$ method works
- Understanding what the tradeoff is in the size of the big-$M$ constant

## Miscellaneous topics

- Understanding of the TSP formulation we discussed in class
- (A small number of) questions may be asked about topics discussed briefly in person during class and not listed above, making up no more than 3% of the total exam by point value

# Final exam point breakdown

Not finalized, but to give an idea of what the exam will look like:

- Roughly a quarter multiple-choice questions
- Roughly 1/8 will be computational questions
- Roughly 3/8 will be coming up with ILP formulations
- Roughly a quarter will be theory/thinking questions
