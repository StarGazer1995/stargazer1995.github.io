---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VN56ZZN%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T074725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA1GxDXiRrY%2F4RgUnSsNaVkBxcVuk6NFD2huQZDXyLuxAiAjb9Ma6iEgXDL9laGn6tSA7hYY4xQDki%2FG8rWg%2BuC%2FSSqIBAiH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMySVULUyJgmIxVPXRKtwD0ZW%2FBz782HyfMzKcDtzKS2UKIuZ%2FeOKMZDj9vqjCh3ibzFnfu0vSwl8%2FvGNtAUwZmoI8wNAiM34rUK%2FtK0RjWpQpaZtUVP8iPw2j%2B%2Fn3xUeAK%2B7eKdAbmJUyihVOwS4Ola25J4wWzl%2BxXwbknzZ5tsq3E8h2MEEKvsEWOxnDyAL0EC0wQuQJAE43iNe%2BfFsm8xWWCUCbJ9F4%2B%2FE1x3ixwJYZnrhXAJPhjL20lSq9edjJVo%2FZe4Wb%2FJTneKbKFrYlL5PT%2FBwCI3%2FuxrLjegT94DZeVck1OkpgtpyRmZBWE9nOCSVXmT%2FYSDZI8YhzSqOW8Y%2FBj106sARpz65jVzliPjhGUXjSTd9K4uAJ7tYXuXyIAAXqm6NLsB847PCLD1PeuoOJ9hDT99%2BuSlT9jHSsEnxDHgNkfCtwzvUgxyd%2FUol5EmSeWon5KRZY8w8BU5v3SSSOMI3OQSkMpgn%2BzR0LVXWY7FBFhTlG4oSgEZqToNyR65Yuigj%2FC3WHmAPfCye3cbPyhdzKl%2BwLl9gJNqaqAcBf9v2MkZEYyovQjYuOMV8VbjMCF71L6th0d3RHqW7edxBxWtQ0ZMNtp%2BA9Lq05Vm1sG9Jy3OsW7X%2BhjmKObPK5YKRVwGK%2Fhp%2BAs5sw7P%2Bf0AY6pgEXxbH3Mk5H2A1sPi%2FGWRcZH5U8PnMAJx4j3Isu4VAdICDwF3kZWP5UMwxbt8z2BkBLuJYGaz8UYglIinwg7xIiQt77DEx3EjK8Kld5%2BMOBi%2BQhnVlrs1%2BBB0ws9O962bs%2BeUaGugAHB2rXzkPyNbP2MNyCLK1y%2BB1WjT1fi3bz8fSSk%2BqSSOwCmAPZr03LNze%2B4AX3jY39OmZrfHNoGsni7omypeXa&X-Amz-Signature=65591c766ba6e4be62cebfd980b352ef14b8627d17df837043a30a84105b890a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
